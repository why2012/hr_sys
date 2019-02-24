# coding : utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.db import IntegrityError, transaction
from django.urls import reverse
from hr_sys.decorators import checklogin
import json
from hr_sys.models import Department, EmployeeLevel, Employee, EmployeePosition, EmployPromoteHistory, EmployeeAttendance
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
def employee_list(request, template_name = "employee_list.html"):
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

    return render(request, template_name, context)

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
                      emp.email as employee_email, emp.phone as employee_phone, lev.id as employee_level_id, pos.id as employee_position_id,
                      emp.induction_date as induction_datetime
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
                      emp.email as employee_email, emp.phone as employee_phone, lev.id as employee_level_id, pos.id as employee_position_id,
                      emp.induction_date as induction_datetime
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
        induction_datetime = str(item.induction_datetime)
        if induction_datetime == "None":
            induction_datetime = "-"
        employee_list["rows"].append({
            "employee_id": item.employee_id, "employee_name": item.employee_name, "employee_gender": employee_gender,
            "employee_position": item.employee_position, "manager_id": manager_id, "manager_name": manager_name,
            "employee_position_id": item.employee_position_id, "employee_level_id": item.employee_level_id,
            "department_id": item.department_id, "department_name": item.department_name, "province_name": item.province_name,
            "city_name": item.city_name, "salary": item.salary, "employee_level": item.employee_level,
            "employee_status": employee_status, "employee_email": item.employee_email, "employee_phone": item.employee_phone,
            "induction_datetime": induction_datetime
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
    induction_datetime = request.POST.get("induction_datetime")
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
    induction_datetime = utils.escape(induction_datetime)
    induction_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(induction_datetime, "%m/%d/%Y %H:%M:%S"))

    if employee_manager_id == -1:
        department = Department.objects.get(pk=employee_department_id)
        if department and department.manager:
            direct_manager_id = department.manager.id
            employee_manager_id = direct_manager_id

    new_employee = Employee(name=employee_name, gender=employee_gender, email=employee_email, phone=employee_phone,
                            manager_id=employee_manager_id, department_id=employee_department_id,
                            province_name=province_name, city_name=city_name, salary=employee_salary,
                            level_id=employee_level_id, position_id=employee_position_id, status=employee_status,
                            induction_date=induction_datetime)
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
    induction_datetime = request.POST.get("induction_datetime")
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
    induction_datetime = utils.escape(induction_datetime)
    induction_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(induction_datetime, "%m/%d/%Y %H:%M:%S"))

    Employee.objects.filter(id=employee_id).update(
                            name=employee_name, gender=employee_gender, email=employee_email, phone=employee_phone,
                            manager_id=employee_manager_id, department_id=employee_department_id,
                            province_name=province_name, city_name=city_name, salary=employee_salary,
                            level_id=employee_level_id, position_id=employee_position_id, status=employee_status,
                            induction_date=induction_datetime)
    return redirect("employee_list")

@checklogin()
def employee_del(request):
    employee_id = request.POST.get("employee_id")
    if not employee_id:
        return HttpResponse(0)
    employee_id = int(employee_id)
    Employee.objects.filter(id=employee_id).delete()
    return HttpResponse(1)

@checklogin()
def employee_promote_list(request):
    return employee_list(request, 'employee_promote.html')

@checklogin()
def employee_promote(request):
    employee_id = request.POST.get("employee_id")
    to_level_id = request.POST.get("to_level_id")
    if not employee_id or not to_level_id:
        return redirect("employee_promote_list")
    employee_id = int(employee_id)
    to_level_id = int(to_level_id)
    from_level_id = -1
    try:
        employee = Employee.objects.get(pk=employee_id)
        to_level = EmployeeLevel.objects.get(pk=to_level_id)
        if employee and to_level:
            from_level_id = employee.level_id
            if to_level.order - employee.level.order > 0:
                type = 0
            elif to_level.order - employee.level.order < 0:
                type = 2
            else:
                type = -1
            if type != -1:
                with transaction.atomic():
                    new_promote_history = EmployPromoteHistory(type=type, employee_id=employee.id, from_level_id=employee.level_id, to_level_id=to_level_id)
                    new_promote_history.save()
                    employee.level_id = to_level_id
                    employee.save()
    except IntegrityError:
        logger.error("Failed to promote employee: %s from level: %s to level: %s" % (employee_id, from_level_id, to_level_id))
        return redirect("employee_promote_list")

    return redirect("employee_promote_list")

