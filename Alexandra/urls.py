from django.conf.urls import patterns , url
from Alexandra import views

urlpatterns = patterns ( '',
    url(r'^$', views.posts, name = 'index' ),
    url(r'^posts/', views.posts, name = 'posts'),
    url(r'^post/(?P<post_id>\d+)', views.post, name = 'post'),
    url(r'^new_post/', views.new_post, name = 'new_post'),
    )
