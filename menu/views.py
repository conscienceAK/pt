# Create your views here.

#from django.views.generic.list_detail import object_list
from django.shortcuts import render_to_response, get_object_or_404
from models import MenuItem, Info
from django.template import RequestContext

def m_list(request, m_id):
	#p = MenuItem.objects.filter(pk=m_id)
	mlist = MenuItem.objects.get(id=m_id) 
	return render_to_response('main_cont.html', {"m_list": mlist}, context_instance=RequestContext(request))

#def info_list(request, object_id, **kwargs):
#	queryset=Info.objects.filter(pk=object_id)
#   	return object_list(request, queryset=queryset, template_object_name='main_cont.html', **kwargs)
    
#def list(request, info_id):
#    queryset=Info.objects.filter(pk=info_id)
#    return object_list(request, dict(queryset, template_name='main_cont.html'))


