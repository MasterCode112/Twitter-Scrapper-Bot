# Generated by Django 3.2.18 on 2023-05-19 19:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Twitter', '0002_auto_20230519_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_settings',
            name='since',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 18, 19, 23, 57, 94442, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='d_settings',
            name='since',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 18, 19, 23, 57, 93569, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='status_scraping',
            field=models.CharField(default='checked', max_length=20),
        ),
    ]
