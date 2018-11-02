from django.db.models import F, Max
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from board.models import Board
from user.models import User

def list(request):
    if request.method == 'GET':
        board_list = Board.objects.all().order_by('-id')

        data = {'board_list':board_list}
        return render(request, 'board/list.html', data)

def write(request):

    board_write = Board.objects.all().order_by('-reg_date')

    data = {'board_write':board_write}
    return render(request, 'board/write.html',data)

def add(request):
    if request.method == 'POST':
        board = Board()

        board.name = request.session['authuser']['name']
        board.title = request.POST['title']
        board.content = request.POST['content']
        board_list = Board.objects.all()
        board.no = len(board_list) + 1

        g_no = Board.objects.aggregate(Max('group_no'))
        if (g_no['group_no__max'] == None):
            board.group_no = 1
        else:
            board.group_no = g_no['group_no__max'] + 1
        board.order_no = 1
        board.depth = 0



        board.save()

        return HttpResponseRedirect("/board/list")

def view(request):
    if request.method == 'GET':
        id = request.GET['id']
        results = Board.objects.get(id=id)
        data = {'board_list':results}
        results.hit += 1
        results.save()

        return render(request, 'board/view.html',data)

def modify(request):
    if request.method == 'GET':
        id = request.GET['id']
        results = Board.objects.get(id=id)
        data = {'board_data':results}

        return render(request, 'board/modify.html',data)

def update(request):
    if request.method == 'POST':
        id = request.GET['id']
        title = request.POST['title']
        content = request.POST['content']
        result = Board.objects.get(id=id)
        result.title = title
        result.content = content
        result.save()

        return HttpResponseRedirect('list')

def delete(request):

    content = Board.objects.get(id=request.GET['id'])
    content_no = content.no

    other_board = Board.objects.filter(no__gt=content_no)
    other_board.update(no=F('no') - 1)
    content.delete()

    return HttpResponseRedirect('/board/list')

def reply(request):
    if request.method == 'GET':
        id = request.GET['id']
        results = Board.objects.get(id=id)
        data = {'board_data': results}
        return render(request, 'board/reply.html',data)

def reple(request):
    new = Board()
    if request.method == 'POST':
        id = request.GET['id']
        board= Board.objects.get(id=id)
        new.group_no = board.group_no
        new.title = request.POST['title']
        new.content = request.POST['content']
        new.order_no = board.order_no + 1
        new.depth = board.depth + 1
        authuser = request.session['authuser']
        auth_username = authuser.get('name')
        auth_user_id = authuser.get('id')
        new.user_name = auth_username
        new.user_id = auth_user_id
        new.save()

    return HttpResponseRedirect("/board/list")