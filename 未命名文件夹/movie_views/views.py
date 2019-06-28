from django.shortcuts import render
from django.http import HttpResponse
from movie_views.models import MovieDetail
from movie_users.forms import UserLoginFrom, RegForm, UserMovieCommentForm


# Create your views here.

def index(request):
    login_form = UserLoginFrom()
    register_form = RegForm()
    featured_movies = MovieDetail.objects.filter(kind__name='fd')
    top_viewed_movies = MovieDetail.objects.filter(kind__name='tv')
    top_rating_movies = MovieDetail.objects.filter(kind__name='tr')
    recently_add_movies = MovieDetail.objects.filter(kind__name='ra')
    data = MovieDetail.objects.all().order_by('-id')
    return render(request, 'index.html',
                  {"movies": data,
                   'fd': featured_movies,
                   'tv': top_viewed_movies,
                   'tr': top_rating_movies,
                   'ra': recently_add_movies,
                   'login_form': login_form,
                   "reg_form": register_form,
                   'Featured': data
                   })


def index1(request, movie_id):
    # pramary key
    # select * from xxxx
    # select * from xxx where pk=1
    # pk = parmary key=主键 = id

    try:
        movie = MovieDetail.objects.filter(pk=movie_id)[0]
    except Exception:
        return HttpResponse("找不到")
    login_form = UserLoginFrom()
    register_form = RegForm()
    comment_form = UserMovieCommentForm()
    CommentModel = UserMovieCommentForm.Meta.model
    comments = CommentModel.objects.filter(movie_id=movie_id).order_by('-id')
    return render(request, 'single.html', {'login_form': login_form,
                                           "reg_form": register_form, 'movie': movie, "comment_form": comment_form,
                                           "comments": comments})


def test(request):
    # 只会生成语句
    data = MovieDetail.objects.all()
    all_data = [i for i in data]

    # 切片才会执行语句
    return HttpResponse(data)