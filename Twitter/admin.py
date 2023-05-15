from django.contrib import admin
from .models import C_Settings, Result_Output, D_Settings, Auth_users, UserProfile
# Register your models here.

admin.site.register(C_Settings)
admin.site.register(Result_Output)
admin.site.register(D_Settings)
admin.site.register(Auth_users)
admin.site.register(UserProfile)