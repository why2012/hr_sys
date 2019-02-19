from django.urls import path, re_path
from .views import user_auth_views, main_frame_views, department_views

urlpatterns = [
    re_path('^login/.*$', user_auth_views.login, name='login'),
    path('logout', user_auth_views.logout, name='logout'),
    path('', main_frame_views.index, name='main_frame'),
    path('overview', main_frame_views.overview, name='overview'),
    path('department_list', department_views.department_list, name='department_list'),
    path('department_tree_json', department_views.department_tree_json, name="department_tree_json"),
    path('add_department', department_views.add_department, name='add_department'),
    path('edit_remove_department', department_views.edit_remove_department, name='edit_remove_department'),
]