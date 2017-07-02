"""se3_borrows URL Configuration

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
from borrows.views import index, borrow, sim, sim_add, sim_update, sim_delete

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^borrow/', borrow),
    url(r'^sim/new', sim_add, name='sim_new'),
    url(r'^sim/delete/(?P<pk>\d+)$', sim_delete, name='sim_delete'),
    url(r'^sim/(?P<pk>\d+)$', sim_update, name='sim_update'),
    url(r'^sim', sim),
    url(r'$', index),
]
