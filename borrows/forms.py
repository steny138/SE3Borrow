# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from borrows.models import Borrower

from django.forms import ModelForm
from django import forms

from home import settings
from borrows.models import Borrower
from sim.models import Sim

def get_sim_choices(): 
    # you place some logic here 
    sim_choices = [(None,'請選擇')]
    sim_choices +=[(m.sim_id, m.number) for m in Sim.objects.filter(status="1").all()]

    # sim_choices = [(m.sim_id, m.number) for m in Sim.objects.all()]
    print "exeute"
    return sim_choices

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
    class Meta:
        model = Borrower
        fields = ['number',"purpose","purpose_other"]

    # def __init__(self,  *args,  **kwargs):
    #     super(BorrowForm, self).__init__(*args, **kwargs) 
    #     self.fields['number'].queryset = Sim.objects.none()
    #     if 'number' in self.data:
    #         self.fields['number'].queryset = Sim.objects.filter(number=self.data['number']).all()

