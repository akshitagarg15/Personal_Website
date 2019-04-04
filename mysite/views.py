from django.shortcuts import render

from .models import contact

import requests,json
# Create your views here.
#from django.http import HttpResponse

#def Index(request):
#    return HttpResponse("Hello World")

def Index(request):
    if request.method == 'POST':
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        #print(firstname)
        r=requests.get('https://api.icndb.com/jokes/random?firstName='+firstname +'&amp;lastName='+lastname)
        #print(r.text)
        json_data=json.loads(r.text)  #json.loads is converting json into dict and storing in json_dats
        #print(json_data)
        joke=json_data.get('value').get('joke')
        #print(joke)
        context={'joke':joke}
        return render(request,'mysite/index.html',context)
    else:  #get method
        firstname='akshita'
        lastname='garg'
        #print(firstname)
        r=requests.get('https://api.icndb.com/jokes/random?firstName='+firstname +'&amp;lastName='+lastname)
        #print(r.text)
        json_data=json.loads(r.text)  #json.loads is converting json into dict and storing in json_dats
        #print(json_data)
        joke=json_data.get('value').get('joke')
        #print(joke)
        context={'joke':joke}
        return render(request,'mysite/index.html',context)


def Contact(request):
    if request.method == 'POST':
        email_r=request.POST.get('email')
        subject_r=request.POST.get('subject')
        message_r=request.POST.get('message')

        c=contact(email=email_r,subject=subject_r,message=message_r)
        c.save()

        return render(request,'mysite/thank.html')
    else:
        return render(request,'contact.html')

def Portfolio(request):
    return render(request,'mysite/portfolio.html')
