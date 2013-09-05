# -*- coding: utf-8 -*- 
# Django settings for skeleton project.
from os import path
DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_NAME = 'Skeleton'
FOOTER_INFO = 'Skeleton - David Michael Brown'
PROJECT_PATH = path.dirname(path.abspath(__file__))
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': path.join(PROJECT_PATH, '..', 'sqlite3.db'),                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = path.join(PROJECT_PATH, '..', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = path.join(PROJECT_PATH, 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '!5i(w&of0r+02#fa%@kk&3j%v6r7nv(9(!tefa1j01o05n)d&8'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'skeleton.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'skeleton.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    # suit process
    "django.core.context_processors.request",
    # skeleton process
    'skeleton.context_processors.project_name',
    'skeleton.context_processors.footer_info',
    # social auth process
    #'social_auth.context_processors.social_auth_by_name_backends',
    #'social_auth.context_processors.social_auth_backends',
    #'social_auth.context_processors.social_auth_by_type_backends',
    #'social_auth.context_processors.social_auth_login_redirect',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'suit',
    'django.contrib.admin',
    'social_auth',
    'disqus',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'skeleton',
    'projects',
    'profiles',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}





# django-social-auth settings
AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.contrib.disqus.DisqusBackend',
    #'social_auth.backends.contrib.linkedin.LinkedinBackend', 
    #'social_auth.backends.contrib.github.GithubBackend',
    'django.contrib.auth.backends.ModelBackend',

    )

TWITTER_CONSUMER_KEY         = 'S2kVYYW3ihDtPgOZg5Q'
TWITTER_CONSUMER_SECRET      = 'ERKZS7zBKQk36GjdNVpe9oMBCpRn0quho5K7tA0'
FACEBOOK_APP_ID              = '512028745545345'
FACEBOOK_API_SECRET          = '6977cd723c04c3f9dddcb6eadd1a02bf'
DISQUS_CLIENT_ID = 'dT2zAW0OIbyQC2OAs4CTEilrmA4O2pkSr7gO7kwVmonkpJSLgP1EPton3GE7vJDs'
DISQUS_CLIENT_SECRET = 'h2vZCFQO8A3277aN5xMEUHKpzxRStbj892rAZMQUpEcBgOl2X4dPWh0lgSsevGLS'

####base###
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT = '/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
#LOGIN_ERROR_URL
#SOCIAL_AUTH_USERNAME_FIXER
#####
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_FORCE_POST_DISCONNECT = True
SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['email',]

#disqus settings

DISQUS_API_KEY = 'h2vZCFQO8A3277aN5xMEUHKpzxRStbj892rAZMQUpEcBgOl2X4dPWh0lgSsevGLS'
DISQUS_WEBSITE_SHORTNAME = 'djangoskeleton'

######### TEMPLATE STUFF
#{% url "socialauth_begin" "backend-name" %}
#{% url "socialauth_disconnect" "backend-name" %}
#{% url "socialauth_disconnect_individual" "backend-name" backend-id %}
######

#LOGIN_URL          = '/login-form/'
#SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/another-login-url/'
#SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/account-disconnected-redirect-url/'
#SOCIAL_AUTH_BACKEND_ERROR_URL = '/new-error-url/'

#SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
#SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'