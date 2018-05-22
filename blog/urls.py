
from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index,name='blog_index'),
    url(r'^(?P<blog_id>[0-9]+)/$', views.detail,name='blog_detail'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.catagory,name='blog_category'),
    url(r'^tag/(?P<tag_id>[0-9]+)/$', views.tag,name='blog_tag'),
    url(r'^search/$', views.search,name='blog_search'),
    url(r'^archives/(?P<year>[0-9]+)/(?P<month>[0-9]+)$', views.archives, name='blog_archives'),
    url(r'^reply/(?P<comment_id>\d+)/$', views.reply, name='comment_reply'),
]
