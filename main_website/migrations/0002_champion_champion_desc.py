# Generated by Django 4.1 on 2022-09-10 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='champion',
            name='champion_desc',
            field=models.TextField(default=250, max_length=300),
            preserve_default=False,
        ),
    ]
