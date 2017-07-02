from django.shortcuts import render

from datetime import datetime
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', {
        'current_time': datetime.now().strftime('%Y-%m-%d(%a) %H:%M:%S'),
    })