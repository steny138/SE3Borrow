# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from borrows.models import Borrower

from django.forms import ModelForm
from django import forms

from home import settings

class BorrowForm(ModelForm):

    borrowType = forms.CharField(label='類型', required=True)
   
    class Meta:
        model = Borrower
        fields = ['borrowType']