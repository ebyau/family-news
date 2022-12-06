from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('user/',views.user_site,name='user_site'),
    path('upload/', views.upload, name='upload'),
    path('howtoupload',views.how_to_upload,name='howtoupload'),
    path('login/',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    #path('dashboard',view.dashboard,name='dashboard')


]
