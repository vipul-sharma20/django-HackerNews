from django.conf.urls import patterns, include, url
import app.views
from django.contrib import admin
from django.contrib.auth.decorators import login_required as auth
from django.conf import settings
from django.conf.urls.static import static
from app.views import  UserProfileDetailView, UserProfileEditView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'app.views.article_view'),
    url(r'^contact/', include('app.urls')),
    url(r'^accounts/login/$', 'app.views.login', name='login'),
    url(r'^accounts/auth/$', 'app.views.auth_view'),
    url(r'^accounts/logout/$', 'app.views.logout'),
    url(r'^accounts/invalid/$', 'app.views.invalid_login'),
    url(r"^accounts/", include("registration.backends.simple.urls")),
    url(r'^personal/$', app.views.personal_info, name='personal',),
    url(r'^user/$', auth(UserProfileEditView.as_view()), name='edit_profile'),
    url(r'^users/(?P<slug>\w+)/$', auth(UserProfileDetailView.as_view()), name='profile'),
    url(r'^users/(?P<slug>\w+)/submissions/$', 'app.views.get_submissions'),
    url(r'^users/(?P<slug>\w+)/comments/$', 'app.views.get_comments'),
    url(r'^', include('app.urls')),
    url(r'^accounts/post/$', 'app.views.post_article_view'),
    url(r'^accounts/articles/$', 'app.views.article_view'),
    url(r'^accounts/articles/like/(?P<article_id>\d+)/$', 'app.views.like_article'),
    url(r"^accounts/articles/comments/(?P<article_id>\d+)/$", "app.views.add_comment"),
    url(r'^accounts/news/(?P<news_id>\d+)/$', 'app.views.newscontent'),
    url(r'accounts/articles/comments/newest/$', 'app.views.recent_comarticles'),
    url(r'accounts/news/$', 'app.views.news'),
    url(r'^me/$', 'app.views.myself'),
    url(r'^$', 'app.views.article_view'),
    url(r'', include('social_auth.urls')),

    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
