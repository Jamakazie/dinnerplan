from django.shortcuts import render, render_to_response
import json
from django.http import HttpResponse
from django.template import RequestContext
from List.models import List as l

# Create your views here.
def list_index(request):
	context = {}
	if len(l.objects.all()) > 0:
		list_item = l.objects.all()[0]
		context['grocerylist'] = json.loads(list_item.items)
	return render_to_response('list_index.html', context, context_instance=RequestContext(request))

def list_commit(request):
	list_names = request.POST.getlist('list_name')
	list_quants = request.POST.getlist('list_quant')
	items = []
	for index, val in enumerate(list_names):
		items.append({list_names[index] : list_quants[index]})
	items = json.dumps(items)
	if len(l.objects.all()) != 0:
		list_item = l.objects.all()[0]
		list_item.items=items
	else:
		list_item = l(items=items)
	list_item.save()
	return HttpResponse("Success")
