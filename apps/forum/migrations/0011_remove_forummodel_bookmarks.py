# Generated by Django 3.2.10 on 2022-07-26 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_forummodel_bookmarks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forummodel',
            name='bookmarks',
        ),
    ]
