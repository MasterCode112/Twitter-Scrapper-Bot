from django.db import models
from django.utils import timezone
import uuid
from django.contrib.auth.models import User

class Auth_users(models.Model):
    Primary_key = models.AutoField(primary_key=True, unique=True, null=False)
    User_uniq_Id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True, null=False)
    Names  = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    username = models.CharField(max_length=30, null=False)
    Password = models.CharField(max_length=30, null=False)
    Reg_Date = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return "{}".format(self.Primary_key)

# Django by default have user table and register table.....

# Default Settings 
# class D_Settings(models.Model):
#     D_Id = models.IntegerField(primary_key=True, auto_created=True, unique=True, null=False)
#     from_account = models.CharField(max_length=300, null=True)
#     to_account = models.CharField(max_length=300, null=True)
#     mention_account = models.CharField(max_length=255, null=True)
#     hashtag = models.CharField(max_length=300, null=True)
#     until = models.DateTimeField(default=timezone.now)
#     since = models.DateTimeField(default=timezone.now() - timezone.timedelta(days=1))
#     interval = models.IntegerField(default=1)
#     lang = models.CharField(max_length=8, default='en')
#     headless = models.BooleanField(Default=True)
#     limit = models.IntegerField()
#     display_type = models.CharField(max_length=30, default='Latest')
#     resume = models.CharField(max_length=300)
#     proxy = models.CharField(max_length=20)
#     proximity = models.CharField(max_length=20)
#     geocode = models.CharField(max_length=300)
#     minreplies = models.IntegerField()
#     minlikes = models.IntegerField()
#     minretweets = models.IntegerField()


# # Custom settings
# class C_Settings(models.Model):
#     C_Id = models.IntegerField(primary_key=True, auto_created=True, null=False, unique=True)
#     from_account = models.CharField(max_length=100, null=True)
#     to_account = models.CharField(max_length=100, null=True)
#     mention_account = models.CharField(max_length=255, null=True)
#     hashtag = models.CharField(max_length=100, null=True)
#     until = models.DateTimeField(default=timezone.now)
#     since = models.DateTimeField(default=timezone.now() - timezone.timedelta(days=1))
#     interval = models.IntegerField(default=1)
#     lang = models.CharField(max_length=8, default='en')
#     headless = models.BooleanField(Default=True)
#     limit = models.IntegerField()
#     display_type = models.CharField(max_length=30, default='Latest')
#     resume = models.CharField(max_length=300)
#     proxy = models.CharField(max_length=20)
#     proximity = models.CharField(max_length=20)
#     geocode = models.CharField(max_length=300)
#     minreplies = models.IntegerField()
#     minlikes = models.IntegerField()
#     minretweets = models.IntegerField()

# class Result_Output(models.Model):
#     R_Id = models.IntegerField(primary_key=True, auto_created=True, null=True, unique=True)
#     FileName = models.CharField(max_length=300, default=null)
#     UserScreenName = models.CharField(max_length=100, null=True)
#     UserName = models.CharField(max_length=100, null=True)
#     Timestamp = models.DateTimeField(null=False)
#     Text = models.TextField()
#     Embedded_text = models.TextField()
#     Emojis = models.CharField(max_length=100)
#     Comments = models.TextField()
#     Likes = models.IntegerField()
#     Retweets = models.IntegerField()
#     Imag_link = models.CharField(max_length=100)
#     Tweet_URL = models.CharField(max_length=100)



class D_Settings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    D_Id = models.AutoField(primary_key=True, unique=True)
    from_account = models.CharField(max_length=80, null=True)
    to_account = models.CharField(max_length=80, null=True)
    mention_account = models.TextField(null=True)
    hashtag = models.CharField(max_length=80, null=True)
    until = models.DateTimeField(default=timezone.now)
    since = models.DateTimeField(default=timezone.now() - timezone.timedelta(days=1))
    interval = models.IntegerField(default=1)
    lang = models.CharField(max_length=8, default='en')
    headless = models.BooleanField(default=True)
    limit = models.IntegerField(null=True)
    display_type = models.CharField(max_length=30, default='Latest')
    resume = models.BooleanField(default=False)
    proxy = models.CharField(max_length=20, null=True)
    proximity = models.CharField(max_length=20, null=True)
    geocode = models.CharField(max_length=80, default="-5.93075788869572, 35.890266339859565")
    minreplies = models.IntegerField(null=True)
    minlikes = models.IntegerField(null=True)
    minretweets = models.IntegerField(null=True)
    Seted_Day = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}".format(self.D_Id)



class C_Settings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    C_Id = models.AutoField(primary_key=True, null=False, unique=True)
    from_account = models.CharField(max_length=80, null=True)
    to_account = models.CharField(max_length=80, null=True)
    mention_account = models.TextField(null=True)
    hashtag = models.CharField(max_length=80, null=True)
    until = models.DateTimeField(default=timezone.now)
    since = models.DateTimeField(default=timezone.now() - timezone.timedelta(days=1))
    interval = models.IntegerField(default=5)
    lang = models.CharField(max_length=8, default='en')
    headless = models.BooleanField(default=True)
    limit = models.IntegerField(null=True)
    display_type = models.CharField(max_length=30, default='Top')
    resume = models.BooleanField(default=False)
    proxy = models.CharField(max_length=20, null=True)
    proximity = models.CharField(max_length=20, null=True)
    geocode = models.CharField(max_length=100, default="-5.93075788869572, 35.890266339859565")
    minreplies = models.IntegerField(null=True)
    minlikes = models.IntegerField(null=True)
    minretweets = models.IntegerField(null=True)
    Seted_Day = models.DateTimeField(default=timezone.now)
    words = models.CharField(max_length=300, null=True)
    

    def __str__(self):
        return "{}".format(self.C_Id)

class Result_Output(models.Model):
    R_Id = models.AutoField(primary_key=True, null=False, unique=True)
    FileName = models.CharField(max_length=100, null=True)
    UserScreenName = models.CharField(max_length=100, null=True)
    UserName = models.CharField(max_length=100, null=True)
    Timestamp = models.DateTimeField(null=False)
    Text = models.TextField(null=True)
    Embedded_text = models.TextField(null=True)
    Emojis = models.CharField(max_length=100, null=True)
    Comments = models.TextField(null=True)
    Likes = models.IntegerField(null=True)
    Retweets = models.IntegerField(null=True)
    Imag_link = models.CharField(max_length=100, null=True)
    Tweet_URL = models.CharField(max_length=100, null=True)
    

    def __str__(self):
        return "{}".format(self.R_Id)



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    status_scraping = models.CharField(max_length=20, default="d_settings")  

    def __str__(self):
        return "{}".format(self.pk)