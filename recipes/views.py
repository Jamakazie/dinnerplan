from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
def recipe_index(request):
	context = {}
	return render_to_response('recipe_index.html', context, context_instance = RequestContext(request))

def recipe_save(request):
	context = {}
	return render_to_response('recipe_save.html', context, context_instance = RequestContext(request))

def recipe_view(request):
	context = {}
	return render_to_response('recipe_view.html', context, context_instance = RequestContext(request))
