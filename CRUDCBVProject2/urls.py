"""
URL configuration for CRUDCBVProject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from MyApps1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.EmployeeListView.as_view(), name='home'),
    path('detail/<pk>', views.EmployeeDetailView.as_view(), name='detail'),
    path('create/', views.EmployeeCreateView.as_view(),name='create'),
    path('update/<pk>', views.EmployeeUpdateView.as_view(),name='update'),
    path('delete/<pk>', views.EmployeeDeleteView.as_view(),name='delete'),
]
