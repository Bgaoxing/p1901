from django.shortcuts import render
from django.http import HttpResponse
from movie_users.forms import RegForm
from django.contrib.auth.hashers import make_password
from movie_users.models import MyUsers
# Create your views here.

def hello_world(request):
    return HttpResponse('<h1>hello world</h1>')

def hello_world2(request):
    with open('/Users/canvas/rimi_teaching/p1901/movies/templates/hello.html','r') as fp:
        msg = fp.read()
    return HttpResponse(msg)
def hello_world3(request):
    return render(request,'hello.html')

def test_login(reqeust):
    if reqeust.method == "GET":
        form = RegForm()
        return render(reqeust,"test1.html",{'form':form})
    if reqeust.method == "POST":
        form = RegForm(reqeust.POST)
        if not form.is_valid():
            return HttpResponse("请检查提交的参数")
        form.instance.password = make_password(form.instance.password)
        form.save()
        return HttpResponse('创建成功')

    return HttpResponse('非法请求操作')

def test_login1(reqeust):
    if reqeust.method == "GET":
        form = RegForm()
        return render(reqeust,"test1.html",{'form':form})

    if reqeust.method == "POST":
        form = RegForm(reqeust.POST)
        if not form.is_valid():
            return HttpResponse("请检查提交的参数")
        data = form.cleaned_data
        password = make_password(data['pwd'])
        try:
            MyUsers.objects.create(username=data["name"],password=password)
        except Exception:
            return HttpResponse("用户名已存在")

    return HttpResponse('非法请求操作')