@checklogin()
def employee_attandance(request):
    def check_file(file_h):
        try:
            standard_time_line = file_h.readline()
            if len(standard_time_line.split(",")) != 2 or len(standard_time_line.split(",")[1].split(":")) != 2:
                raise Exception("基准时间行格式错误")
            heading_line = file_h.readline()
            if len(heading_line.split(",")) != 6:
                raise Exception("表头格式错误")
            data_line = file_h.readline()
            if not data_line:
                raise EOFError()
            line_no = 3
            while data_line:
                data_line = data_line.strip()
                data_item = data_line.split(",")
                if len(data_item) != 6:
                    raise Exception("数据行%s格式错误" % line_no)
                try:
                    time.strptime(data_item[5].strip(), "%Y-%m-%d %H:%M:%S")
                except Exception as e:
                    raise Exception("数据行%s日期格式错误: %s" % (line_no, data_item[5]))
                data_line = file_h.readline()
                line_no += 1
        except EOFError:
            return "数据缺失"
        except Exception as e:
            return str(e)
        return ""
    context = {}
    error_msg = request.GET.get("error_msg")
    ok_msg = request.GET.get("ok_msg")
    filename = ""
    if request.method == 'POST':
        file_handler = request.FILES.get('upload_file')
        if file_handler:
            filename = Employee._meta.app_label + '/files/attandance-%s.csv' % uuid.uuid1()
            with open(filename, 'wb') as destination:
                for chunk in file_handler.chunks():
                    destination.write(chunk)
            with open(filename, 'r', encoding='UTF-8') as f:
                error_msg = check_file(f)
            if error_msg:
                os.remove(filename)
        else:
            error_msg = "提交文件不能为空"
    if error_msg:
        context["error_msg"] = utils.escape(error_msg)
    if ok_msg:
        context["ok_msg"] = utils.escape(ok_msg)
    if filename and not error_msg:
        context["grid_url"] = reverse("employee_attandance_save_viewlist_json") + "?filepath=" + filename
        context["save_btn_redirect"] = reverse("employee_attandance_save") + "?filepath=" + filename
    else:
        context["grid_url"] = reverse("employee_attandance_save_viewlist_json")
        context["save_btn_redirect"] = "not-allowed"
    return render(request, "employee_attandance.html", context)

@checklogin()
def employee_attandance_template_download(request):
    def make_template():
        all_employees = Employee.objects.filter(status=0).all()
        template_lines = ["考勤基准时间(请根据需要更改):, 10:00", "员工ID, 姓名, 性别, 部门, 是否迟到(是/否), 签到时间(年-月-日 小时:分:秒)"]
        for item in all_employees:
            gender = '男'
            if item.gender == 1:
                gender = '女'
            template_lines.append("{id}, {name}, {gender}, {depart}, {is_late}, {check_time}".format(
                id=item.id, name=item.name, gender=gender, depart=item.department.name, is_late="否", check_time="xxxx-xx-xx xx:xx:xx"
            ))
        return "\n".join(template_lines)

    response = HttpResponse(content_type='text/csv')
    response.write(codecs.BOM_UTF8)
    response.write(make_template())
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="attandance_template.csv"'
    return response

@checklogin()
def employee_attandance_save_viewlist_json(request):
    attandance_data_filepath = request.GET.get("filepath")
    attandance_list = {"total": 0, "rows": []}
    if not attandance_data_filepath:
        attandance_list["total"] = 1
        attandance_list["rows"].append({"employee_id": "-", "employee_name": "-", "employee_gender": "-", "employee_position": "-",
                                        "is_late": "-", "checktime": "-", "standardtime": "-"})
    else:
        if attandance_data_filepath.startswith(Employee._meta.app_label + "/files/") and attandance_data_filepath.endswith(".csv"):
            try:
                with open(attandance_data_filepath, encoding='UTF-8') as file_h:
                    standard_time_line = file_h.readline()
                    heading_line = file_h.readline()
                    data_line = file_h.readline()

                    standard_time = utils.escape(standard_time_line.split(",")[1])
                    attandance_list["total"] = 0
                    while data_line:
                        attandance_list["total"] += 1
                        data_line = data_line.strip()
                        attandance_item = data_line.split(",")
                        attandance_list["rows"].append(
                            {"employee_id": int(attandance_item[0]), "employee_name": utils.escape(attandance_item[1]),
                             "employee_gender": utils.escape(attandance_item[2]), "employee_position": utils.escape(attandance_item[3]),
                             "is_late": utils.escape(attandance_item[4]), "checktime": attandance_item[5], "standardtime": utils.escape(standard_time)})
                        data_line = file_h.readline()
            except Exception as e:
                logger.error(e)
                attandance_list["rows"].append(
                    {"employee_id": "-", "employee_name": "文件处理出错", "employee_gender": "-", "employee_position": "-",
                     "is_late": "-", "checktime": "-", "standardtime": "-"})
    return HttpResponse(json.dumps(attandance_list, ensure_ascii=False), content_type="application/json, charset=utf-8")

