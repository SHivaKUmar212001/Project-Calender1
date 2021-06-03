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

from .models import *
from .utils import Calendar
from .forms import EventForm, CreateUserForm

from django.conf import settings
from django.core.mail import send_mail


def registerPage(request):
    form=CreateUserForm()

    if request.method =="POST":
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)
            return redirect('cal:login')

    context={'form':form}

    return render(request, 'cal/register.html',context)

# def loginPage(request):
#     m = Member.objects.get(username=request.POST['username'])
#     if m.password == request.POST['password']:
#         request.session['member_id'] = m.id
#         return redirect('cal:calendar')
#     else:
#         return HttpResponse("Your username and password didn't match.")

#     context={}
#     return render(request, 'cal/login.html', context)

# def loginPage(request,pk):
#     # if request.session.get(id=pk):

#     #     return HttpResponse(user.id)

#         if request.method=="POST":
#             username=request.POST.get('username')
#             password= request.POST.get('password')


#             user=authenticate(request,username=username, password=password)
#             request.session['foo']={}

#             if user is not None:
#                 login(request,user)
#                 return redirect('cal:calendar')
#             else:
#                 messages.info(request,'Username or Password is incorrect')


#         context={}
#         return render(request, 'cal/login.html', context)

#     # else:
#     #     return HttpResponse("User doesnot exist")

def loginPage(request):
    # if request.session.get(pk,use_id):
    #     return HttpResponse(user.id)

    if request.method=="POST":
        username=request.POST.get('username')
        password= request.POST.get('password')


        user=authenticate(request,username=username, password=password)

        # user=request.session['user']

        if user is not None:
            login(request,user)
            return redirect('cal:calendar')
        else:
            messages.info(request,'Username or Password is incorrect')


    context={}
    return render(request, 'cal/login.html', context)

    # else:
    #     return HttpResponse("User doesnot exist")

def logoutUser(request):
    logout(request)
    return redirect('cal:index')

def index(request):
    return render(request, 'cal/index.html')

def nav(request):
    return render(request, 'cal/nav.html')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)

        # print ("key:=>"+request.session['user'])
        ##print the request sesssion here
        return context


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


from cal.models import Event
def event(request, event_id=None):
    instance = Event()
    if event_id:
        print(event_id)
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        btn_name = request.POST.get('send_email')
        print(btn_name)
        if btn_name == "Send Email":
            sub= instance.title
            body= instance.Purpose_Of_Meeting
            from_email= settings.EMAIL_HOST_USER
            to_email= instance.Meeting_ClientID
            send_mail(sub, body, from_email,[to_email],fail_silently=False,)
            return HttpResponse("Email is send")
        return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request, 'cal/event.html', {'form': form})
