"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from contacts.views import ContactsApiView
from header.views import HeaderAPIView
from menuItems.views import MenuItemsApiView
from projectStepsPage.views import ProjectStepsApiView
from request.views import RequestApiView
from workProcessPage.views import WorkProcessPageApiView

router = DefaultRouter()

router.register(r"project_steps", ProjectStepsApiView, basename="project_steps")
router.register(r"work_process", WorkProcessPageApiView, basename="work_process")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include(router.urls)),
    path('api/v1/header/', HeaderAPIView.as_view()),
    path('api/v1/contacts/', ContactsApiView.as_view()),
    path('api/v1/request/', RequestApiView.as_view()),
    path('api/v1/menu_items/', MenuItemsApiView.as_view()),
]