import json
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from recipes.models import recipe as r

# Create your views here.
def recipe_index(request):
	context = {}
	return render_to_response('recipe_index.html', context, context_instance = RequestContext(request))

def recipe_save(request):
	context = {}
	return render_to_response('recipe_save.html', context, context_instance = RequestContext(request))

def recipe_view(request):
	recipes = r.objects.all()
	context = {}
	context['recipes'] = recipes
	return render_to_response('recipe_view.html', context, context_instance = RequestContext(request))

def recipe_commit(request):
	
	title = request.POST['title'].strip()
	prep_time = request.POST['prep_time']
	cook_time = request.POST['cook_time']
	item_names = request.POST.getlist('item_name')
	item_quantites = request.POST.getlist('item_quantity')
	items = []
	for index, val in enumerate(item_names):
		items.append({item_names[index] : item_quantites[index]})
	
	recipe = r(title=title, prep_time = prep_time, cook_time=cook_time, ingredients = json.dumps(items))
	recipe.save()
	return HttpResponse("Success");

def recipe_view_specific(request, params):
	recipe = r.objects.get(pk=params)
	context = {}
	context['recipe'] = recipe
	context['ingredients'] = json.loads(recipe.ingredients)
	return render_to_response('recipe_view_specific.html', context, context_instance = RequestContext(request))
