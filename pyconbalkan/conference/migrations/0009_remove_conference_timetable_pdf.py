# Generated by Django 2.2.4 on 2019-09-08 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0008_auto_20190303_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conference',
            name='timetable_pdf',
        ),
    ]
