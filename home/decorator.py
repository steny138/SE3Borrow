# -*- coding: utf-8 -*-

try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps  # Python 2.4 fallback.
from django.utils.decorators import available_attrs
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

default_message = "您沒有管理者權限。"

def user_passes_test(test_func, message=default_message, redirect_url="/"):
    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):                
            decorated_view_func = login_required(request)
            if not decorated_view_func.user.is_authenticated():
                return decorated_view_func(request)  # return redirect to signin

            if not test_func(request.user):
                messages.error(request, message)
                return redirect(redirect_url)

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

def super_login_required(view_func=None, message=default_message, redirect_url="/"):
    super_login_func = user_passes_test(
        lambda u: u.is_superuser,
        message=message,
        redirect_url=redirect_url
    )

    if view_func:
        return super_login_func(view_func)
    return super_login_func
