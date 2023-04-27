import reversion
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


@reversion.register()
class Document(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Наименование',
                             help_text='Наименование',
                             )
    content = models.TextField(verbose_name='Содержание',
                               help_text='Содержание',
                               )
    date = models.DateField(auto_now_add=True,
                            verbose_name='Дата создания')
    author = models.ForeignKey(User,
                               verbose_name='Автор документа',
                               on_delete=models.DO_NOTHING,
                               )
    for_deleting = models.BooleanField(default=False,
                                       verbose_name='На удаление',
                                       help_text='Пометить на удаление')

    class Meta:
        ordering = ['date']
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
