# Generated by Django 3.2.18 on 2023-05-30 11:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Twitter', '0014_auto_20230530_1140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='statusS',
            new_name='status_scraping',
        ),
        migrations.AlterField(
            model_name='c_settings',
            name='since',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 29, 11, 41, 40, 514185, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='d_settings',
            name='since',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 29, 11, 41, 40, 513112, tzinfo=utc)),
        ),
    ]