@checklogin()
def employee_attandance_save(request):
    attandance_data_filepath = request.GET.get("filepath")
    msgs = {}
    attandance_list = []
    if attandance_data_filepath:
        if attandance_data_filepath.startswith(Employee._meta.app_label + "/files/") and attandance_data_filepath.endswith(".csv"):
            try:
                with open(attandance_data_filepath, encoding='UTF-8') as file_h:
                    standard_time_line = file_h.readline()
                    heading_line = file_h.readline()
                    data_line = file_h.readline()

                    standard_time = utils.escape(standard_time_line.split(",")[1])
                    while data_line:
                        data_line = data_line.strip()
                        attandance_item = data_line.split(",")
                        late_type = 0
                        if attandance_item[4] == "是":
                            late_type = 1
                        attandance_list.append(EmployeeAttendance(**{"employee_id": int(attandance_item[0]), "type": late_type,
                             "check_time": attandance_item[5].strip(), "standard_time": standard_time}))
                        data_line = file_h.readline()
                    EmployeeAttendance.objects.bulk_create(attandance_list)
                    msgs["ok_msg"] = "保存成功"
            except Exception as e:
                logger.error(e)
                msgs["error_msg"] = "保存失败, 请重新提交"
            if os.path.isfile(attandance_data_filepath):
                os.remove(attandance_data_filepath)
    return redirect("employee_attandance/?" + urlencode(msgs))

@checklogin()
def employee_person_stat(request):
    return employee_list(request, 'employee_person_stat.html')

@checklogin()
def employee_attendance_list_json(request):
    employee_id = request.POST.get("employee_id")
    attandance_list = []
    if not employee_id:
        return HttpResponse(json.dumps(attandance_list, ensure_ascii=False), content_type="application/json, charset=utf-8")
    employee_id = int(employee_id)
    employee_attendance_log = EmployeeAttendance.objects.filter(employee_id=employee_id).order_by("-check_time").all()
    for item in employee_attendance_log:
        is_late = "否"
        if item.type == 1:
            is_late = "是"
        attandance_list.append({
                    "employee_id": employee_id, "employee_name": item.employee.name,
                     "is_late": is_late, "checktime": str(item.check_time), "standardtime": item.standard_time})
    return HttpResponse(json.dumps(attandance_list, ensure_ascii=False), content_type="application/json, charset=utf-8")

@checklogin()
def employee_person_promotion_list_json(request):
    employee_id = request.POST.get("employee_id")
    promotion_list = []
    if not employee_id:
        return HttpResponse(json.dumps(promotion_list, ensure_ascii=False), content_type="application/json, charset=utf-8")
    employee_id = int(employee_id)
    employee_promotion_log = EmployPromoteHistory.objects.filter(employee_id=employee_id).order_by("-log_time").all()
    for item in employee_promotion_log:
        promote_type = "晋升"
        if item.type == 1:
            promote_type = "离职"
        elif item.type == 2:
            promote_type = "降职"
        promotion_list.append({
            "employee_id": employee_id, "employee_name": item.employee.name, "datetime": str(item.log_time),
            "promote_type": promote_type, "from_level_name": item.from_level.name, "to_level_name": item.to_level.name})
    return HttpResponse(json.dumps(promotion_list, ensure_ascii=False), content_type="application/json, charset=utf-8")

@checklogin()
def employee_attendance_chart_json(request):
    employee_id = request.POST.get("employee_id")
    attendance_list = {"xAxis": [], "values": []}
    if not employee_id:
        return HttpResponse(json.dumps(attendance_list, ensure_ascii=False), content_type="application/json, charset=utf-8")
    employee_id = int(employee_id)
    today = datetime.date.today()
    first_day = today.replace(day=1)
    last_month = first_day - datetime.timedelta(days=1)
    last_month_today = last_month.replace(day=today.day)
    attendance_objs = EmployeeAttendance.objects.filter(employee_id=employee_id, check_time__gte=last_month_today).order_by("check_time").all()
    curr_datetime = last_month_today
    item_index = 0
    while curr_datetime != today:
        datestr = curr_datetime.strftime("%Y-%m-%d")
        attendance_list["xAxis"].append(datestr)
        if item_index < len(attendance_objs):
            item = attendance_objs[item_index]
        else:
            item = None
        if item and item.check_time.date() == curr_datetime:
            attendance_list["values"].append({"name": datestr, "value": item.check_time.timetuple().tm_hour})
            item_index += 1
        else:
            attendance_list["values"].append({"name": datestr, "value": 0})
        curr_datetime = curr_datetime + datetime.timedelta(days=1)
    return HttpResponse(json.dumps(attendance_list, ensure_ascii=False), content_type="application/json, charset=utf-8")







