from django.conf.urls import url
from django.views.generic import ListView, DateDetailView
from django.urls import path

from blog.models import Post

from blog.views.renderallposts import RenderallpostsView


app_name = 'blog'


urlpatterns = [
    path('renderallposts/', RenderallpostsView.as_view(), name='renderallposts'),
    url(r'^$', ListView.as_view(model=Post, paginate_by=3), name='post-list'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        DateDetailView.as_view(date_field="publish", model=Post),
        name='post-detail')
]
