from django.contrib import admin
from .models import UserGroup, User, MenuItem, UserGroupMenuItem
# Register your models here.
admin.site.register([UserGroup, User, MenuItem, UserGroupMenuItem])

