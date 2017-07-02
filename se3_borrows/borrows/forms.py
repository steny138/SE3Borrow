# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from borrows.models import Sim, Borrower

from django.forms import ModelForm
from django import forms
from borrows import settings

class SimForm(ModelForm):

    number = forms.CharField(label='Sim卡號碼', required=True)
    title = forms.CharField(label='Sim卡描述', required=False)
    operate = forms.ChoiceField(label='電信商', widget=forms.Select, choices=settings.OPERATE_CHOICES, required=True)
    status = forms.ChoiceField(label='用途', widget=forms.RadioSelect, choices=settings.STATUS_CHOICES, required=True)

    class Meta:
        model = Sim
        fields = ['number', 'title', 'operate', 'status']