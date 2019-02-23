# coding: utf-8
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import hashers
from hr_sys.models import User, UserGroup, UserGroupMenuItem, MenuItem
from django.conf import settings
from django.http import HttpResponse
from hr_sys.decorators import checklogin
import logging
import json
from jinja2 import utils
logger = logging.getLogger(__name__)

def login(request):
    context = {}
    if request.method == "GET":
        if request.GET.get("error_msg"):
            context["error_msg"] = utils.escape(request.GET["error_msg"])
        return render(request, 'login.html', context)
    elif request.method == "POST":
        username = utils.escape(request.POST.get("username"))
        password = utils.escape(request.POST.get("password"))
        hashed_password = hashers.make_password(password=password, salt=settings.SALT)
        queryset = User.objects.filter(name=username, password=hashed_password)
        if not queryset or len(queryset) == 0 or not queryset[0].user_group:
            context["error_msg"] = "用户名或密码错误"
            if len(queryset) != 0 and not queryset[0].user_group:
                context["error_msg"] = "此用户无任何权限，请先绑定用户组"
            return render(request, 'login.html', context)
        else:
            request.session["username"] = queryset[0].name
            request.session["userid"] = queryset[0].id
            return redirect("main_frame")

def logout(request):
    if "username" in request.session:
        del request.session["username"]
    if "userid" in request.session:
        del request.session["userid"]
    return redirect("login")

@checklogin()
def add_a_user(request):
    context = {}
    user_groups = UserGroup.objects.all()
    context['user_groups'] = user_groups
    return render(request, "add_a_user.html", context)

@checklogin()
def user_list_json(request):
    user_obj_list = User.objects.all()
    user_list = []
    for item in user_obj_list:
        user_list.append({"user_id": item.id, "user_name": item.name, "user_email": item.email,
                          "user_group_id": item.user_group_id, "user_group_name": item.user_group.name})
    return HttpResponse(json.dumps(user_list, ensure_ascii=False), content_type="application/json, charset=utf-8")

@checklogin()
def user_add(request):
    user_name = request.POST.get("user_name")
    user_password = request.POST.get("user_password")
    user_email = request.POST.get("user_email")
    user_group_id = request.POST.get("user_group_id")
    if not user_name or not user_password or not user_email or not user_group_id:
        return redirect("add_a_user")
    user_name = utils.escape(user_name)
    user_email = utils.escape(user_email)
    hashed_password = hashers.make_password(password=user_password, salt=settings.SALT)
    user_group_id = int(user_group_id)
    new_user = User(name=user_name, password=hashed_password, email=user_name, user_group_id=user_group_id)
    new_user.save()
    return redirect("add_a_user")

@checklogin()
def user_del(request):
    user_id = request.POST.get("user_id")
    if not user_id:
        return HttpResponse(0)
    user_id = int(user_id)
    User.objects.filter(id=user_id).delete()
    return HttpResponse(1)

@checklogin()
def user_edit(request):
    user_id = request.POST.get("user_id")
    user_name = request.POST.get("user_name")
    user_password = request.POST.get("user_password")
    user_email = request.POST.get("user_email")
    user_group_id = request.POST.get("user_group_id")
    if not user_name or not user_email or not user_group_id:
        return redirect("add_a_user")
    user_id = int(user_id)
    user_name = utils.escape(user_name)
    user_email = utils.escape(user_email)
    hashed_password = None
    if user_password:
        hashed_password = hashers.make_password(password=user_password, salt=settings.SALT)
    user_group_id = int(user_group_id)
    update_dict = {"name": user_name, "email": user_email, "user_group_id": user_group_id}
    if hashed_password:
        update_dict["password"] = hashed_password
    User.objects.filter(id=user_id).update(**update_dict)
    return redirect("add_a_user")

@checklogin()
def add_a_usergroup(request):
    context = {}
    return render(request, "add_a_usergroup.html", context)

@checklogin()
def usergroup_list_json(request):
    usergroup_obj_list = UserGroup.objects.all()
    usergroup_list = []
    for item in usergroup_obj_list:
        usergroup_list.append({"group_id": item.id, "group_name": item.name, "group_remark": item.remark})
    return HttpResponse(json.dumps(usergroup_list, ensure_ascii=False), content_type="application/json, charset=utf-8")

