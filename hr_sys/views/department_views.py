# coding : utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from hr_sys.decorators import checklogin
import json
from hr_sys.models import Department, EmployeeLevel, EmployeePosition
from jinja2 import utils
from hr_sys.libs.sql_helper import namedtuplefetchall

@checklogin()
def department_list(request):
    context = {}
    return render(request, 'department_list.html', context)

@checklogin()
# 构建树时从底往上合并
def department_tree_json(request):
    departments = Department.objects.all()
    departments_dict = {} # parent_id -> children
    id_parentid_dict = {} # id -> parent_id
    parentid_list = []
    for item in departments:
        if item.parent_id not in departments_dict:
            departments_dict[item.parent_id] = []
            parentid_list.append(item.parent_id)
        departments_dict[item.parent_id].append({"id": item.id, "text": "[" + str(item.id) + "]" + item.name})
        id_parentid_dict[item.id] = item.parent_id
    parentid_list.sort(reverse=True)
    for parentid in parentid_list:
        if parentid == -1:
            break
        nodes = departments_dict[parentid]
        if parentid in id_parentid_dict:
            grandparent_id = id_parentid_dict[parentid]
            for parentnode in departments_dict[grandparent_id]:
                if parentnode["id"] == parentid:
                    parentnode["children"] = nodes
    departments_tree = departments_dict[-1]

    return HttpResponse(json.dumps(departments_tree, ensure_ascii = False), content_type="application/json, charset=utf-8")

@checklogin()
def add_department(request):
    department_name = request.POST.get("department_name")
    parent_id = request.POST.get("parent_id")
    if not department_name or not parent_id:
        return redirect("department_list")
    department_name = utils.escape(department_name)
    parent_id = int(parent_id)
    new_department = Department(name=department_name, parent_id=parent_id)
    new_department.save()
    return redirect("department_list")

@checklogin()
def edit_remove_department(request):
    new_name = request.POST.get("new_name").split("]")[-1];
    department_id = request.POST.get("department_id");
    if not new_name or not department_id:
        return HttpResponse(0);
    new_name = utils.escape(new_name)
    department_id = int(department_id)
    if new_name == "--DELETE--":
        #delete department
        new_department = Department(name=new_name, id=department_id)
        new_department.delete()
    else:
        # update
        Department.objects.filter(id=department_id).update(name=new_name)
    return HttpResponse(1)

@checklogin()
def department_level(request):
    context = {}
    return render(request, 'department_level.html', context)

@checklogin()
def employee_level_json(request):
    tablename = EmployeeLevel._meta.db_table
    with connection.cursor() as cursor:
        cursor.execute("select a.id, a.order, a.name, b.id as next_level_id, b.order as next_level_order, b.name as next_level_name from "
                       + tablename + " as a left join " + tablename + " as b on a.next_level_id=b.id")
        levels = namedtuplefetchall(cursor)
    json_levels = {"total": len(levels), "rows": []}
    for item in levels:
        next_level_id = item.next_level_id
        next_level_order =item.next_level_order
        next_level_name = item.next_level_name
        if next_level_id is None:
            next_level_id = "-"
        if next_level_order is None:
            next_level_order = "-"
        if next_level_name is None:
            next_level_name = "-"
        json_levels["rows"].append({"level_id": item.id, "level_order": item.order, "level_name": item.name,
                                    "next_level_id": next_level_id, "next_level_order": next_level_order, "next_level_name": next_level_name})
    return HttpResponse(json.dumps(json_levels, ensure_ascii = False), content_type="application/json, charset=utf-8")

@checklogin()
def employee_level_add(request):
    employee_level_name = request.POST.get("employee_level_name")
    level_order = request.POST.get("level_order")
    next_level_id = request.POST.get("next_level_id")
    if not employee_level_name or not level_order or not next_level_id:
        return redirect("employee_level")
    employee_level_name = utils.escape(employee_level_name)
    level_order = int(level_order)
    next_level_id = int(next_level_id)
    new_employee_level = EmployeeLevel(name=employee_level_name, order=level_order, next_level_id=next_level_id)
    new_employee_level.save()
    return redirect("employee_level")

@checklogin()
def employee_level_edit(request):
    employee_level_id = request.POST.get("employee_level_id")
    employee_level_name = request.POST.get("employee_level_name")
    level_order = request.POST.get("level_order")
    next_level_id = request.POST.get("next_level_id")
    if not employee_level_id or  not employee_level_name or not level_order or not next_level_id:
        return redirect("employee_level")
    employee_level_id = int(employee_level_id)
    employee_level_name = utils.escape(employee_level_name)
    level_order = int(level_order)
    next_level_id = int(next_level_id)
    EmployeeLevel.objects.filter(id=employee_level_id).update(name=employee_level_name, order=level_order, next_level_id=next_level_id)
    return redirect("employee_level")

@checklogin()
def employee_level_del(request):
    employee_level_id = request.POST.get("employee_level_id")
    if not employee_level_id:
        return HttpResponse(0)
    employee_level_id = int(employee_level_id)
    EmployeeLevel.objects.filter(id=employee_level_id).delete()
    EmployeeLevel.objects.filter(next_level_id=employee_level_id).update(next_level_id=-1)
    return HttpResponse(1)

@checklogin()
def position_list(request):
    context = {}
    return render(request, 'position_list.html', context)

@checklogin()
def position_json(request):
    positions = EmployeePosition.objects.all()
    json_positions = {"total": len(positions), "rows": []}
    for item in positions:
        json_positions["rows"].append({"id": item.id, "name": item.name})
    return HttpResponse(json.dumps(json_positions, ensure_ascii = False), content_type="application/json, charset=utf-8")

@checklogin()
def position_add(request):
    position_name = request.POST.get("position_name")
    if not position_name:
        return redirect("position_list")
    position_name = utils.escape(position_name)
    new_position = EmployeePosition(name=position_name)
    new_position.save()
    return redirect("position_list")

@checklogin()
def position_edit(request):
    position_id = request.POST.get("position_id")
    position_name = request.POST.get("position_name")
    if not position_id or not position_name:
        return redirect("position_list")
    position_id = int(position_id)
    position_name = utils.escape(position_name)
    EmployeePosition.objects.filter(id=position_id).update(name=position_name)
    return redirect("position_list")

@checklogin()
def position_del(request):
    position_id = request.POST.get("position_id")
    if not position_id:
        return HttpResponse(0)
    position_id = int(position_id)
    EmployeePosition.objects.filter(id=position_id).delete()
    return HttpResponse(1)

@checklogin()
def department_manager(request):
    context = {}
    return render(request, 'department_manager.html', context)

@checklogin()
def department_json(request):
    departments = Department.objects.all()
    json_positions = {"total": len(departments), "rows": []}
    for item in departments:
        if item.manager:
            json_positions["rows"].append({"id": item.id, "name": item.name, "manager_id": item.manager.id, "manager_name": item.manager.name})
        else:
            json_positions["rows"].append({"id": item.id, "name": item.name, "manager_id": "-", "manager_name": "-"})

    return HttpResponse(json.dumps(json_positions, ensure_ascii = False), content_type="application/json, charset=utf-8")

@checklogin()
def department_manager_edit(request):
    manager_id = request.POST.get("manager_id")
    department_id = request.POST.get("department_id")
    if not manager_id or not department_id:
        return redirect("department_manager")
    manager_id = int(manager_id)
    department_id = int(department_id)
    Department.objects.filter(id=department_id).update(manager_id=manager_id)
    return redirect("department_manager")
