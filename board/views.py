from django.http import HttpResponse, HttpResponseRedirect
import board.models as boardmodel
from django.shortcuts import render

def index(request):
    totalcount = boardmodel.fetchlistcount()
    countpage = 10
    maxpage = boardmodel.maxpage(totalcount, countpage)
    page = int(request.GET['page'])
    startcount = (page - 1) * countpage + 1
    endcount = page * countpage
    results = boardmodel.fetchlist(startcount, endcount)
    data = {'boardlist':results}
    data['maxpage'] = maxpage
    data['page'] = page
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
    return HttpResponseRedirect('/board?page=1')

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
    try:
        if data['board']['user_no'] == request.session['auth']['no']:
            return render(request, 'board/modifyform.html', data)
        else:
            return HttpResponseRedirect('/board?page=1')
    except KeyError as e:
        return HttpResponseRedirect('/board?page=1')


def modify(request):
    no = request.GET['no']
    title = request.POST['title']
    content = request.POST['content']
    boardmodel.updateboard(title, content, no)
    return HttpResponseRedirect('/board?page=1')

def replyform(request):
    no = request.GET['no']
    results = boardmodel.fetchonebynore(no)
    data = {'replylist': results}
    return render(request, 'board/replyform.html', data)

def reply(request):
    try:
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
        return HttpResponseRedirect('/board?page=1')
    except KeyError as e:
        return HttpResponseRedirect('/board?page=1')

def delete(request):
    no = request.GET['no']
    boardmodel.delete(no)
    return HttpResponseRedirect('/board?page=1')