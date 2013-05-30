from django.shortcuts import render, render_to_response
import datetime
from django.http import HttpResponse
from django.template import RequestContext
from recipes.models import recipe as r
from Calendar.models import CalendarObject as c

# Create your views here.
def calendar_index(request):
	context = {}
	return render_to_response('calendar_index.html', context, context_instance = RequestContext(request))

def calendar_add(request):
	recipes = r.objects.all()
	context = {}
	context['recipes'] = recipes
	return render_to_response('calendar_add.html', context, context_instance = RequestContext(request))

def calendar_commit(request):
	r_id = name_to_id(request.POST['calendar_recipe'])
	date = request.POST['calendar_date']
	temp = datetime.datetime.strptime(date, '%m/%d/%Y')
	date = temp.strftime('%Y-%m-%d')
	cal_object = c.objects.filter(date=date)
	if(len(cal_object) > 0):
		cal = cal_object[0]
		cal.recipe_id = r_id
	else:
		cal = c(date=date, recipe_id=r_id)
	cal.save()
	return HttpResponse("Success")

def calendar_view(request):
	start_date = datetime.datetime.now()
	end_date = start_date + datetime.timedelta(days=7)
	events = c.objects.filter(date__range=[start_date, end_date])
	for event in events:
		event.recipe_id = id_to_name(event.recipe_id)
	context = {}
	context['events'] = events
	return render_to_response('calendar_view.html', context, context_instance = RequestContext(request)) 

def name_to_id(name):
	recipe = r.objects.filter(title=name)[0]
	return recipe.pk
def id_to_name(rid):
	recipe = r.objects.filter(pk=rid)[0]
	return recipe.title
