# Generated by Django 3.2.10 on 2022-07-16 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_alter_forummodel_view_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forummodel',
            name='stt',
            field=models.IntegerField(default=1),
        ),
    ]
