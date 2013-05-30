from django.conf.urls import patterns, url

from recipes import views

urlpatterns = patterns('',
	url(r'^$', views.recipe_index, name='recipe_index'),
	url(r'^save$', views.recipe_save, name='recipe_save'),
	url(r'^view$', views.recipe_view, name='recipe_view'),
)
