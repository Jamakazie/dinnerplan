from django.conf.urls import patterns, url
from List import views

urlpatterns = patterns('',
	url(r'^$', views.list_index, name='list_index'),
	url(r'commit$', views.list_commit, name='list_commit'),
)
