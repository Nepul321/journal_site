# Generated by Django 4.2.5 on 2023-11-01 02:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_alter_post_citations_alter_post_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='article_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]