@checklogin()
def group_add(request):
    group_name = request.POST.get("group_name")
    group_remark = request.POST.get("group_remark")
    if not group_name:
        return redirect("add_a_usergroup")
    group_name = utils.escape(group_name)
    if group_remark:
        group_remark = utils.escape(group_remark)
    else:
        group_remark = ""
    new_usergroup = UserGroup(name=group_name, remark=group_remark)
    new_usergroup.save()
    return redirect("add_a_usergroup")

@checklogin()
def group_del(request):
    group_id = request.POST.get("group_id")
    if not group_id:
        return HttpResponse(0)
    group_id = int(group_id)
    UserGroup.objects.filter(id=group_id).delete()
    return HttpResponse(1)

@checklogin()
def group_edit(request):
    group_id = request.POST.get("group_id")
    group_name = request.POST.get("group_name")
    group_remark = request.POST.get("group_remark")
    if not group_id:
        return redirect("add_a_usergroup")
    group_id = int(group_id)
    update_dict = {}
    if group_name:
        group_name = utils.escape(group_name)
        update_dict["name"] = group_name
    if group_remark:
        group_remark = utils.escape(group_remark)
        update_dict["remark"] = group_remark
    UserGroup.objects.filter(id=group_id).update(**update_dict)
    return redirect("add_a_usergroup")

@checklogin()
def group_priv(request):
    context = {}
    menuItems = MenuItem.objects.order_by("id").all()
    groups = UserGroup.objects.order_by("id").all()
    context["menuItems"] = menuItems
    context["groups"] = groups

    return render(request, "group_priv.html", context)

@checklogin()
def group_priv_json(request):
    priv_objs = UserGroupMenuItem.objects.order_by("user_group_id", "id").all()
    priv_list = []
    for item in priv_objs:
        priv_list.append({"priv_id": item.id, "group_id": item.user_group.id, "group_name": item.user_group.name,
                          "menu_id": item.menu_item.id, "menu_name": item.menu_item.name})
    return HttpResponse(json.dumps(priv_list, ensure_ascii=False), content_type="application/json, charset=utf-8")

@checklogin()
def group_priv_add(request):
    user_group_id = request.POST.get("user_group_id")
    menu_item_id = request.POST.get("menu_item_id")
    if not user_group_id or not menu_item_id:
        return redirect("group_priv")
    user_group_id = int(user_group_id)
    menu_item_id = int(menu_item_id)
    new_relation = UserGroupMenuItem(user_group_id=user_group_id, menu_item_id=menu_item_id)
    new_relation.save()

    return redirect("group_priv")

@checklogin()
def group_priv_del(request):
    group_priv_id = request.POST.get("group_priv_id")
    if not group_priv_id:
        return HttpResponse(0)
    group_priv_id = int(group_priv_id)
    UserGroupMenuItem.objects.filter(id=group_priv_id).delete()

    return HttpResponse(1)

@checklogin()
def group_priv_edit(request):
    group_priv_id = request.POST.get("group_priv_id")
    menu_item_id = request.POST.get("menu_item_id")
    if not group_priv_id or not menu_item_id:
        return redirect("group_priv")
    group_priv_id = int(group_priv_id)
    menu_item_id = int(menu_item_id)
    UserGroupMenuItem.objects.filter(id=group_priv_id).update(menu_item_id=menu_item_id)
    return redirect("group_priv")

@checklogin()
def group_priv_tree_json(request):
    priv_objs = MenuItem.objects.all()
    priv_dict = {}  # parent_id -> children
    id_parentid_dict = {}  # id -> parent_id
    parentid_list = []
    for item in priv_objs:
        if item.parent_id not in priv_dict:
            priv_dict[item.parent_id] = []
            parentid_list.append(item.parent_id)
        priv_dict[item.parent_id].append({"id": item.id, "text": "[" + str(item.id) + "]" + item.name})
        id_parentid_dict[item.id] = item.parent_id
    parentid_list.sort(reverse=True)
    for parentid in parentid_list:
        if parentid == -1:
            break
        nodes = priv_dict[parentid]
        if parentid in id_parentid_dict:
            grandparent_id = id_parentid_dict[parentid]
            for parentnode in priv_dict[grandparent_id]:
                if parentnode["id"] == parentid:
                    parentnode["children"] = nodes
    departments_tree = priv_dict[-1]

    return HttpResponse(json.dumps(departments_tree, ensure_ascii=False), content_type="application/json, charset=utf-8")
