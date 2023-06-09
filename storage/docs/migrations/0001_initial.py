# Generated by Django 4.2 on 2023-04-26 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Автор документа')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
                'ordering': ['-date'],
            },
        ),
    ]
