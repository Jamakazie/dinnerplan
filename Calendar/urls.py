from django.conf.urls import patterns, url

from Calendar import views

urlpatterns = patterns('',
	url(r'^$', views.calendar_index, name='calendar_index'),
)
