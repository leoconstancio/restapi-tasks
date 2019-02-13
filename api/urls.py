"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from api.todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='list_tasks'),
    path('api/v1/tasks', views.task_list),
    re_path('api/v1/tasks/(?P<id_task>[0-9]+)', views.task_detail),
    # DRF API View
    path('api/v2/', include('api.todo.api_urls'))
]
