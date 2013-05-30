from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
def calendar_index(request):
	context = {}
	return render_to_response('calendar_index.html', context, context_instance = RequestContext(request))
