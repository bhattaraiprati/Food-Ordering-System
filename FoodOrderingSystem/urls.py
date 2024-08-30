"""
URL configuration for FoodOrderingSystem project.

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
from order.views import *
from restaurant.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", landingPage ),
    path("register/", register_page , name="register_page" ),
    path("sign-in/", signin_page , name="signin_page" ),
    path("sign-up/", signup_page , name="signup_page" ),



]
