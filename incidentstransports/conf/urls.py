from django.conf.urls.defaults import patterns, url, include             
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
    url(r'^accounts/',                 include('registration.urls')), 
    url(r'^accounts/',                 include('social_auth.urls')),   
    url(r'^api/',                      include('api.urls')),
    url(r'^sentry/',                   include('sentry.web.urls')),
    url('^nexus/',                     include(nexus.site.urls)),
    url(r'^admin/',                    include(admin.site.urls)),
    url(r'^incidents/?$',              direct_to_template, {'template': 'incidents/incidents.html'},'incidents'),
    url(r'^contribuer/donation/?$',    direct_to_template, {'template': 'static/donate.html'}, 'contribute_donate'),
    url(r'^contribuer/twitter/?$',     direct_to_template, {'template': 'static/twitter.html'},'contribute_twitter'),
    url(r'^contribuer/?$',             direct_to_template, {'template': 'static/contribute.html'},'contribute'),
    url(r'^about/?$',                  direct_to_template, {'template': 'static/team.html'},'about'),   
    url(r'^stats/?$',                  direct_to_template, {'template': 'stats.html'}, 'stats'),
    url(r'^dev/iphone/?$',             direct_to_template, {'template': 'dev_iphone.html'}, 'dev_iphone'),
    url(r'^dev/android/?$',            direct_to_template, {'template': 'dev_android.html'}, 'dev_android'), 
    url(r'^dev/?$',                    direct_to_template, {'template': 'static/dev.html'}, 'dev'),
    url(r'^/?$',                       direct_to_template, {'template': 'index.html'}, "homepage"),     
)              
         
# frontend :
urlpatterns += patterns('frontend.views',                        
    url(r'^incident/add', 
        view='add_incident', 
        name='add_incident'),
    url(r'^incidents/(?P<scope>[a-z]*)', 
        view='get_incidents',
        name="get_incidents"),     
    # this one is deprecated :
    url(r'^incident/detail/(?P<incident_id>[0-9]*)/?$', 
        view='get_incident'),
    # this is the more SEO friendly version :
    url(r'^incident/detail/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<line_slug>[-\w]+)_(?P<line_id>[0-9]+)/(?P<incident_slug>[-\w]+)_(?P<incident_id>[0-9]+)/$',
            view='get_incident', 
            name='get_incident_url'),
    url(r'^i/disqus/(?P<id>[0-9]*)', 
        view='disqus_mobile', 
        name="disqus_mobile"),
    url(r'mu-86515d2e-482e5eb8-4a1262bb-ab3242ca/?$', view='load_test'),
    url(r'^archives/?$', 
        view='archives', 
        name="archives"),
)
# sitemap                                         
urlpatterns += patterns('',
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)               