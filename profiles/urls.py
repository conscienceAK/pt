from django.conf.urls.defaults import *
from pt.profiles.models import CustomUser 
from django.contrib.auth.models import User


info_dict = {
    'queryset': CustomUser.objects.all(),
}

urlpatterns = patterns('',
    (r'^', 'django.views.generic.list_detail.object_list', info_dict),
    (r'^/(?P<object_id>\d+)/', 'django.views.generic.list_detail.object_detail', info_dict),
)

