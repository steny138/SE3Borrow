# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from borrows import views

urlpatterns = patterns('',
    url(r'^$', views.borrow),
)

  	# url(r'^new$', views.sim_add, name='sim_new'),
   #  url(r'^delete/(?P<pk>\d+)$', views.sim_delete, name='sim_delete'),
   #  url(r'^(?P<pk>\d+)$', views.sim_update, name='sim_update'),