# coding: utf-8

from django.db import models

# Create your models here.
# 系统用户权限部分
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

# 用户组权限
class UserGroupMenuItem(models.Model):
    user_group = models.ForeignKey(UserGroup, on_delete=models.DO_NOTHING)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.DO_NOTHING)

# 员工部分
class Department(models.Model):
    name = models.CharField(max_length=255)
    parent_id = models.IntegerField(default=-1)

# 员工职级
#       P5              T5
#       /\--------      /\
#       /\        ------/\
#       P4              T4
#       /\ -------      /\
#       /\        ------/\
#       P3              T3
#       /\              /\
#       /\              /\
#       P2              T2
#       /\              /\
#       /\              /\
#       P1              T1
# P 1-5 T 6-10
class EmployeeLevel(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField()
    next_level_id = models.IntegerField()

# 员工职位
class EmployeePosition(models.Model):
    name = models.CharField(max_length=255)

# 员工信息
class Employee(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=50, choices=((0, "male"), (1, "female")))
    email = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=50, null=True)
    manager_id = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    province_name = models.CharField(max_length=50)
    city_name = models.CharField(max_length=50)
    salary = models.PositiveIntegerField()
    level = models.ForeignKey(EmployeeLevel, on_delete=models.DO_NOTHING)
    position = models.ForeignKey(EmployeePosition, on_delete=models.DO_NOTHING)
    status = models.SmallIntegerField(choices=((0, "normal"),(1, "desert")))

# 员工晋升记录
class EmployPromoteHistory(models.Model):
    type = models.SmallIntegerField(choices=((0, "promote"),(1, "desert"), (2, "demote")))
    log_time = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    from_level = models.ForeignKey(EmployeeLevel, related_name="from_level_fk", on_delete=models.DO_NOTHING)
    to_level = models.ForeignKey(EmployeeLevel, related_name="to_level_fk", on_delete=models.DO_NOTHING)

# 员工考勤记录
class EmployeeAttendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    type = models.SmallIntegerField(choices=((0, "ontime"), (1, "late")))
    standard_time = models.SmallIntegerField() # 0~23 * 60 一天内的考勤时间点
    check_time = models.DateTimeField(auto_now_add=True)

# 其他杂项
# kv record
class KeyValue(models.Model):
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=500)
