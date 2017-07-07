# -*- coding: utf-8 -*-

from django.views.decorators.cache import cache_page
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from datetime import datetime
from django.http import HttpResponse

from datetime import datetime

from sim.models import Sim
from borrows.models import Borrower

import json

@cache_page(60 * 10)
def index(request):
    # 取得Sim卡全部資料
    simcards = Sim.objects.all()

    # 初始化圖表
    chart_rows = []
    chart_row = []

    # 加入 電信商圓餅圖
    chart_row.append(__operate_chart(simcards))

    # 加入 借用狀態圓餅圖
    chart_row.append(__sim_status_chart(simcards))

    chart_rows.append(chart_row)

    return render(request, 'index.html', {
        'chart_rows': chart_rows
    })

def __operate_chart(simcards):
    chart_row = []

    # group by user, show the user rent sim cards information.
    res = {}
    for item in simcards:
        res.setdefault(item.get_operate_display(), []).append(item)


    chart = {}
    chart["size"] = 5
    chart["title"] = "Sim卡"
    chart["desp"] = "電信商分佈數量"
    chart["id"] = "sim_operate"
    chart["time"] = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    chart["items"] = []
    
    count = 97
    labels = []
    series = []
    for key in res:
        labels.append("%3.0f%%" % ((len(res[key])/1.0/len(simcards))*100//1.0))
        series.append(len(res[key]))
        chart["items"].append({ "name":key, "color":chr(count)})
        count += 1

    chart["labels"] = json.dumps(labels)
    chart["series"] = json.dumps(series)
    
    return chart

def __sim_status_chart(simcards):
    
    # group by user, show the user rent sim cards information.
    res = {}
    for item in simcards:
        res.setdefault(item.get_status_display(), []).append(item)
    chart = {}
    chart["size"] = 5
    chart["title"] = "Sim卡"
    chart["desp"] = "借用狀態分佈"
    chart["id"] = "sim_status"
    chart["time"] = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    chart["items"] = []
    
    count = 97
    labels = []
    series = []
    for key in res:
        labels.append("%3.0f%%" % ((len(res[key])/1.0/len(simcards))*100//1.0))
        series.append(len(res[key]))
        chart["items"].append({ "name":key, "color":chr(count)})
        count += 1

    chart["labels"] = json.dumps(labels)
    chart["series"] = json.dumps(series)
    return chart

def login(request):
    if request.user.is_authenticated(): 
        return redirect('/index/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        next_page = request.GET.get('next', '')
        
        if next_page:
            return redirect(next_page)
        else:
            return redirect('/index/')
        
    else:
        return render(request, 'login.html') 

def logout(request):
    if request.user.is_authenticated(): 
        auth.logout(request)
        return redirect('/accounts/login/')
    return redirect('/')

def set_password(request):
    if not request.user.is_authenticated(): 
        return redirect('/login/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    new_password = password = request.POST.get('password', '')

    u = User.objects.get(username='john')
    u.set_password('new password')
    u.save()
