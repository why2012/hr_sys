# coding: utf-8
from functools import wraps
from django.shortcuts import redirect

def checklogin():
    def method_process(view_func):
        @wraps(view_func)
        def check(request, *args, **kwargs):
            if request.session.get("username") is not None and request.session.get("userid") is not None:
                return view_func(request, *args, **kwargs)
            else:
                return redirect("login/?error_msg=请先登录")
        return check
    return method_process

