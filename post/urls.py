from django.conf.urls import patterns
from django.conf.urls import url

from openstack_dashboard.dashboards.forum.post.views \
    import IndexView, AddPostView, PostsIndexView

urlpatterns = patterns(
    '',
    url(r'^$', PostsIndexView.as_view(), name='index'),
    url(r'^add', AddPostView.as_view(), name='add'),
)
