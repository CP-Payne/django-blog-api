# Generated by Django 5.0.3 on 2024-03-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog_app", "0002_remove_blog_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="snippet",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
