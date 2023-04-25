from django.db import models
import reversion
from django.contrib.auth import get_user_model

User = get_user_model()


@reversion.register()
class Document(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Наименование')
    content = models.TextField(verbose_name='Содержание')
    date = models.DateField(auto_now_add=True,
                            verbose_name='Дата создания')
    author = models.ForeignKey(User,
                               verbose_name='Автор документа',
                               on_delete=models.DO_NOTHING,
                               )

    class Meta:
        ordering = ['-date']
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
