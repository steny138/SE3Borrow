# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from borrows.models import Borrower

from django.forms import ModelForm
from django.forms.extras import SelectDateWidget
from django import forms

from home import settings
from home.widget import DateTimePicker
from borrows.models import Borrower
from sim.models import Sim
from datetime import datetime

class BorrowForm(ModelForm):
    number = forms.ModelChoiceField(
        label="Sim卡", 
        empty_label="請選擇",
        queryset = Sim.objects.filter(status="1").all(),
        required=True)

    purpose = forms.ChoiceField(label='借用原因', 
        widget=forms.RadioSelect, 
        choices=settings.PURPOSE_CHOICES, 
        required=True)

    purpose_other = forms.CharField(label='其他原因', required=False)
    # rent_date = forms.DateField(label="租借日",
    #     widget=SelectDateWidget(
    #         empty_label=("Choose Year", "Choose Month", "Choose Day"),
    #     ), 
    #     required=True
    # )
    rent_date = forms.DateField(label="租借日",
                                widget=DateTimePicker(options={"format": "YYYY/MM/DD"}),
                                input_formats=["%Y/%m/%d"],
                                initial=datetime.now())

    borrow_date = forms.DateField(label="到期日",
                                widget=DateTimePicker(options={"format": "YYYY/MM/DD"}),
                                input_formats=["%Y/%m/%d"])

    class Meta:
        model = Borrower
        fields = ['number',"purpose","purpose_other","rent_date","borrow_date"]

    # def __init__(self,  *args,  **kwargs):
    #     super(BorrowForm, self).__init__(*args, **kwargs) 
    #     self.fields['number'].queryset = Sim.objects.none()
    #     if 'number' in self.data:
    #         self.fields['number'].queryset = Sim.objects.filter(number=self.data['number']).all()

