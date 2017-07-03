# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from borrows import views

urlpatterns = patterns('',
    url(r'^new$', views.borrow_add, name='borrow_new'),
    url(r'^delete/(?P<pk>\d+)$', views.borrow_delete, name='borrow_delete'),
    url(r'^(?P<pk>\d+)$', views.borrow_update, name='borrow_update'),
    url(r'^$', views.borrow),   
)