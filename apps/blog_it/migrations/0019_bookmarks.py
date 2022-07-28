# Generated by Django 3.2.10 on 2022-07-28 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0011_remove_forummodel_bookmarks'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_it', '0018_upvotemodel_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookmark_blog', to='blog_it.blogmodel')),
                ('forum', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookmark_forum', to='forum.forummodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmark_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]