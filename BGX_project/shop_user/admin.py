from django.contrib import admin
from shop_user.models import UserGoodsComment

# Register your models here.

class UserGoodsCommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserGoodsComment, UserGoodsCommentAdmin)