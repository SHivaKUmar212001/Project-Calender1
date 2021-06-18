# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.urls import path
from .views import CalendarJsonListView, CalendarView

urlpatterns = [
  path('calendar_json/', CalendarJsonListView.as_view(), name='calendar_json'),
  path('calendarview/',CalendarView.as_view(),name='calendar'),
]
