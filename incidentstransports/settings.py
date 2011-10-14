# Django settings for IncidentRATP project.
import os
                       
#==============================================================================
# Generic Django project settings
#==============================================================================

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()

# django project root, automatically adapt to your on plateform
DJANGO_ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DJANGO_ROOT_PATH + '/db/db.sqlite',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}                   

# setting up cache :
CACHE_BACKEND = 'locmem://'

# and session handling 
SESSION_ENGNE = "django.contrib.sessions.backends.cache"

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'c%xt_h0yhy)n*q0xnmdm_db7qo%92$d&lnht&*kvbkxcy5^na5'

TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'fr-FR'    

SITE_ID = 1
USE_I18N = True
USE_L10N = True

#==============================================================================
# Project URLS and media settings
#==============================================================================

ROOT_URLCONF = 'appartinfo.conf.urls'
                                              
# auth property to associate profile to Users :
AUTH_PROFILE_MODULE = 'accounts.UserProfile'
LOGIN_URL = '/accounts/login/'                
            
# adding auth backends to use with the social-auth
AUTHENTICATION_BACKENDS = (            
    'accounts.backends.HashBasedAuthentificationBackend',  
	'accounts.backends.EmailBasedAuthentificationBackend',
	'django.contrib.auth.backends.ModelBackend',
    'social_auth.backends.twitter.TwitterBackend', 
    'social_auth.backends.facebook.FacebookBackend',
)        

LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/'

MEDIA_URL = '/uploads/'
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(VAR_ROOT, 'static')
#MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, PROJECT_MODULE_NAME, 'static'),
)
                  
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"   

#==============================================================================
# Logging with Sentry
#==============================================================================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'DEBUG',
            'class': 'raven.contrib.django.logging.SentryHandler',
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

#==============================================================================
# Templates
#==============================================================================

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, PROJECT_MODULE_NAME, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
    # 'Custom context processors here',
)         

TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',
					'django.template.loaders.app_directories.Loader')

SOCIAL_AUTH_COMPLETE_URL_NAME  = 'complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'associate_complete'

#==============================================================================
# Middlewares
#==============================================================================

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)     

#==============================================================================
# Tests Runner
#==============================================================================
TEST_RUNNER = 'tests.run_tests'   

#==============================================================================
# Project Apps
#==============================================================================

               
PROJECT_APPS = (             
	'frontend',
	'api',
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
	'basic.blog',
	'basic.inlines',
	'basic.tools',
	'tagging',
	'django.contrib.markup',
	'django.contrib.comments',
    'nexus',
    'gargoyle',
    'sentry',
    'raven.contrib.django',
) + PROJECT_APPS