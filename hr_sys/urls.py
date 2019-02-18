from django.urls import path, re_path

from . import views
from .views import user_auth_views, main_frame_views

urlpatterns = [
    re_path('^login/.*$', user_auth_views.login, name='login'),
    path('logout', user_auth_views.logout, name='logout'),
    path('', main_frame_views.index, name='main_frame'),
]