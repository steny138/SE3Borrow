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
    if request.user.is_authenticated():
        print request.user.username

    form = BorrowForm(request.POST or None)
    if form.is_valid():
        borrower = form.save(commit=False)
        borrower.user = request.user 
        borrower.sim = Sim.objects.get(number= form.cleaned_data["number"])
        try:
            borrower.save()

            sim = Sim.objects.get(number= form.cleaned_data["number"])
            sim.status = "2"
            sim.save()

        except DatabaseError:
            messages.error(request, "資料庫發生錯誤，請稍後再試！")
        except TransactionManagementError:
            messages.error(request, "寫入資料庫失敗，請稍後再試！")

        return redirect('/borrow/')
    return render(request, 'borrow_new.html', {'form':form})

def borrow_update(request):
    return render(request, 'borrow_new.html', {})

def borrow_delete(request):
    return render(request, 'borrow_new.html', {})
