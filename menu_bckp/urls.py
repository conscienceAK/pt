from django.conf.urls.defaults import *
from pt.menu.models import Menu, Info 
from django.contrib.auth.models import User

info_dict = {
    'queryset': Menu.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', dict(info_dict, template_name='base1.html'), name='Menu_item'),
    (r'^/content/(?P<object_id>\d+)/', 'django.views.generic.list_detail.object_detail', info_dict),
)

