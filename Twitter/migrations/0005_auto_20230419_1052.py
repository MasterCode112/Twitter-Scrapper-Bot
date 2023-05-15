# Generated by Django 3.2.16 on 2023-04-19 10:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Twitter', '0004_auto_20230419_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_settings',
            name='C_Id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='c_settings',
            name='since',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 18, 10, 52, 15, 383261, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='d_settings',
            name='since',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 18, 10, 52, 15, 316495, tzinfo=utc)),
        ),
    ]