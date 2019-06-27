from django.shortcuts import render, redirect
from django.http import HttpResponse
from shop_view.models import GoodsDetail
from shop_user.forms import UserLoginFrom, RegForm, SearchForm, UserGoodsCommentForm


# Create your views here.

def index(request):
    search_form = SearchForm()
    login_form = UserLoginFrom()
    register_form = RegForm()
    NEW_PRODUCTS = GoodsDetail.objects.filter(kind__name='new')
    FEATURE_PRODUCTS = GoodsDetail.objects.filter(kind__name='feature')

    data = GoodsDetail.objects.all().order_by('-id')
    data1 = GoodsDetail.objects.all().order_by('id')

    goods = data[1]
    goods1 = data1[1]
    return render(request, 'index.html',
                  {'hs': goods,
                   'hs1': goods1,
                   'new': NEW_PRODUCTS,
                   'feature': FEATURE_PRODUCTS,
                   'gg': data,
                   'gg1': data1,
                   'login_form': login_form,
                   "reg_form": register_form,
                   'search_form':search_form
                   })

def index1(request, goods_id):
    # pramary key
    # select * from xxxx
    # select * from xxx where pk=1
    # pk = parmary key=主键 = id

    try:
        goods = GoodsDetail.objects.filter(pk=goods_id)[0]

    except Exception:
        return HttpResponse("找不到")
    # login_form = UserLoginFrom()
    # register_form = RegForm()
    comment_form = UserGoodsCommentForm()
    CommentModel = UserGoodsCommentForm.Meta.model
    comments = CommentModel.objects.filter(goods_id=goods_id).order_by('-id')
    return render(request, 'preview.html', {#'login_form': login_form,
                                           #"reg_form": register_form,
                                           'goods': goods,
                                           "comment_form": comment_form,
                                           "comments": comments
                                             })


def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def delivery(request):
    return render(request, 'delivery.html')
def news(request):
    return render(request, 'news.html')

def test(request):
    # 只会生成语句
    data = GoodsDetail.objects.all()
    all_data = [i for i in data]

    # 切片才会执行语句
    return HttpResponse(data)
# def preview(request):
#     return render(request, 'preview.html')


def login(request):
    login_in = UserLoginFrom()

    return render(request, 'login.html', {'login_form': login_in})
def register(request):
    reg = RegForm()
    return render(request, 'register.html', {'reg': reg})

def search(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if not form.is_valid():
            return HttpResponse("请正确输入数据")
        data = form.cleaned_data

        goods = GoodsDetail.objects.values_list('id', 'title')
        for i in goods:
            if i[1] == data['content']:
                # if list(data['content'][:]) in list(i[i][:]):
                # print(i[1])
                #  print(2)
                # search_list = goods_detail.objects.values_list('name')
                # for j in search_list:
                #     if j[0] == data['content']:
                #         print(search_list)

                return redirect('/preview/{}'.format(i[0]))
        else:

            return redirect('/index/')



