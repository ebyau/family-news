from django.urls import path
from . import views


urlpatterns = [
        path('',views.home2,name='home2'),
        path('login_user', views.login_user,name='login'),
        path('logout/',views.logout_user,name='logout'),
        path('upload/',views.upload,name='upload'),
        path('register/',views.register_user,name='register'),
    ]
