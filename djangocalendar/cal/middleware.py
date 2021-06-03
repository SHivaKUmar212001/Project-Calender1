# -*- coding: utf-8 -*-

from django.contrib.sessions.models import Session
from .views import event

class OneSessionPerUser:
    def __init__(self,get_response):
        self.get_response=get_response
        
    def __call__(self,request):
        if request.user.is_authenticated:
            current_session_key=request.user.logged_in_user.session_key
            print(request.user.id,"CCCCC")
            if current_session_key and current_session_key != request.session.session_key:
                # Session.objects.get(session_key=current_session_key).delete()
                # event.get(session_key=current_session_key).delete()
                request.session['user_id'] = request.user.id
            request.user.logged_in_user.session_key = request.session.session_key
            print(request.user.logged_in_user.session_key)
            request.user.logged_in_user.save()
        
        response=self.get_response(request)
        
        return response
    
    
# from django.contrib.sessions.models import Session
# from flask import request

# def auth_middleware(get_response):
   
#    def middleware(request,):
#         print('middleware') 
#         if request.user.is_authenticated:
#             stored_session_key = request.user.logged_in_user.session_key
#         if stored_session_key and stored_session_key !=request.session.session_key:
#             Session.objects.get(session_key=storeed_session_key).delete()
#             request.user.logged_in_user.session_key=request.sesssion.session_key
#             request.user.logged_in_user.save()
#             response = get_response(request)
#         return response
        
        
#    return middleware    