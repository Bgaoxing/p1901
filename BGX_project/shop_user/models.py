from django.db import models
from django.contrib.auth.models import AbstractUser
from shop_view.models import GoodsKind, GoodsDetail
from django.utils.timezone import now

# Create your models here.
class MyUsers(AbstractUser):
    pass


class UserGoodsComment(models.Model):
    user = models.ForeignKey(MyUsers, verbose_name='评论商品的用户')
    goods = models.ForeignKey(GoodsDetail, verbose_name='被评论的商品')
    context = models.TextField(verbose_name='评论的内容', max_length=2000)
    time = models.DateTimeField(verbose_name='评论的时间', default=now)
    # 一个用户只能对一件商品评论一次
    class Mate:
        unique_together = ('user', 'goods')

    def __str__(self):
        return '{}:评论:{}'.format(self.user.username, self.goods.title)