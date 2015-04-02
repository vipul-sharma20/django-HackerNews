from django.conf.urls import patterns, include, url
import contacts.views
from django.contrib import admin
from django.contrib.auth.decorators import login_required as auth
from django.conf import settings
from django.conf.urls.static import static
from contacts.views import  UserProfileDetailView, UserProfileEditView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'contacts.views.landing'),
    url(r'^contact/', include('contacts.urls')),
    url(r'^accounts/login/$', 'contacts.views.login'),
    url(r'^accounts/auth/$', 'contacts.views.auth_view'),
    url(r'^accounts/logout/$', 'contacts.views.logout'),
    #url(r'^accounts/loggedin/$', 'contacts.views.loggedin'),
    url(r'^accounts/invalid/$', 'contacts.views.invalid_login'),
    url(r"^accounts/", include("registration.backends.simple.urls")),
    #url(r'^accounts/register/complete/$', 'contacts.views.register_success'),
    url(r'^personal/$', contacts.views.personal_info, name='personal',),
    #url(r'^user/$', 'contacts.views.user_profile_edit'),
    url(r'^user/$', auth(UserProfileEditView.as_view()), name='edit_profile'),
    url(r'^users/(?P<slug>\w+)/$', auth(UserProfileDetailView.as_view()), name='profile'),
    url(r'^users/(?P<slug>\w+)/submissions/$', 'contacts.views.get_submissions'),
    url(r'^users/(?P<slug>\w+)/comments/$', 'contacts.views.get_comments'),
    url(r'^', include('contacts.urls')),
    url(r'^accounts/post/$', 'contacts.views.post_article_view'),
    url(r'^accounts/articles/$', 'contacts.views.article_view'),
    url(r'^accounts/articles/like/(?P<article_id>\d+)/$', 'contacts.views.like_article'),
    url(r"^accounts/articles/comments/(?P<article_id>\d+)/$", "contacts.views.add_comment"),
    url(r'^accounts/news/(?P<news_id>\d+)/$', 'contacts.views.newscontent'),
    url(r'accounts/articles/comments/newest/$', 'contacts.views.recent_comarticles'),
    url(r'accounts/news/$', 'contacts.views.news'),
    url(r'^me/$', 'contacts.views.myself'),
    url(r'^$', 'contacts.views.landing'),

    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
