# Generated by Django 2.1.7 on 2019-03-22 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0012_auto_20190321_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='logo',
            field=models.FileField(upload_to=''),
        ),
    ]
