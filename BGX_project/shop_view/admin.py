from django.contrib import admin
from shop_view.models import GoodsDetail, GoodsKind
# Register your models here.

class GoodsDetailAdmin(admin.ModelAdmin):
    pass
class GoodsKindAdmin(admin.ModelAdmin):
    pass
admin.site.register(GoodsDetail, GoodsDetailAdmin)
admin.site.register(GoodsKind, GoodsKindAdmin)