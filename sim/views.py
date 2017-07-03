# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# -*- coding: utf-8 -*-

from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from sim.models import Sim
from sim.forms import SimForm

def sim(request):
    return render(request, 'sim.html', {"sim_cards" : Sim.objects.all()})

def sim_add(request):
    form = SimForm(request.POST or None)
    if form.is_valid():
        sim = form.save(commit=False)
        # sim.status = "1"
        sim.save()
        return redirect('/sim/')
    return render(request, 'sim_new.html', {'form':form})

def sim_update(request, pk):
    sim= get_object_or_404(Sim, pk=pk)
    form = SimForm(request.POST or None, instance=sim)
    if form.is_valid():
        form.save()
        return redirect('/sim/')
    return render(request, 'sim_detail.html', {'form':form})


def sim_delete(request, pk):
    sim= get_object_or_404(Sim, pk=pk)
    form = SimForm(request.POST or None, instance=sim)
    if request.method=='POST' and form.is_valid():
        sim.delete()
        return redirect('/sim/')
    return render(request, 'sim_detail.html', {'form':form})