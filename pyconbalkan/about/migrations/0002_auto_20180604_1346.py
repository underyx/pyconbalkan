# Generated by Django 2.0.5 on 2018-06-04 13:46

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=markdownx.models.MarkdownxField(blank=True, null=True),
        ),
    ]