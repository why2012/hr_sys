from django.shortcuts import render, redirect
from django.http import HttpResponse
from hr_sys.decorators import checklogin
import json
from hr_sys.models import Department
from jinja2 import utils

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
    return HttpResponse(1);