from incidentstransports.conf.settings import *
           
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()

# django project root, automatically adapt to your on plateform
PROJECT_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
                                                

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': PROJECT_ROOT_PATH + '/db/db.sqlite',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}                                

# for debug toolbar
INTERNAL_IPS = ('127.0.0.1',)
                   
# serving static local file :
DJANGO_STATIC_MEDIA_URL = '/static/'        
          
JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.with_coverage',
    'django_jenkins.tasks.django_tests',
    'django_jenkins.tasks.run_pep8', 
    'django_jenkins.tasks.run_pyflakes' ,
	'django_jenkins.tasks.run_sloccount',
)

# adding debug toolbar :
DEBUG_TOOLBAR_CONFIG = { 'INTERCEPT_REDIRECTS': False }
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)                                               
INSTALLED_APPS += ('debug_toolbar', )
