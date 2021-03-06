# Import global settings to make it easier to extend settings. 
from django.conf.global_settings import *
import os
                       
#==============================================================================
# Generic Django project settings
#==============================================================================

ADMINS = ()

# django project root, automatically adapt to your on plateform
PROJECT_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

MANAGERS = ADMINS

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

ROOT_URLCONF = 'incidentstransports.conf.urls'
                                              
# auth property to associate profile to Users :
#AUTH_PROFILE_MODULE = 'accounts.UserProfile'
LOGIN_URL = '/accounts/login/'                
            
# adding auth backends to use with the social-auth
AUTHENTICATION_BACKENDS = (            
    'django.contrib.auth.backends.ModelBackend',
    'social_auth.backends.twitter.TwitterBackend', 
    'social_auth.backends.facebook.FacebookBackend',
)        

LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/'

MEDIA_URL = '/uploads/'
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_ROOT_PATH, 'public', 'static')
                   
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT_PATH, 'static'),
)
                  
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"   
#==============================================================================
# Logging with sentry
#==============================================================================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.handlers.SentryHandler',
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
        }
    },
}
#==============================================================================
# Templates
#==============================================================================

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT_PATH, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
    "django.core.context_processors.request",
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
    'maintenancemode.middleware.MaintenanceModeMiddleware',  
    'django_sorting.middleware.SortingMiddleware', 
    'pagination.middleware.PaginationMiddleware',
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
    # django basic auth system
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # and adding django-social-auth app
    'social_auth',
    # sessions, sites, and messages
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',    
    'django.contrib.humanize',  
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',   
    # django admin
    'django.contrib.admin',
    # admin
    'nexus',
    # feature switch
    'gargoyle',     
    #sentry
    #'sentry',
    'raven.contrib.django',
    # database migration tool
    'south',   
    #django registration app
    'registration',   
    # piston rest api
    'piston',
    'maintenancemode',  
    'django_sorting',
    'pagination',
) + PROJECT_APPS            