from django.conf.urls import patterns, include, url
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weirdCanada.views.home', name='home'),
    # url(r'^weirdCanada/', include('weirdCanada.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),

    # REST API
    (r'^api/featured_events/', include('featuredEvents.restUrls')),

    # S3 Upload Signer
    (r'^api/s3_upload_signature/', include('s3UploadSignature.urls')),
)
