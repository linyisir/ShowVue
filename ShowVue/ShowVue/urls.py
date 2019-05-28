"""ShowVue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
import xadmin
from django.conf.urls import url, include
from django.views.static import serve
from django.conf import settings
# from goods.views_base import GoodsListView
from rest_framework.documentation import include_docs_urls
from goods.views import GoodsListView

urlpatterns = [
    url('xadmin/', xadmin.site.urls),
    url('ueditor/', include('DjangoUeditor.urls')),
    url('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^api-auth/', include('rest_framework.urls')),
    # 商品列表
    url(r'goods/$',GoodsListView.as_view(), name="good_list"),
    url(r'docs/', include_docs_urls(title='文档'))
]
