# Generated by Django 5.0.4 on 2024-04-24 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_rename_posts_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateField(default=datetime.datetime(2024, 4, 24, 18, 45, 49, 328803)),
        ),
    ]
