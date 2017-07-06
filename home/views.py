from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from datetime import datetime
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {
        'current_time': datetime.now().strftime('%Y-%m-%d(%a) %H:%M:%S'),
    })

def login(request):
    print "login"
    if request.user.is_authenticated(): 
        print "is_authenticated"
        return redirect('/index/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        print "is_active"
        auth.login(request, user)
        next_page = request.GET.get('next', '')
        
        if next_page:
            return redirect(next_page)
        else:
            return redirect('/index/')
        
    else:
        return render(request, 'login.html') 


def logout(request):
    print "logout"
    if request.user.is_authenticated(): 
        print "processing"
        auth.logout(request)
        return redirect('/accounts/login/')
    return redirect('/')
