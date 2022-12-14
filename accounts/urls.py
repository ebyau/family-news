from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.landing_page, name='landing_page'),
    path('family_news/',views.family_news,name='family_news'),
    path('home/',views.home,name='home'),
    path('upload/', views.upload, name='upload'),
    path('howtoupload',views.how_to_upload,name='howtoupload'),
    path('login/',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    #path('dashboard',view.dashboard,name='dashboard')


]
