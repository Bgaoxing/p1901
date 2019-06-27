"""BGX_project URL Configuration

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
from shop_view.views import index, about, contact, delivery, news, index1, register
from shop_user.views import user_register
from BGX_project.settings import STATIC_ROOT, MEDIA_ROOT,BASE_DIR
from django.views.static import serve
from shop_view.views import login, search


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', index, name='index'),
    url(r'^about/$', about, name='about'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^delivery/$', delivery, name='delivery'),
    url(r'^news/$', news, name='news'),

    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    url(r'^preview/(?P<goods_id>\d+)$', index1, name='single_log'),

    # url(r'^preview/$', preview, name='preview'),

    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
    url(r'^search/$', search, name='search'),
    #激活user里面的url
    url(r'^user/', include('shop_user.urls')),
    url(r'^api-auth/', include('rest_framework.urls'))

]
