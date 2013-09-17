from django.conf.urls import patterns, url

urlpatterns = patterns('s3UploadSignature.views',
    url(r'^$', "s3_upload_signature", name="s3_upload_signature"),
)
