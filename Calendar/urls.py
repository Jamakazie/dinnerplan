from django.conf.urls import patterns, url

from Calendar import views

urlpatterns = patterns('',
	url(r'^$', views.calendar_index, name='calendar_index'),
	url(r'^add$', views.calendar_add, name='calendar_addd'),
	url(r'^commit$', views.calendar_commit, name='calendar_commit'),
	url(r'^view$', views.calendar_view, name='calendar_view'),
)
