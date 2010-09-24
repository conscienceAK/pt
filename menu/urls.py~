from django.conf.urls.defaults import *
from pt.menu.models import News, Info 
from django.contrib.auth.models import User

info_dict = {
    'queryset': News.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', dict(info_dict, template_name='main.html')),
    (r'^/content/(?P<object_id>\d+)/', 'django.views.generic.list_detail.object_detail', dict(info_dict, template_name='detail.html')),
    (r'^/news/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', dict(info_dict, template_name='detail.html')),
)

