from django.contrib import admin
from  movie_views.models import MovieDetail, MovieKind

# Register your models here.

class MovieDetailAdmin(admin.ModelAdmin):
    pass

class MovieKindAdmin(admin.ModelAdmin):
    pass
admin.site.register(MovieDetail, MovieDetailAdmin)
admin.site.register(MovieKind, MovieKindAdmin)