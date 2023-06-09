# Generated by Django 3.2.18 on 2023-05-19 19:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='Result_Output',
            fields=[
                ('R_Id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('FileName', models.CharField(default=None, max_length=100)),
                ('UserScreenName', models.CharField(max_length=100, null=True)),
                ('UserName', models.CharField(max_length=100, null=True)),
                ('Timestamp', models.DateTimeField()),
                ('Text', models.TextField(null=True)),
                ('Embedded_text', models.TextField(null=True)),
                ('Emojis', models.CharField(max_length=100, null=True)),
                ('Comments', models.TextField(null=True)),
                ('Likes', models.IntegerField(null=True)),
                ('Retweets', models.IntegerField(null=True)),
                ('Imag_link', models.CharField(max_length=100, null=True)),
                ('Tweet_URL', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('status_scraping', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='D_Settings',
            fields=[
                ('D_Id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('from_account', models.CharField(max_length=80, null=True)),
                ('to_account', models.CharField(max_length=80, null=True)),
                ('mention_account', models.TextField(null=True)),
                ('hashtag', models.CharField(max_length=80, null=True)),
                ('until', models.DateTimeField(default=django.utils.timezone.now)),
                ('since', models.DateTimeField(default=datetime.datetime(2023, 5, 18, 19, 1, 32, 576563, tzinfo=utc))),
                ('interval', models.IntegerField(default=1)),
                ('lang', models.CharField(default='en', max_length=8)),
                ('headless', models.BooleanField(default=True)),
                ('limit', models.IntegerField(null=True)),
                ('display_type', models.CharField(default='Latest', max_length=30)),
                ('resume', models.CharField(max_length=80, null=True)),
                ('proxy', models.CharField(max_length=20, null=True)),
                ('proximity', models.CharField(max_length=20, null=True)),
                ('geocode', models.CharField(max_length=80, null=True)),
                ('minreplies', models.IntegerField(null=True)),
                ('minlikes', models.IntegerField(null=True)),
                ('minretweets', models.IntegerField(null=True)),
                ('Seted_Day', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='C_Settings',
            fields=[
                ('C_Id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('from_account', models.CharField(max_length=80, null=True)),
                ('to_account', models.CharField(max_length=80, null=True)),
                ('mention_account', models.TextField(null=True)),
                ('hashtag', models.CharField(max_length=80, null=True)),
                ('until', models.DateTimeField(default=django.utils.timezone.now)),
                ('since', models.DateTimeField(default=datetime.datetime(2023, 5, 18, 19, 1, 32, 577536, tzinfo=utc))),
                ('interval', models.IntegerField(default=1)),
                ('lang', models.CharField(default='en', max_length=8)),
                ('headless', models.BooleanField(default=True)),
                ('limit', models.IntegerField(null=True)),
                ('display_type', models.CharField(default='Latest', max_length=30)),
                ('resume', models.CharField(max_length=100, null=True)),
                ('proxy', models.CharField(max_length=20, null=True)),
                ('proximity', models.CharField(max_length=20, null=True)),
                ('geocode', models.CharField(max_length=100, null=True)),
                ('minreplies', models.IntegerField(null=True)),
                ('minlikes', models.IntegerField(null=True)),
                ('minretweets', models.IntegerField(null=True)),
                ('Seted_Day', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
