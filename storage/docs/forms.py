from django import forms
from .models import Document


class PostForm(forms.ModelForm):

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
