from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from cal.models import *

from django.conf import settings
from django.core.mail import send_mail


def check(request):
    return render(request, 'confirm.html')

def confirm(request, event_id=None):
    obj = Confirm()
    btn = request.POST.get('Confirm')
    print(btn)
    if btn == "CONFIRM":
        obj.confirm = True
