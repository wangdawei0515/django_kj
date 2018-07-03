from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^add$',views.add_user),
    url(r'^del$',views.delete_user),
    url(r'^update$',views.update_user),
    url(r'^search$',views.search_user),
    url(r'^find$',views.find_Ftest),
    url(r'^add_info$',views.add_info),
    url(r'^search_info$',views.search_info),
    url(r'^$',views.blog_index,name="blog_index"),
    url(r'^blog_add$',views.blog_add,name="blog_add"),
    url(r'^blog_list$',views.blog_list,name="blog_list"),
    url(r'^blog_detail/(?P<blog_id>\d+)$',views.blog_detail,name="blog_detail"),
    # 这里的blog_id是关键字要和demo_list.html中<th><a href="{% url "blog_detail" blog_id=blog.id %}">{{ blog.title }}</a></th>这里的blog_id相同，
    # 以及views.py中blog_detail这个函数中的blog_id相同
    url(r'^blog_delete/(?P<blog_id>\d+)$',views.blog_delete,name="blog_delete"),
    url(r'^blog_edit/(?P<blog_id>\d+)$',views.blog_edit,name="blog_edit"),
    url(r'^get_add/$',views.get_add,name="get_add"),
    url(r'^get_index/$',views.get_index,name="get_index"),
    url(r'^post_index/$',views.post_add,name="post_index"),
    url(r'^get_test11/$',views.get_test11,name="get_test11"),
    url(r'^get_test22/$',views.get_test22,name="get_test22"),
    url(r'^cktest/$',views.ckTest,name="blog_cktest"),
    url(r'^w1/$',views.w1,name="blog_w1"),
    url(r'^w2/(?P<w2_id>\w+)/(?P<w2_name>\w+)/$',views.w2,name="blog_w2"),
    url(r'^home/$', views.home, name='blog_home'),
    url(r'^login/$', views.login, name='blog_login'),
    url(r'^logout/$', views.logout, name='blog_logout'),
    url(r'^register/$',views.register,name='blog_register'),

    ]