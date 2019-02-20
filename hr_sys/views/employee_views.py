# coding : utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from hr_sys.decorators import checklogin
import json
from hr_sys.models import Department, EmployeeLevel, Employee, EmployeePosition
from jinja2 import utils
from hr_sys.libs.sql_helper import namedtuplefetchall
import logging
from urllib.parse import urlencode
logger = logging.getLogger(__name__)

@checklogin()
def employee_list(request):
    context = {}
    departments = Department.objects.all()
    levels = EmployeeLevel.objects.all()
    positions = EmployeePosition.objects.all()
    context["departments"] = departments
    context["levels"] = levels
    context["positions"] = positions
    context["grid_url"] = "employee_list_json"
    if request.method == "POST":
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        manager_id = request.POST.get("manager_id")
        manager_name = request.POST.get("manager_name")
        department = request.POST.get("department")
        province_name = request.POST.get("province_name")
        city_name = request.POST.get("city_name")
        level = request.POST.get("level")
        position = request.POST.get("position")
        status = request.POST.get("status")
        valid_params = {}
        if name:
            valid_params["search_name"] = name
        if gender != "ALL":
            valid_params["search_gender"] = gender
        if email:
            valid_params["search_email"] = email
        if phone:
            valid_params["search_phone"] = phone
        if manager_id:
            valid_params["search_manager_id"] = manager_id
        if manager_name:
            valid_params["manager_name"] = manager_name
        if department != "ALL":
            valid_params["search_department"] = department
        if province_name:
            valid_params["search_province_name"] = province_name
        if city_name:
            valid_params["search_city_name"] = city_name
        if level != "ALL":
            valid_params["search_level"] = level
        if position != "ALL":
            valid_params["search_position"] = position
        if status != "ALL":
            valid_params["search_status"] = status
        grid_url = "employee_list_json"
        if valid_params:
            grid_url += "?" + urlencode(valid_params)
        context["grid_url"] = grid_url

    return render(request, 'employee_list.html', context)

@checklogin()
def employee_list_json(request):
    page = request.GET.get("page")
    rows = request.GET.get("rows")
    manager_name = request.GET.get("manager_name")
    manager_id = request.GET.get("search_manager_id")
    where_args = []
    where_sql = " where "
    search_keywords = {"name": "emp.name", "gender": "emp.gender", "email": "emp.email", "phone": "emp.phone",
                       "manager_id": "emp.manager_id", "department": "emp.department_id", "province_name": "emp.province_name",
                       "city_name": "emp.city_name", "level": "emp.level_id", "position": "emp.position_id", "status": "emp.status"}

    if manager_name and not manager_id:
        manager_objs = Employee.objects.filter(name=manager_name).all()
        if len(manager_objs) > 0:
            search_manager_ids = []
            for manager_obj in manager_objs:
                search_manager_ids.append(str(manager_obj.id))
            search_manager_ids_str = ",".join(search_manager_ids)
            where_sql += " %s in ( " % search_keywords["manager_id"]
            where_sql += search_manager_ids_str
            where_sql += " ) and "

    for k, v in request.GET.items():
        if k.startswith("search"):
            k = k.split("_", 1)[-1]
            if k in search_keywords:
                where_args.append(v)
                where_sql += " %s=%s and " % (search_keywords[k], "%s")

    if where_sql.endswith("and "):
        where_sql = where_sql[0: -4]

    if not page or not rows:
        return redirect("employee_list")
    page = int(page)
    rows = int(rows)
    emp_tablename = Employee._meta.db_table
    dep_tablename = Department._meta.db_table
    lev_tablename = EmployeeLevel._meta.db_table
    pos_tablename = EmployeePosition._meta.db_table
    # l = logging.getLogger('django.db.backends')
    # l.setLevel(logging.DEBUG)
    # l.addHandler(logging.StreamHandler())
    with connection.cursor() as cursor:
        if where_sql == " where ":
            cursor.execute(
                """
                    select 
                      emp.id as employee_id, emp.name as employee_name, emp.gender as employee_gender, pos.name as employee_position,
                      emp2.id as manager_id, emp2.name as manager_name, dep.id as department_id, dep.name as department_name, 
                      emp.province_name, emp.city_name, emp.salary, lev.name as employee_level, emp.status as employee_status, 
                      emp.email as employee_email, emp.phone as employee_phone, lev.id as employee_level_id, pos.id as employee_position_id
                    from  
                      %s as emp left join %s as emp2 on emp.manager_id=emp2.id 
                      inner join %s as dep on emp.department_id=dep.id 
                      inner join %s as lev on emp.level_id=lev.id 
                      inner join %s as pos on emp.position_id=pos.id 
                     order by emp.id asc limit %s, %s
                """ % (emp_tablename, emp_tablename, dep_tablename, lev_tablename, pos_tablename, "%s", "%s"), [(page - 1) * rows, rows])
        else:
            sql_args = []
            sql_args.extend(where_args)
            sql_args.extend([(page - 1) * rows, rows])
            cursor.execute(
                """
                    select 
                      emp.id as employee_id, emp.name as employee_name, emp.gender as employee_gender, pos.name as employee_position,
                      emp2.id as manager_id, emp2.name as manager_name, dep.id as department_id, dep.name as department_name, 
                      emp.province_name, emp.city_name, emp.salary, lev.name as employee_level, emp.status as employee_status, 
                      emp.email as employee_email, emp.phone as employee_phone, lev.id as employee_level_id, pos.id as employee_position_id
                    from  
                      """ + emp_tablename + """ as emp left join """ + emp_tablename + """ as emp2 on emp.manager_id=emp2.id 
                      inner join """ + dep_tablename + """ as dep on emp.department_id=dep.id 
                      inner join """ + lev_tablename + """ as lev on emp.level_id=lev.id 
                      inner join """ + pos_tablename + """ as pos on emp.position_id=pos.id
                """
                + where_sql +
                """
                     order by emp.id asc limit %s, %s 
                """, sql_args)
        employee_obj_list = namedtuplefetchall(cursor)
        if where_sql == " where ":
            cursor.execute("select count(*) as total from %s" % (emp_tablename))
        else:
            cursor.execute("select count(*) as total from " + emp_tablename + " as emp " + where_sql, where_args)
        employee_total = namedtuplefetchall(cursor)
    employee_list = {"total": employee_total[0].total, "rows": []}
    for item in employee_obj_list:
        manager_id = item.manager_id
        manager_name = item.manager_name
        employee_gender = item.employee_gender
        employee_status = item.employee_status
        if manager_id is None:
            manager_id = "-"
        if manager_name is None:
            manager_name = "-"
        if employee_gender == "0":
            employee_gender = "男"
        else:
            employee_gender = "女"
        if employee_status == 0:
            employee_status = "在职"
        else:
            employee_status = "离职"
        employee_list["rows"].append({
            "employee_id": item.employee_id, "employee_name": item.employee_name, "employee_gender": employee_gender,
            "employee_position": item.employee_position, "manager_id": manager_id, "manager_name": manager_name,
            "employee_position_id": item.employee_position_id, "employee_level_id": item.employee_level_id,
            "department_id": item.department_id, "department_name": item.department_name, "province_name": item.province_name,
            "city_name": item.city_name, "salary": item.salary, "employee_level": item.employee_level,
            "employee_status": employee_status, "employee_email": item.employee_email, "employee_phone": item.employee_phone
        })
    return HttpResponse(json.dumps(employee_list, ensure_ascii=False), content_type="application/json, charset=utf-8")

