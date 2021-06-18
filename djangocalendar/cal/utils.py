from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import *


class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		# self.user = user
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):

		events_per_day = events.filter(Meeting_time__day=day)
		d = ''
		for event in events_per_day:
			d += f'<li> {event.get_html_url} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		for i  in LoggedInUser.objects.all():
				# print("logged in",i.user)
				ans = i.user
				# print("final",ans)

		events = Event.objects.filter(Meeting_time__year=self.year, Meeting_time__month=self.month,Host_ID=ans)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal
