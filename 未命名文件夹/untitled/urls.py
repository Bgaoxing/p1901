"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from p1901_test.views import hello_world, hello_world2, test_login
from movie_views.views import index,test,index1
from django.views.static import serve
from untitled.settings import BASE_DIR, MEDIA_ROOT
import os

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', hello_world),
    url(r'^hello2/', hello_world2),
    url(r'^index/$', index),
    url(r'^test/', test_login, name="test"),
    url(r'^index/$', index, name='movie_index'),
    # http://0.0.0.0:8080/static/images/m11.jpg


    url(r'^static/(?P<path>.*)$', serve, {'document_root': os.path.join(BASE_DIR, 'static')}),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    url(r'^movie/(?P<movie_id>\d+)$', index1, name='single_log'),
    #激活user里面的url
    url(r'^user/', include('movie_users.urls')),
    url(r'^api-auth/', include('rest_framework.urls'))

]
