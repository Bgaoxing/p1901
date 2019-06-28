from django.db import models
from django.contrib.auth.models import AbstractUser
from movie_views.models import MovieKind, MovieDetail

from django.utils.timezone import now

# Create your models here.

class MyUsers(AbstractUser):
    pass

class UserMovieComment(models.Model):
    user = models.ForeignKey(MyUsers, verbose_name='评论电影的用户')
    movie = models.ForeignKey(MovieDetail, verbose_name='被评论的电影')
    context = models.TextField(verbose_name='评论的内容', max_length=2000)
    time = models.DateTimeField(verbose_name='评论的时间', default=now)
    # 一个用户只能对一部电影评论一次
    class Mate:
        unique_together = ('user', 'movie')

    def __str__(self):
        return '{}:评论:{}'.format(self.user.username, self.movie.title)