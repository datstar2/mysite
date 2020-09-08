from django.http import HttpResponse, HttpResponseRedirect
import board.models as boardmodel
from django.shortcuts import render



def index(request):
    results = boardmodel.fetchlist()
    data = {'boardlist':results}
    return render(request, 'board/index.html', data)

def writeform(request):
    return render(request, 'board/writeform.html')

def write(request):
    title = request.POST['title']
    content = request.POST['content']
    user_no = request.session['auth']['no']
    boardmodel.insert(title, content, user_no)
    no = boardmodel.maxno()
    gno = boardmodel.maxg_no()
    boardmodel.g_noplus(gno, no)
    return HttpResponseRedirect('/board')

def viewform(request):
    no = request.GET['no']
    boardmodel.hitplus(no)
    results = boardmodel.fetchonebyno(no)
    data = {'board': results}
    return render(request, 'board/viewform.html', data)

def modifyform(request):
    no = request.GET['no']
    results = boardmodel.fetchonebyno(no)
    data = {'board': results}
    return render(request, 'board/modifyform.html', data)

def modify(request):
    no = request.GET['no']
    title = request.POST['title']
    content = request.POST['content']
    boardmodel.updateboard(title, content, no)
    return HttpResponseRedirect('/board')

def replyform(request):
    no = request.GET['no']
    results = boardmodel.fetchonebynore(no)
    data = {'replylist': results}
    return render(request, 'board/replyform.html', data)

def reply(request):
    g_no = request.POST['g_no']
    o_no = str(int(request.POST['o_no'])+1)
    depth = str(int(request.POST['depth'])+1)
    title = request.POST['title']
    content = request.POST['content']
    user_no = request.session['auth']['no']
    boardmodel.insert(title, content, user_no)
    no = boardmodel.maxno()
    boardmodel.updatereply(g_no, o_no, depth, no)
    boardmodel.neworder(g_no, o_no, no)
    return HttpResponseRedirect('/board')

def delete(request):
    no = request.GET['no']
    boardmodel.delete(no)
    return HttpResponseRedirect('/board')