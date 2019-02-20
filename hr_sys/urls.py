# coding : utf-8
from django.urls import path, re_path
from .views import user_auth_views, main_frame_views, department_views, employee_views

urlpatterns = [
    re_path('^login/.*$', user_auth_views.login, name='login'),
    path('logout', user_auth_views.logout, name='logout'),
    path('', main_frame_views.index, name='main_frame'),
    path('overview', main_frame_views.overview, name='overview'),
    # 部门管理
    path('department_list', department_views.department_list, name='department_list'),
    path('department_tree_json', department_views.department_tree_json, name="department_tree_json"),
    path('add_department', department_views.add_department, name='add_department'),
    path('edit_remove_department', department_views.edit_remove_department, name='edit_remove_department'),
    path('employee_level', department_views.department_level, name='employee_level'),
    path('employee_level_json', department_views.employee_level_json, name='employee_level_json'),
    path('employee_level_add', department_views.employee_level_add, name='employee_level_add'),
    path('employee_level_edit', department_views.employee_level_edit, name='employee_level_edit'),
    path('employee_level_del', department_views.employee_level_del, name='employee_level_del'),
    path('position_list', department_views.position_list, name='position_list'),
    path('position_json', department_views.position_json, name='position_json'),
    path('position_add', department_views.position_add, name='position_add'),
    path('position_edit', department_views.position_edit, name='position_edit'),
    path('position_del', department_views.position_del, name='position_del'),
    path('department_manager', department_views.department_manager, name='department_manager'),
    path('department_json', department_views.department_json, name='department_json'),
    path('department_manager_edit', department_views.department_manager_edit, name='department_manager_edit'),
    # 员工管理
    path('employee_list', employee_views.employee_list, name='employee_list'),
    path('employee_list_json', employee_views.employee_list_json, name='employee_list_json'),
    path('employee_add', employee_views.employee_add, name='employee_add'),
    path('employee_edit', employee_views.employee_edit, name='employee_edit'),
    path('employee_del', employee_views.employee_del, name='employee_del'),
]