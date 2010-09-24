# Create your views here.

from django.views.generic.list_detail import object_list

from models import Info

#def info_list(request, object_id, **kwargs):
#	queryset=Info.objects.filter(pk=object_id)
#   	return object_list(request, queryset=queryset, template_object_name='main_cont.html', **kwargs)
    
def list(request, info_id):
    queryset=Info.objects.filter(pk=info_id)
    return object_list(request, dict(queryset, template_name='main_cont.html'))


