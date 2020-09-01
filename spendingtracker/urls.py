"""spendingtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework import routers
import spendings.views

me_router = routers.SimpleRouter()
me_router.register(
    'spendings', spendings.views.SpendingViewSetForUser, basename='spending')

me_urls = [
    path('', include(me_router.urls)),
]

api_urls = [
    path('me/', include((me_urls, 'me')))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((api_urls, 'api'))),
]
