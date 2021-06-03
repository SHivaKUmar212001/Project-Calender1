from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User


MeetingType= (
    ('Interview','Interview'),
    ('FormalMeeting','Formal Meeting'),
    ('Annual General Meeting', 'Annual General Meeting'),
    ('Statutory Meeting','Statutory Meeting'),
    ('Board Meeting','Board Meeting'),
    ('Informal Meeting','Informal Meeting'),
)


class Event(models.Model):
    title = models.CharField(max_length=200)
    Host_ID = models.ForeignKey(User,on_delete=models.CASCADE, default = User)
    Meeting_ClientName = models.CharField(max_length=200)
    Meeting_ClientID = models.EmailField(max_length=200)
    Meeting_Link = models.CharField(max_length=200)
    Meeting_Type = models.CharField(max_length=40, choices=MeetingType)
    Purpose_Of_Meeting = models.TextField()
    Meeting_time = models.DateTimeField()




    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

class LoggedInUser(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, related_name='logged_in_user',on_delete=models.CASCADE)
    session_key=models.CharField(max_length=32, blank=True,null=True)

    def __str__(self):
        return self.user.username
