# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.urls import path

# ans = whichuser
app_name = 'cal'
urlpatterns = [
    # path('register/',views.registerPage,name='register'),
    # path('login/',views.loginPage,name='login'),

    url(r'^register/$',views.registerPage,name='register'),
    url('^login/$',views.loginPage,name='login'),
    url('^logout/$',views.logoutUser,name='logout'),
    url('^check/(?P<event_id>\d+)/$',views.check,name='check'),
    #url('/conf',views.conf,name='conf'),

    url(r'^nav/$', views.nav, name='nav'),
    url(r'^$', views.index, name='index'),
    # url(r'^index/$', views.index, name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', views.event, name='event_new'),
 	url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]
