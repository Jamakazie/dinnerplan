from django.conf.urls import patterns, url

from Calendar import views

urlpatterns = patterns('',
	url(r'^$', views.calendar_index, name='calendar_index'),
	url(r'^add$', views.calendar_add, name='calendar_add'),
	url(r'^add/getrecipe$', views.calendar_ajax_getrecipe, name='calendar_ajax_getrecipe'),
	url(r'^commit$', views.calendar_commit, name='calendar_commit'),
	url(r'^view$', views.calendar_view, name='calendar_view'),
	url(r'^grocerylist$', views.calendar_grocery_list, name='calendar_grocery_list'),
	url(r'^grocerylist/generate$', views.calendar_ajax_grocerylist, name='calendar_ajax_grocerylist'),
)
