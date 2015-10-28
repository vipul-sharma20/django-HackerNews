"""
Django settings for project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_ROOT = BASE_DIR
MEDIA_URL = '/media/'
"""LOGIN_EXEMPT_URLS = (
                    r'^accounts/auth/$',
                    r'^accounts/register/$',
                    r'^accounts/articles/$',
                    r'^index/$',
                    r'^admin/$',
                    r'^accounts/invalid/$',
                    r'^me/$',
                    r'^accounts/articles/comments/newest/$',
	            r'^$',
                    )
"""

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#6y$6e170xn@py=kr6zi5$zws6^j*@ljg1-=*zu+v(cmy$17c4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/accounts/loggedin'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'app',
    'south',
)

SITE_ID = 1
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.backends.ModelBackend',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'project.middleware.LoginRequiredMiddleware',
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
            'default': dj_database_url.config(
            default='sqlite:////{0}'.format(os.path.join(BASE_DIR, 'db.sqlite3'))
                            )
            }
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
FACEBOOK_APP_ID='1545038315730349'
FACEBOOK_API_SECRET='e1ce1160ff18ce8b29a6a96542577c3c'

GOOGLE_OAUTH2_CLIENT_ID = '449110994783-k01sqs6399080jt8lno3vl4b560ulv81.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = '2gOf_ZOjMyPXDQ50C47MuGZn'
GOOGLE_WHITE_LISTED_DOMAINS = ['incuna.com']
SOCIAL_AUTH_USER_MODEL = 'auth.User'

STATICFILES_DIRS = (BASE_DIR+'/static',)
STATIC_ROOT = BASE_DIR+'/collectstatic/'
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
