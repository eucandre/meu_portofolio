from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$','app_portofolio.views.portofolio'),
    url(r'^mensagem/$','app_portofolio.views.dashboard'),
    url(r'^mensagem_contato/(?P<nr_item>\d+)$','app_portofolio.views.aconpanha'),
    (r'^login/$',"django.contrib.auth.views.login",{"template_name":"administrativo/login.html"}),
    (r'^logout/$',"django.contrib.auth.views.logout_then_login",{"login_url":"/"}),

    url(r'^cadl/', include(admin.site.urls)),
)

urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }))
