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
from .import views



urlpatterns = [
    path('m-profile/', views.m_profile, name='m-profile'),
    path('m_all_members/', views.m_all_members, name='m_all_members'),
    #path('add-members/', views.add_members, name='add-members'),
    path('m-view-notice/',views.m_view_notice, name='m-view-notice'),
    path('m-view-notice-details/<int:pk>',views.m_view_notice_details, name='m-view-notice-details'),
    path('add-complain/',views.add_complain, name='add-complain'),
    path('m-view-complain/',views.m_view_complain, name='m-view-complain'),
    path('m-add-event/',views.m_add_event, name='m-add-event'),
    path('m-view-event/',views.m_view_event, name='m-view-event'),
]