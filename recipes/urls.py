from django.conf.urls import patterns, url

from recipes import views

urlpatterns = patterns('',
	url(r'^$', views.recipe_index, name='recipe_index'),
	url(r'^save$', views.recipe_save, name='recipe_save'),
	url(r'^view$', views.recipe_view, name='recipe_view'),
	url(r'^view/(.*)$', views.recipe_view_specific, name='recipe_view_specific'),
	url(r'^edit/(.*)$', views.recipe_edit, name='recipe_edit'),
	url(r'^commit/edit$', views.recipe_edit_commit, name='recipe_edit_commit'),
	url(r'^commit$', views.recipe_commit, name='recipe_commit'),

)
