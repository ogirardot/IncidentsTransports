from django.conf.urls.defaults import *             
from django.views.generic.simple import direct_to_template
from django.contrib.sitemaps import Sitemap
from django.contrib import admin           
import settings
import nexus
import gargoyle

admin.autodiscover()                       
nexus.autodiscover()
gargoyle.autodiscover()

# google sitemaps :
sitemaps = {
	#TODO
}

# handler404 :
handler404 = 'frontend.views.handler_404'

urlpatterns = patterns('', 
	(r'^accounts/', 				include('registration.urls')), 
	(r'^accounts/', 				include('social_auth.urls')),   
    (r'^api/', 						include('api.urls')),
    (r'^sentry/', 					include('sentry.web.urls')),
    ('^nexus/', 					include(nexus.site.urls)),
    (r'^admin/', 					include(admin.site.urls)),
    (r'^incidents/?$',				direct_to_template, {'template': 'incidents.html'},'incidents'),
    (r'^services/?$',				direct_to_template, {'template': 'services.html'},'services'),
    (r'^contribuer/donation/?$',	direct_to_template, {'template': 'contribute_donate.html'}, 'contribute_donate'),
    (r'^contribuer/twitter/?$',		direct_to_template, {'template': 'contribute_twitter.html'},'contribute_twitter'),
    (r'^contribuer/?$',				direct_to_template, {'template': 'contribute.html'},'contribute'),
    (r'^about/?$',  				direct_to_template, {'template': 'about.html'},'about'),   
	(r'^stats/?$',  				direct_to_template, {'template': 'stats.html'}, 'stats'),
    (r'^dev/iphone/?$', 			direct_to_template, {'template': 'dev_iphone.html'}, 'dev_iphone'),
	(r'^dev/android/?$',			direct_to_template, {'template': 'dev_android.html'}, 'dev_android'), 
    (r'^dev/?$', 					direct_to_template, {'template': 'dev.html'}, 'dev'),
	(r'^/?$', 						direct_to_template, {'template': 'index.html'}, "homepage"),     
)              
         
# frontend :
urlpatterns += patterns('frontend.views',                        
	url(r'^incident/add', 'add_incident', name='add_incident'),
    url(r'^incidents/(?P<scope>[a-z]*)', 'get_incidents'),
    url(r'^incident/detail/(?P<id>[0-9]*)/?$', 'get_incident'),
    url(r'^incident/action/(?P<id>[0-9]*)/(?P<action>[a-z]*)', 'incident_interact'),
    url(r'^i/disqus/(?P<id>[0-9]*)', 'disqus_mobile'),
    url(r'mu-86515d2e-482e5eb8-4a1262bb-ab3242ca/?$', 'load_test'),
)
# sitemap                                         
urlpatterns += patterns('',
	(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)               