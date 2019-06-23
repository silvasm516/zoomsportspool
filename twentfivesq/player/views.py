from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.template import Context
from django.template.context_processors import csrf
from django.template import loader
# Create your views here.







def Login(request):
    from django.template import Template
    from django.template import loader
    from django.template import loader
    
    
    a = "Player Login" 
    c = {
         'tit': a,
         
         }
    
    temp = loader.get_template('login.html') 
    return HttpResponse(temp.render(c,request))                        

