# Generated by Django 3.2.18 on 2023-05-12 19:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Twitter', '0014_auto_20230512_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='c_settings',
            name='Primary_key',
        ),
        migrations.RemoveField(
            model_name='d_settings',
            name='Primary_key',
        ),
        migrations.AddField(
            model_name='c_settings',
            name='id',
            field=models.AutoField(default=django.utils.timezone.now, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='d_settings',
            name='id',
            field=models.AutoField(default=django.utils.timezone.now, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='c_settings',
            name='since',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 11, 19, 32, 29, 766765, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='d_settings',
            name='since',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 11, 19, 32, 29, 765846, tzinfo=utc)),
        ),
    ]