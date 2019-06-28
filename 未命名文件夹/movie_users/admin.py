from django.contrib import admin
from movie_users.models import UserMovieComment

# Register your models here.

class UserMovieCommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserMovieComment, UserMovieCommentAdmin)