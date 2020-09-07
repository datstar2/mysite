from django.http import HttpResponse, HttpResponseRedirect
import guestbook.models as guestbookmodel
from django.shortcuts import render


def index(request):
    results = guestbookmodel.fetchlist()
    data = {'guestbooklist':results}
    return render(request, 'guestbook/index.html', data)


def add(request):
    name = request.POST['name']
    password = request.POST['password']
    message = request.POST['message']
    guestbookmodel.insert(name, password, message)
    return HttpResponseRedirect('/guestbook')

def deleteform(request):
    no = request.GET['no']
    data = {'no' : no}
    return render(request, 'guestbook/deleteform.html')

def delete(request):
    no = request.POST['no']
    password = request.POST['password']
    guestbookmodel.delete(no, password)
    return HttpResponseRedirect('/guestbook')
