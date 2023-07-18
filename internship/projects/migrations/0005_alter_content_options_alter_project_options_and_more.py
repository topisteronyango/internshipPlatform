# Generated by Django 4.1.9 on 2023-07-03 13:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0004_alter_content_content_type"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="content",
            options={"ordering": ["-order"]},
        ),
        migrations.AlterModelOptions(
            name="project",
            options={"ordering": ["-order"]},
        ),
        migrations.AddField(
            model_name="specialization",
            name="students",
            field=models.ManyToManyField(
                blank=True,
                related_name="specializations_joined",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]