# Generated by Django 3.1.3 on 2020-11-18 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='images',
        ),
    ]
