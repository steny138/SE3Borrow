# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from home import settings
from sim.models import Sim

class Borrower(models.Model):
    """docstring for Borrow"""
    no = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    sim = models.ForeignKey(Sim)
    
    purpose = models.CharField(max_length=10, null=True)
    purpose_other = models.CharField(max_length=1100, null=True)

    created_date = models.DateTimeField(
            default=timezone.now)
    rent_date = models.DateTimeField(null=True)
    borrow_date = models.DateTimeField(null=True)
    
    published_date = models.DateTimeField(
            blank=True, null=True)

    class Meta:
        db_table = 'Borrower'

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __unicode__(self):
        return str(self.user)
        
    
    def __str__(self):
        return self.no
        