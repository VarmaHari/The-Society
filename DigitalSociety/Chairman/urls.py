"""DigitalSociety URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Chairman import views


urlpatterns = [
    path('home/',views.home,name="home"), 
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('c-profile/',views.c_profile,name="c-profile"),
    path('c-dashboard/',views.c_dashboard,name="c-dashboard"),
    path('forgot-password/',views.forgot_password,name="forgot-password"),
    path('reset-password/',views.reset_password,name="reset-password"),
    path('add-member/',views.add_member,name='add-member'),
    path('all-member/',views.all_member,name='all-member'),
    #path('update/',views.update,name='update'),
    path('add-notice/',views.add_notice, name='add-notice'),
    path('view-notice/',views.view_notice, name='view-notice'),
    path('watchman/',views.watchman, name="watchman"),
    path('approved/<int:pk>/',views.approved,name="approved"),
    path('rejected/<int:pk>/',views.rejected, name="rejected"),
    path('del-notice/<int:pk>/',views.del_notice,name='del-notice'),
    path('m-noticeview-details/<int:pk>/',views.m_noticeview_details,name='m-noticeview-details'),
    path('view-complain/',views.view_complain, name='view-complain'),
    path('add-event/',views.add_event, name='add-event'),
    path('view-event/',views.view_event, name='view-event'),

    ] 
