from django import forms
from .models import Document


class PostForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'content']
