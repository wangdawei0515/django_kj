"""hello_django URL Configuration

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
from django.conf.urls import include,url
from django.contrib import admin
from books import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/python/$', views.hello_python),
    url(r'^hello/php/$', views.hello_php),
    url(r'^hello/(\w+)/$',views.hello_course),
    #下面的是位置参数，url中的参数也需要2个
    url(r'^add/(\d+)/(\d+)/$', views.add),
    #这里的name和num是关键字参数，所以名字要和views.hello_django的name、num一致
    url(r'^hello/(?P<name>\w+)/(?P<num>\d+)$',views.hello_django),   #使用关键字参数时前面要加 ?P 他们是一个组合，不要问为什么？因为这个是固定语法
    url(r'^books/',include('books.urls')),   #这里是url拼接方式 XXX.XXX.XXX.XXX:8000/books/<再加books.urls.py文件中的url，如：index2>
    #访问方式如：http://106.14.163.146:8000/books/index2
    url(r'^blog/',include('blog.urls')),
]

