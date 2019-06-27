from django.db import models

# Create your models here.
# class GoodsKind(models.Model):
#     """
#     商品信息
#     """
#     name = models.CharField(max_length=255, verbose_name='商品名称')
#     desc = models.CharField(max_length=255, verbose_name='电影类型的描述')
#
#     def __str__(self):
#         return self.name
class GoodsKind(models.Model):
    name = models.CharField(max_length=255, verbose_name='商品类型')
    desc = models.CharField(max_length=255, verbose_name='商品类型的描述')

    def __str__(self):
        return self.name


# class GoodsPrice(models.Model):
#     price = models.CharField(max_length=1000, verbose_name='商品价格')


    # def __str__(self):
    #     return self.price

class GoodsDetail(models.Model):
    title = models.CharField(max_length=255, verbose_name='商品名称', unique=True)
    desc = models.CharField(max_length=1000, verbose_name='商品价格')
    id = models.ImageField

    #upload_to表示把图片上传到哪
    img = models.ImageField(upload_to='goods', null=True, default=None, blank=True)
                                                # 表示可以不传，默认为空

    kind = models.ManyToManyField(GoodsKind)
    #多对多

    def __str__(self):
        return self.title

