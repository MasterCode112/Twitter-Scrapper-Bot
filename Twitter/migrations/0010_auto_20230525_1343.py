# Generated by Django 3.2.18 on 2023-05-25 13:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Twitter', '0009_auto_20230525_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_settings',
            name='from_account',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='c_settings',
            name='mention_account',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='c_settings',
            name='minlikes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='c_settings',
            name='minreplies',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='c_settings',
            name='minretweets',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='c_settings',
            name='proximity',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='c_settings',
            name='proxy',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='c_settings',
            name='since',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 24, 13, 43, 48, 657005, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='c_settings',
            name='to_account',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='c_settings',
            name='words',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='d_settings',
            name='proximity',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='d_settings',
            name='since',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 24, 13, 43, 48, 656099, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='result_output',
            name='FileName',
            field=models.CharField(max_length=100, null=True),
        ),
    ]