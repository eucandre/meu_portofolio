from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$','app_portofolio.views.portofolio'),
    #(r'^login/$',"django.contrib.auth.views.login",{"template_name":"paginas_do_sistema/login.html"}),
    #(r'^logout/$',"django.contrib.auth.views.logout_then_login",{"login_url":"/login/"}),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }))
