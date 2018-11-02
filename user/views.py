from django.forms import model_to_dict
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from user.models import User


def joinform(request):
    return render(request, 'user/joinform.html')

def join(requset):
    user = User()
    user.name = requset.POST['name']
    user.email = requset.POST['email']
    user.password = requset.POST['password']
    user.gender = requset.POST['gender']

    #models.insert((name, email, password, gender))
    user.save()

    return HttpResponseRedirect('/user/joinsuccess')

def joinsuccess(requset):
    return render(requset, 'user/joinsuccess.html')

def loginform(request):
    return render(request, 'user/loginform.html')

def login(requset):
    # user = models.get(email, password)

    results = User.objects.filter(email=requset.POST['email']).filter(password=requset.POST['password'])

    # 로그인 실패
    if len(results) == 0:
        return HttpResponseRedirect('/user/loginform?results=fail')

    # 로그인 성공(처리)
    authuser = results[0]
    requset.session['authuser'] = model_to_dict(authuser)

    # main으로 리다이렉트
    return HttpResponseRedirect('/')

def logout(request):
    del request.session['authuser']
    return HttpResponseRedirect('/')

def modifyform(request):
    authuser = request.session['authuser']
    data = {'user' : authuser}
    return render(request, 'user/modifyform.html', data)

def checkemail(request):
    results = User.objects.filter(email=request.GET['email'])

    result = {'result' : len(results) == 0} # true : not exist(사용가능)
    return JsonResponse(result)

def modify(request):
    authuser = request.session['authuser']
    auth = User.objects.get(id=authuser.get('id'))
    auth.password = request.POST['password']
    auth.gender = request.POST['gender']
    auth.save()

    return HttpResponseRedirect('/')