# Generated by Django 4.1 on 2023-02-15 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_website", "0004_challvideos_champions_championspresentations_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="championspresentations",
            name="presentation_name",
            field=models.CharField(
                db_column="PRESENTATION_NAME", max_length=60, null=True
            ),
        ),
    ]