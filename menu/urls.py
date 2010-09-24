from django.conf.urls.defaults import *
from pt.menu.models import News, Info 
from django.contrib.auth.models import User

news_dict = {
    'queryset': News.objects.all(),
}
info_dict = {
	'queryset': Info.objects.all(),
}

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list_detail.object_list', dict(news_dict, template_name='main.html')),
    url(r'^cont/(\d+)/list/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', dict(info_dict, template_name='detail_cont.html')),
    url(r'^news/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', dict(news_dict, template_name='detail.html')),
)

urlpatterns += patterns('',
    (r'^cont/(?P<object_id>\d+)/$', 'submenu_list'),
)
