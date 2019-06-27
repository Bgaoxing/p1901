from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password, make_password
from shop_user.forms import UserLoginFrom, RegForm, UserGoodsCommentForm
from django.contrib.auth import login, logout
from shop_user.models import MyUsers
from copy import deepcopy

# Create your views here.
# def get_login(request):
#     if request.method == 'POST':
#         # try:
#         #     username = request.POST['username']
#         # if(len(username)< 15 )
#         # if(len(username)> 15 )
#         # if(len(username)> 15 )
#         # except Exception:
#         #     return HttpResponse('用户不存在')
#         #
#         # pwd = request.POST['pwd']
#         # if len(pwd) < 6:
#         #     return HttpResponse('密码至少6位'
#         #                         )
#         userlogin = UserLoginFrom(request.POST)
#         if not userlogin.is_valid():
#             return HttpResponse('无效')
#         data = userlogin.cleaned_data
#         # data =request.POST
#         user = MyUsers.objects.filter(username=data['name'])[0]
#         encode_pwd = user.password
#         is_true = False
#         # 123456 pbkdf2_sha256$36000$DhGGYrrD
#         if check_password(data['password'], encode_pwd):
#             is_true = True
#         if is_true:
#             login(request)
#             return HttpResponse('用户登录成功')
#         else:
#             return HttpResponse('密码错误')
#         # select * from user where pwd='asdasfdf'
#     else:
#         userlogin = UserLoginFrom()
#         return render(request, 'test.html', {'form': userlogin})

def user_login(request):
    if request.method == 'POST':
        #refer_url = request.META['HTTP_REFERER']
        userlogin = UserLoginFrom(request.POST)
        if not userlogin.is_valid():
            return HttpResponse('无效')
        data = userlogin.cleaned_data
        try:
            user = MyUsers.objects.filter(username=data['name'])[0]
        except Exception:
            return HttpResponse('用户不存在!')
        encode_pwd = user.password
        is_true = False
        if check_password(data['password'], encode_pwd):
            is_true = True
        if is_true:
            login(request, user)
            #return HttpRespone('用户登录成功')
            return redirect('/index/')
        else:
            return HttpResponse('密码错误')

def user_logout(request):
    refer_url = request.META['HTTP_REFERER']
    logout(request)
    return redirect(refer_url)

def user_register(request):
    form = RegForm(request.POST)
    if not form.is_valid():
        return HttpResponse("请检查提交的参数")
    form.instance.password = make_password(form.instance.password)
    user = form.save()
    login(request, user)
    # return HttpRespone('用户登录成功')
    # refer_url = request.META['HTTP_REFERER']
    return redirect('/index/')

def register(request):
    return render(request, 'register.html')



def user_comment(request, goods_id):
    refer_url = request.META['HTTP_REFERER']
    data = deepcopy(request.POST)
    try:
        data['user'] = request.user.pk
    except Exception:
        data['user'] = 0
    data['goods'] = goods_id
    res_data = UserGoodsCommentForm(data)
    if not res_data.is_valid():
        return redirect(refer_url)
    res_data.save()
    return redirect(refer_url)