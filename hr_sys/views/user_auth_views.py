# coding: utf-8
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import hashers
from hr_sys.models import User
from django.conf import settings
import logging
logger = logging.getLogger(__name__)

def login(request):
    context = {}
    if request.method == "GET":
        if request.GET.get("error_msg"):
            context["error_msg"] = request.GET["error_msg"]
        return render(request, 'login.html', context)
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        hashed_password = hashers.make_password(password=password, salt=settings.SALT)
        queryset = User.objects.filter(name=username, password=hashed_password)
        if not queryset or len(queryset) == 0:
            context["error_msg"] = "用户名或密码错误"
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

