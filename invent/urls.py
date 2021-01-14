"""invent URL Configuration

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
from django.urls import path
from asset import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('search',views.search),
    path('searchGlobal',views.searchGlobal),
    path('fetchALL',views.fetchALL),
    path('',views.index),
    path('asset',views.asset),
    path('assetDelete',views.assetDelete),
    path('assetAdd',views.assetAdd),
    path('createFrom',views.createFrom),
    path('addForm',views.addForm),
    path('editForm',views.editForm),
    path('saveForm',views.saveFrom),
    path('upload',views.upload),
    path(r'^export/xls/$', views.export_users_xls, name='export_users_xls'),
    path('readExcel', views.readExcel,name='readExcel')

]
