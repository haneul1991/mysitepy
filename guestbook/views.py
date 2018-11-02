from django.db.models import F
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from guestbook import models
from guestbook.models import Guestbook


def list(request):
    guestbook_list = Guestbook.objects.all().order_by('-reg_date')

    data = {'guestbook_list':guestbook_list}
    return render(request, 'guestbook/list.html',data)

def add(request):
    guestbook = Guestbook()

    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.data = request.POST['content']

    guestbook_list = Guestbook.objects.all()
    guestbook.no = len(guestbook_list) + 1

    guestbook.save()

    return HttpResponseRedirect('/guestbook/list')

def deleteform(request):

    id = request.GET['id']
    data = {'id' : id}

    return render(request,'guestbook/deleteform.html', data)


def delete(request):
    password = request.POST['password']

    messages = Guestbook.objects.filter(id=request.POST['id'],password=password)


    messages.delete()

    return HttpResponseRedirect('/guestbook/list')






def ajax(request):
    return render(request,'guestbook/ajax.html')


def api_list(request):
    p = request.GET['p']
    page = (int(p)-1) * 5
    newlist = []
    results = Guestbook.objects.all()[page:page+5]
    quest = results.values()
    for a in quest:
        newlist.append(a)
    response = {'result' : 'ok', 'data' : newlist}
    return JsonResponse(response)

def api_add(request):
    name = request.GET['name']
    password = request.GET['password']
    message = request.GET['message']

    no = models.insert((name, password, message))

    response = {'result' : 'success', 'data' : no}
    return JsonResponse(response)

