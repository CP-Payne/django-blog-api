# Generated by Django 5.0.3 on 2024-03-10 08:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="tags",
        ),
    ]