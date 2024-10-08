# Generated by Django 5.0.3 on 2024-08-10 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_app", "0006_remove_user_posts"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="facebook",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="instagram",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="twitter",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="website",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
