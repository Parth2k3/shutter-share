# Generated by Django 5.0.3 on 2024-07-14 18:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_posts"),
        ("user_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="bio",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="followers",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="user_followers",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="following",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="user_following",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="posts",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="home.posts",
            ),
        ),
    ]
