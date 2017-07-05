# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages,auth
from django.db.models import Count

from borrows.models import Borrower
from borrows.forms import BorrowForm

from home import settings

from sim.models import Sim

from collections import defaultdict

@login_required
def borrow(request):
    current_user = auth.get_user(request)
    if not current_user.is_superuser:
        data = Borrower.objects.filter(user=current_user)
    else:
        data = Borrower.objects.all()
    
    # group by user, show the user rent sim cards information.
    res = {}
    for item in data:
        res.setdefault(item.user.username, []).append(item)

    return render(request, 'borrow.html', {"borrow_cards" : res})

@login_required
def borrow_add(request):
    form = BorrowForm(request.POST or None)
    if form.is_valid():
    	num = form.cleaned_data["number"] # type is <class 'sim.models.Sim'>
        borrower = form.save(commit=False)
        borrower.user = request.user 
        borrower.sim = num
        try:
            borrower.save()
            sim = num
            sim.status = "2"
            sim.save()
        except DatabaseError:
            messages.error(request, "資料庫發生錯誤，請稍後再試！")
        except TransactionManagementError:
            messages.error(request, "寫入資料庫失敗，請稍後再試！")

        return redirect('/borrow/')
    return render(request, 'borrow_new.html', {'form':form})

@login_required
def borrow_update(request, pk):
    borrow= get_object_or_404(Borrower, pk=pk)
    form = BorrowForm(request.POST or None, instance=borrow)

    form.fields['number'].queryset = Sim.objects.filter(number=borrow.sim.number).all()
    form.fields['number'].empty_label = None

    if form.is_valid():
        form.save()
        return redirect('/borrow/')
    return render(request, 'borrow_new.html', {'form':form})

@login_required
def borrow_delete(request, pk):
    borrow= get_object_or_404(Borrower, pk=pk)
    form = BorrowForm(request.POST or None, instance=borrow)

    form.fields['number'].queryset = Sim.objects.filter(number=borrow.sim.number).all()
    form.fields['number'].empty_label = None

    if request.method=='POST' and form.is_valid():
        borrow.delete()
        sim = form.cleaned_data["number"]
        sim.status = "1"
        sim.save()

        return redirect('/borrow/')
    return render(request, 'borrow_new.html', {'form':form})
