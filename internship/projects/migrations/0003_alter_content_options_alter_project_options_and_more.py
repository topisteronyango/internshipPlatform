# Generated by Django 4.1.9 on 2023-06-23 19:36

from django.db import migrations
import projects.fields


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_video_text_image_file_content"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="content",
            options={"ordering": ["order"]},
        ),
        migrations.AlterModelOptions(
            name="project",
            options={"ordering": ["order"]},
        ),
        migrations.AddField(
            model_name="content",
            name="order",
            field=projects.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="project",
            name="order",
            field=projects.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
    ]