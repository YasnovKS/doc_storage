from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from docs.models import Document

User = get_user_model()


class TestDocsViews(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = User.objects.create(username='User')

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def setUp(self) -> None:
        super().setUp()
        self.client = Client()
        self.client.force_login(self.user)

    def test_doc_create(self):
        'Testing the document created succesfully.'
        documents_count = Document.objects.all().count()

        data = {
            'title': 'New document',
            'content': 'new content',
            'author': self.user
        }
        self.client.post(reverse('docs:doc_create'), data=data)

        updated_count = Document.objects.all().count()
        self.assertEqual(updated_count, documents_count + 1,
                         'Новый документ создается некорректно.')

    def test_doc_update(self):
        '''Test updating the document.'''

        data = {
            'title': 'Old document',
            'content': 'Old content',
            'author': self.user
        }
        Document.objects.create(**data)
        doc_id = Document.objects.all().first().id
        start_count = Document.objects.all().count()

        form = {
            'title': 'Old document',
            'content': 'New content',
        }
        self.client.post(reverse('docs:doc_edit', kwargs={'pk': doc_id}),
                         form, follow=True)
        end_count = Document.objects.all().count()
        checked_document = Document.objects.get(pk=doc_id)
        self.assertEqual(start_count, end_count,
                         'Редактирование документов работает некорректно')
        self.assertEqual(checked_document.content, form['content'],
                         'Редактирование документов работает некорректно')

    def test_doc_delete(self):
        data = {
            'title': 'Old document',
            'content': 'Old content',
            'author': self.user,
        }
        self.client.post(reverse('docs:doc_create'), data=data)
        del_data = {
            'title': 'Old document',
            'content': 'Old content',
            'author': self.user,
            'for_deleting': True,
        }
        docs = Document.objects.all()
        start_count = docs.count()
        first_doc = docs.first()
        self.client.post(
            reverse(
                'docs:doc_edit', kwargs={'pk': first_doc.id}
            ),
            del_data,
            follow=True,
        )
        end_count = Document.objects.all().count()
        self.assertEqual(start_count - 1, end_count)
