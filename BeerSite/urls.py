from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'BeerSite.views.home', name='home'),
    url(r'search/', 'BeerSite.views.search', name='search'),
    url(r'brewer/(?P<brewer_name>.+)', 'BeerSite.views.brewers', name='brewers'),
    url(r'morelikethis/(?P<id>\d+)', 'BeerSite.views.morelikethis', name='morelikethis'),
    # url(r'^BeerSite/', include('BeerSite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
