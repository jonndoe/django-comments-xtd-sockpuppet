from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from blog.views.home import HomePageView


urlpatterns = [
    path(r'comments/', include('django_comments_xtd.urls')),
    path(r'admin/', admin.site.urls),
    path(r'blog/', include('blog.urls', namespace='blog')),
    path(r'', HomePageView.as_view(), name='homepage'),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
