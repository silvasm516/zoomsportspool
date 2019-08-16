from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.template import Context
from django.template.context_processors import csrf
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
##from django.contrib.sessions.models import Session



# Create your views here.







def enter(request):
    from django.template import Template
    from django.template import loader
    
    
    
    

    
    a = "Player Login" 
    c = {
         'tit': a,
         
         }
    
    temp = loader.get_template('login.html') 
    return HttpResponse(temp.render(c,request))                        
      







def logP(request, first, email, authcode):
    from django.contrib.auth.models import User
    from django.contrib.auth import authenticate, login
    username = first
    password = email
    user = authenticate(username=username, password=password)
    login(request, user)
    request.session['UsrName'] = username 
    request.session['UsrType'] = 'p'
    request.session['Ackcode'] = authcode
    
    
