# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from borrows.models import Borrower
from borrows.forms import BorrowForm

# Create your views here.

def borrow(request):
    return render(request, 'borrow.html', {})
