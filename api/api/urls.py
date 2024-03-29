"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include
from tastypie.api import Api
from app.resources import *

v1_api = Api(api_name='v1')
v1_api.register(UserByIdResource())
v1_api.register(PortfolioByIdResource())
v1_api.register(GoalByIdResource())
v1_api.register(AppointementsByUserIdResource())
v1_api.register(UserAuth())
v1_api.register(PortfolioInPdf())
v1_api.register(HelpResource())

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(v1_api.urls))
]
