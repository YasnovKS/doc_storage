from django import forms

from .models import Document


class CreateForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'field',
                    'placeholder': 'Наименование документа'
                }
            ),
            'content': forms.Textarea(attrs={'class': 'text-field',
                                             'placeholder': 'Содержание'}),
        }


class EditForm(CreateForm):

    class Meta(CreateForm.Meta):
        fields = ['title', 'content', 'for_deleting']
