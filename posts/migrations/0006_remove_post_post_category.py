# Generated by Django 3.1.3 on 2020-11-19 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_category',
        ),
    ]
