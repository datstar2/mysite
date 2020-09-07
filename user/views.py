from django.http import HttpResponse, HttpResponseRedirect
import user.models as usermodels
from django.shortcuts import render


def joinform(request):
    return render(request, 'user/joinform.html')

def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')

def join(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    gender = request.POST['gender']
    usermodels.insert(name, email, password, gender)
    return HttpResponseRedirect('/user/joinsuccess')


def loginform(request):
    return render(request, 'user/loginform.html')

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    result = usermodels.fetchone(email, password)
    if result is None:
        return HttpResponseRedirect('/user/loginform?result=fail')
    # login 처리
    request.session['auth'] = result
    return HttpResponseRedirect('/')

def logout(request):
    del request.session['auth']
    return HttpResponseRedirect('/')

def updateform(request):
    no = request.session['auth']['no']
    result = usermodels.fetchonebyno(no)
    data = {'user': result}
    return render(request, 'user/updateform.html', data)

def update(request):
    no = request.session['auth']['no']
    name = request.POST['name']
    gender = request.POST['gender']
    if request.POST['password'] != '':
        password = request.POST['password']
        usermodels.updateuser(name, password, gender, no)
    else:
        usermodels.updateuserwd(name, gender, no)
    return HttpResponseRedirect('/user/logout')