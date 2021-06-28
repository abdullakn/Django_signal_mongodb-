from django.contrib import admin
from .models import User, UserData,BlogPost

# Register your models here.

admin.site.register(UserData)
admin.site.register(BlogPost)
