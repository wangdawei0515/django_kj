from django.conf.urls import url
from . import views

urlpatterns =[
    # url(r'^$',views.index,{"switch":"true"}),
    url(r'^index2$',views.index_2),#浏览器的url中需要输入http://106.14.163.146:8000/books/index3才能访问的到，因为在主urls的hello_django中的urls中设置了拼接url
    url(r'^index3$',views.index_3),
    url(r'^article/$', views.article,name='books_article'),
    url(r'^article_new/$', views.article_new,name='books_article_new'),
    # url(r'^old/(?P<name1>\w+)/(?P<name2>\w+)/(?P<name3>\w+)/$', views.old,name='books_old'),#这种关键字传参的那么views.py文件中接收到的就是字典的形式
    url(r'^old/(\w+)/$', views.old,name='books_old'),#这种关键字传参的那么views.py文件中接收到的就是元组的形式
    # url(r'^new/(?P<name1>\w+)/(?P<name2>\w+)/(?P<name3>\w+)/$', views.new,name='books_new'),#这种位置传参的话views.py文件中接收的是字典形式
    url(r'^new/(\w+)/$', views.new,name='books_new'),#这种位置传参的话views.py文件中接收的是元组形式
    url(r'^url/(?P<urlcc>\w+)/$', views.index_4), #这里的urlcc这里的第三位参数是需要传参的，给到index.html文件中的{{ zheli }}变量中然后显示出来
    url(r'^mbbl/$', views.index_5),
    url(r'^glq/$', views.hello),
    url(r'^index33/(?P<name>\w+)/$', views.index33),
    url(r'^test/$',views.test,name='test'),
    url(r'^index6/$',views.index6),
    url(r'^index7/$',views.index7),
]