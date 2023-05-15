# Generated by Django 3.2.16 on 2023-04-19 13:01

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Twitter', '0007_auto_20230419_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auth_users',
            fields=[
                ('Primary_key', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('User_uniq_Id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('Names', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
                ('Reg_Date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RenameField(
            model_name='result_output',
            old_name='R_ID',
            new_name='R_Unique_ID',
        ),
        migrations.AddField(
            model_name='c_settings',
            name='Seted_Day',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='d_settings',
            name='Seted_Day',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='c_settings',
            name='since',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 18, 13, 1, 47, 791716, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='d_settings',
            name='since',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 18, 13, 1, 47, 791133, tzinfo=utc)),
        ),
    ]