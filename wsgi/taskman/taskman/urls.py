"""taskman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'taskman.views.index' , name="index"),
    url(r'^register/$', 'taskman.views.register_user' , name="register"),
    url(r'^home/$', 'taskman.views.dashboard', name="home" ),
    url(r'^home/create/$', 'taskManager.views.create_task', name="create" ),
    url(r'^update/$', 'taskManager.views.update_task', name="update" ),
    url(r'^update/multiple/$', 'taskManager.views.update_multiple', name="updatemultiple" ),
    url(r'^logout/$', 'taskman.views.logout_user', name="logout" ),
]