@checklogin()
def employee_add(request):
    employee_name = request.POST.get("name")
    employee_gender = request.POST.get("gender")
    employee_email = request.POST.get("email")
    employee_phone = request.POST.get("phone")
    employee_manager_id = request.POST.get("manager_id")
    employee_department_id = request.POST.get("department")
    province_name = request.POST.get("province_name")
    city_name = request.POST.get("city_name")
    employee_salary = request.POST.get("salary")
    employee_level_id = request.POST.get("level")
    employee_position_id = request.POST.get("position")
    employee_status = request.POST.get("status")
    not_null = [employee_name, employee_gender, employee_manager_id, employee_department_id, province_name, city_name,
                employee_salary, employee_level_id, employee_position_id, employee_status]
    for item in not_null:
        if item is None:
            return redirect("employee_list")
    employee_name = utils.escape(employee_name)
    employee_gender = utils.escape(employee_gender)
    if employee_email is not None:
        employee_email = utils.escape(employee_email)
    if employee_phone is not None:
        employee_phone = utils.escape(employee_phone)
    employee_manager_id = int(employee_manager_id)
    province_name = utils.escape(province_name)
    city_name = utils.escape(city_name)
    employee_salary = int(employee_salary)
    employee_level_id = int(employee_level_id)
    employee_position_id = int(employee_position_id)
    employee_status = int(employee_status)

    if employee_manager_id == -1:
        department = Department.objects.get(pk=employee_department_id)
        if department and department.manager:
            direct_manager_id = department.manager.id
            employee_manager_id = direct_manager_id

    new_employee = Employee(name=employee_name, gender=employee_gender, email=employee_email, phone=employee_phone,
                            manager_id=employee_manager_id, department_id=employee_department_id,
                            province_name=province_name, city_name=city_name, salary=employee_salary,
                            level_id=employee_level_id, position_id=employee_position_id, status=employee_status)
    new_employee.save()
    return redirect("employee_list")

@checklogin()
def employee_edit(request):
    employee_id = request.POST.get("employee_id")
    employee_name = request.POST.get("name")
    employee_gender = request.POST.get("gender")
    employee_email = request.POST.get("email")
    employee_phone = request.POST.get("phone")
    employee_manager_id = request.POST.get("manager_id")
    employee_department_id = request.POST.get("department")
    province_name = request.POST.get("province_name")
    city_name = request.POST.get("city_name")
    employee_salary = request.POST.get("salary")
    employee_level_id = request.POST.get("level")
    employee_position_id = request.POST.get("position")
    employee_status = request.POST.get("status")
    not_null = [employee_id, employee_name, employee_gender, employee_manager_id, employee_department_id, province_name,
                city_name, employee_salary, employee_level_id, employee_position_id, employee_status]
    for item in not_null:
        if item is None:
            return redirect("employee_list")
    employee_name = utils.escape(employee_name)
    employee_gender = utils.escape(employee_gender)
    if employee_email is not None:
        employee_email = utils.escape(employee_email)
    if employee_phone is not None:
        employee_phone = utils.escape(employee_phone)
    employee_manager_id = int(employee_manager_id)
    province_name = utils.escape(province_name)
    city_name = utils.escape(city_name)
    employee_salary = int(employee_salary)
    employee_level_id = int(employee_level_id)
    employee_position_id = int(employee_position_id)
    employee_status = int(employee_status)
    Employee.objects.filter(id=employee_id).update(
                            name=employee_name, gender=employee_gender, email=employee_email, phone=employee_phone,
                            manager_id=employee_manager_id, department_id=employee_department_id,
                            province_name=province_name, city_name=city_name, salary=employee_salary,
                            level_id=employee_level_id, position_id=employee_position_id, status=employee_status)
    return redirect("employee_list")

@checklogin()
def employee_del(request):
    employee_id = request.POST.get("employee_id")
    if not employee_id:
        return HttpResponse(0)
    employee_id = int(employee_id)
    Employee.objects.filter(id=employee_id).delete()
    return HttpResponse(1)

