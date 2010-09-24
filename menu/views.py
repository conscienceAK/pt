# Create your views here.

#from django.views.generic.list_detail import object_list
from django.shortcuts import render_to_response, get_object_or_404
from models import *

def submenu_list(request, object_id)
	p = ger_object_or_404(MenuItem, order=object_id)
	list = get_object_or_404(Info, menu_item=p)
	return render_to_response('main_cont.html', {'submenu_list': list})

#def info_list(request, object_id, **kwargs):
#	queryset=Info.objects.filter(pk=object_id)
#   	return object_list(request, queryset=queryset, template_object_name='main_cont.html', **kwargs)
    
#def list(request, info_id):
#    queryset=Info.objects.filter(pk=info_id)
#    return object_list(request, dict(queryset, template_name='main_cont.html'))


