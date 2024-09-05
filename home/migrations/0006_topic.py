# Generated by Django 5.0.3 on 2024-07-22 19:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_posts_is_private"),
    ]

    operations = [
        migrations.CreateModel(
            name="Topic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("self_portraits", models.FloatField(default=0.0)),
                ("art", models.FloatField(default=0.0)),
                ("fashion_style", models.FloatField(default=0.0)),
                ("products", models.FloatField(default=0.0)),
                ("creative_projects", models.FloatField(default=0.0)),
                ("events", models.FloatField(default=0.0)),
                ("photography_techniques", models.FloatField(default=0.0)),
                ("themes_challenges", models.FloatField(default=0.0)),
                ("inspiration_ideas", models.FloatField(default=0.0)),
                ("comparisons", models.FloatField(default=0.0)),
                (
                    "post",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_topics",
                        to="home.posts",
                    ),
                ),
            ],
        ),
    ]
