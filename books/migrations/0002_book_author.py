# Generated by Django 4.0.3 on 2022-04-12 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, null=True, verbose_name='nome do autor'),
        ),
    ]
