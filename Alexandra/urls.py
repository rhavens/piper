from django.conf.urls import patterns , url
from Alexandra import views

urlpatterns = patterns ( '',
    url(r'^$', views.index, name = 'index' ),
    url(r'^posts/', views.posts, name = 'posts'),
    url(r'^new_post/', views.new_post, name = 'new_post'),
    )
