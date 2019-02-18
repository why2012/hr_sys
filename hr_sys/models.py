from django.db import models

# Create your models here.
class UserGroup(models.Model):
    name = models.CharField(max_length=255, unique=True)
    remark = models.TextField(default="", null=True)

class User(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    user_group = models.ForeignKey(UserGroup, on_delete=models.DO_NOTHING)

class MenuItem(models.Model):
    name = models.CharField(max_length=255, unique=True)
    icon_url = models.CharField(max_length=255, null=True, default="")
    link_url = models.CharField(max_length=255, null=True, default="")
    type = models.SmallIntegerField(default=1) # 0: parent 1: child
    order = models.IntegerField(default=10000)
    parent_id = models.IntegerField(default=-1, null=True)

class UserGroupMenuItem(models.Model):
    user_group = models.ForeignKey(UserGroup, on_delete=models.DO_NOTHING)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.DO_NOTHING)