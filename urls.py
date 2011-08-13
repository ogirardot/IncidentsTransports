from django.conf.urls.defaults import *  
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

urlpatterns = patterns('frontend.views',
    (r'^api/', include('api.urls')),
    (r'^sentry/', include('sentry.web.urls')),
    ('^nexus/', include(nexus.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^services/?$', 'services'),
    (r'^incidents/(?P<scope>[a-z]*)', 'get_incidents'),
    (r'^incidents/?$', 'incidents'),
    (r'^incident/add', 'add_incident'),
    (r'^incident/detail/(?P<id>[0-9]*)/?$', 'get_incident'),
    (r'^incident/action/(?P<id>[0-9]*)/(?P<action>[a-z]*)', 'incident_interact'),
    (r'^i/disqus/(?P<id>[0-9]*)', 'disqus_mobile'),
    (r'^contribuer/donation/?$', 'contribute_donate'),
    (r'^contribuer/twitter/?$', 'contribute_twitter'),
    (r'^contribuer/?$', 'contribute'),
    (r'^dev/iphone/?$', 'dev_iphone'),
	(r'^dev/android/?$', 'dev_android'), 
	(r'^blog/', include('basic.blog.urls')),
	(r'^comments/', include('django.contrib.comments.urls')),
    (r'^about/?$', 'about'),   
    (r'^home/?$', 'index'),
	(r'^stats/?$', 'stats'),
    (r'^dev/?$', 'dev'),
    (r'mu-86515d2e-482e5eb8-4a1262bb-ab3242ca/?$', 'load_test'),
    (r'^/?$', 'index'),
)                                                       
urlpatterns += patterns('',
	(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)

#local urls for serving media files during development
if settings.LOCAL_DEVELOPMENT:
    urlpatterns += patterns("django.views",
        url(r"%s(?P<path>.*)/$" % settings.MEDIA_URL[1:], "static.serve", {
            "document_root": settings.MEDIA_ROOT,
        })
    )
