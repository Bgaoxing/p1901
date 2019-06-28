from django.conf.urls import url
from movie_users.views import get_login,user_login,user_logout,user_register, user_comment
urlpatterns = [
    url(r'^test/login$',get_login,name='test_login'),
    url(r'^login$',user_login,name='user_login'),
    url(r'^logout$',user_logout,name='user_logout'),
    url(r'^register$',user_register,name='user_register'),
    url(r"^comment/(?P<movie_id>\d+)$", user_comment, name="user_comment")

]