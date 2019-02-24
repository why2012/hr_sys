# coding : utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.db import IntegrityError, transaction
from django.urls import reverse
from hr_sys.decorators import checklogin
import json
from hr_sys.models import Department, EmployeeLevel, Employee, EmployeePosition, EmployPromoteHistory, EmployeeAttendance
from django.db.models import Count
from jinja2 import utils
from hr_sys.libs.sql_helper import namedtuplefetchall
import logging
from urllib.parse import urlencode, quote
import time
import datetime
import codecs
import uuid
import os
logger = logging.getLogger(__name__)

@checklogin()
def overview(request):
    context = {}
    return render(request, "overview.html", context)

@checklogin()
def overview_list_json(request):
    overview_list = []
    employee_amount = Employee.objects.exclude(status=1).count()
    employee_male_amount = Employee.objects.exclude(status=1).filter(gender=0).count()
    employee_female_amount = Employee.objects.exclude(status=1).filter(gender=1).count()
    department_amount = Department.objects.count()
    manager_amount = Employee.objects.exclude(manager_id=-1, status=1).values("manager_id").distinct().count()

    overview_list.append({"employee_amount": employee_amount, "employee_male_amount": employee_male_amount,
                          "employee_female_amount": employee_female_amount, "department_amount": department_amount,
                          "manager_amount": manager_amount})

    return HttpResponse(json.dumps(overview_list, ensure_ascii=False), content_type="application/json, charset=utf-8")

@checklogin()
def employee_amount_by_department(request):
    amount_by_department = {"legend": [], "data": []}
    department_names = Department.objects.all().values("id", "name")
    department_id_name = {}
    for id_name in department_names:
        department_id_name[id_name["id"]] = id_name["name"]
        amount_by_department["legend"].append(id_name["name"])
    amount_by_department_objs = Employee.objects.exclude(status=1).values("department_id").annotate(amount=Count("id"))
    for item in amount_by_department_objs:
        if item["department_id"] in department_id_name:
            amount_by_department["data"].append({"name": department_id_name[item["department_id"]], "value": item["amount"]})
    return HttpResponse(json.dumps(amount_by_department, ensure_ascii=False), content_type="application/json, charset=utf-8")

@checklogin()
def employee_gender_by_department(request):
    amount_by_department = {"legend": [], "data1": [], "data2": []}
    department_names = Department.objects.all().values("id", "name")
    department_id_name = {}
    for id_name in department_names:
        department_id_name[id_name["id"]] = id_name["name"]
        amount_by_department["legend"].append(id_name["name"])
    male_amount_by_department_objs = Employee.objects.exclude(status=1).filter(gender=0).values("department_id").annotate(amount=Count("id"))
    female_amount_by_department_objs = Employee.objects.exclude(status=1).filter(gender=1).values("department_id").annotate(amount=Count("id"))
    for item in male_amount_by_department_objs:
        if item["department_id"] in department_id_name:
            amount_by_department["data1"].append(
                {"name": department_id_name[item["department_id"]], "value": item["amount"]})
    for item in female_amount_by_department_objs:
        if item["department_id"] in department_id_name:
            amount_by_department["data2"].append(
                {"name": department_id_name[item["department_id"]], "value": item["amount"]})
    return HttpResponse(json.dumps(amount_by_department, ensure_ascii=False),
                        content_type="application/json, charset=utf-8")

@checklogin()
def employee_promote_log(request):
    promotion_list = {"xAxis": [], "data": []}
    today = datetime.date.today()
    first_day = today.replace(day=1)
    last_month = first_day - datetime.timedelta(days=1)
    last_month_today = last_month.replace(day=today.day)
    promote_objs = EmployPromoteHistory.objects.filter(log_time__gte=last_month_today, type=0).\
            extra(select={'log_time_day': 'date( log_time )'}).values('log_time_day').annotate(amount=Count("id")).order_by("log_time_day").all()
    curr_datetime = last_month_today
    item_index = 0
    while curr_datetime != today:
        datestr = curr_datetime.strftime("%Y-%m-%d")
        promotion_list["xAxis"].append(datestr)
        if item_index < len(promote_objs):
            item = promote_objs[item_index]
        else:
            item = None
        if item and item["log_time_day"] == curr_datetime:
            promotion_list["data"].append({"name": datestr, "value": item["amount"]})
            item_index += 1
        else:
            promotion_list["data"].append({"name": datestr, "value": 0})
        curr_datetime = curr_datetime + datetime.timedelta(days=1)
    return HttpResponse(json.dumps(promotion_list, ensure_ascii=False), content_type="application/json, charset=utf-8")

@checklogin()
def employee_attendance_log(request):
    attendance_list = {"xAxis": [], "data1": [], "data2": []}
    today = datetime.date.today()
    first_day = today.replace(day=1)
    last_month = first_day - datetime.timedelta(days=1)
    last_month_today = last_month.replace(day=today.day)
    attendance_objs = EmployeeAttendance.objects.filter(check_time__gte=last_month_today, type=0).\
        extra(select={'check_time_day': 'date( check_time )'}).values("check_time_day").annotate(amount=Count("id")).order_by("check_time_day").all()
    late_attendance_objs = EmployeeAttendance.objects.filter(check_time__gte=last_month_today, type=1). \
        extra(select={'check_time_day': 'date( check_time )'}).values("check_time_day").annotate(amount=Count("id")).order_by("check_time_day").all()
    curr_datetime = last_month_today
    attendance_item_index = 0
    late_item_index = 0
    while curr_datetime != today:
        datestr = curr_datetime.strftime("%Y-%m-%d")
        attendance_list["xAxis"].append(datestr)
        if attendance_item_index < len(attendance_objs):
            item = attendance_objs[attendance_item_index]
        else:
            item = None
        if item and item["check_time_day"] == curr_datetime:
            attendance_list["data1"].append({"name": datestr, "value": item["amount"]})
            attendance_item_index += 1
        else:
            attendance_list["data1"].append({"name": datestr, "value": 0})

        if late_item_index < len(late_attendance_objs):
            item = late_attendance_objs[late_item_index]
        else:
            item = None
        if item and item["check_time_day"] == curr_datetime:
            attendance_list["data2"].append({"name": datestr, "value": item["amount"]})
            late_item_index += 1
        else:
            attendance_list["data2"].append({"name": datestr, "value": 0})
        curr_datetime = curr_datetime + datetime.timedelta(days=1)
    return HttpResponse(json.dumps(attendance_list, ensure_ascii=False), content_type="application/json, charset=utf-8")