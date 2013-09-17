"""
Yo, all this comes from:

http://philfreo.com/blog/how-to-allow-direct-file-uploads-from-javascript-to-amazon-s3-signed-by-python/

But then I Django'ed it.
"""

import time, os, json, base64, urllib, hmac, sha

from django.conf import settings
from django.http import HttpResponse

from .forms import S3UploadForm

def as_json(stuff, status):
    return HttpResponse(
        json.dumps(stuff),
        status=status,
        content_type='application/json')

def s3_upload_signature(request):
    """
    Provide a temporary signature so that users can upload files directly from their
    browsers to our AWS S3 bucket.
    The authorization portion is taken from Example 3 on
    http://s3.amazonaws.com/doc/s3-developer-guide/RESTAuthentication.html
    """
    aws_upload = getattr(settings, "AWS_UPLOAD", {})
    bucket_name = aws_upload.get("BUCKET_NAME")
    access_key = aws_upload.get("ACCESS_KEY_ID")
    secret_key = aws_upload.get("SECRET_ACCESS_KEY")
    if not (bucket_name and access_key and secret_key):
        return as_json({
            "error": "You need to set AWS_UPLOAD stuff in your "
                     "settings.py file."}, 500)

    form = S3UploadForm(data=request.REQUEST)
    if not form.is_valid():
        return as_json({
            "error": "You need to call this with parameters for "
                     "s3_object_name and s3_object_type"}, 400)

    object_name = form.cleaned_data["s3_object_name"]
    mime_type = form.cleaned_data["s3_object_type"]

    # don't give user full control over filename - avoid ability to overwrite files
    random = base64.urlsafe_b64encode(os.urandom(2))
    object_name = random + object_name
    object_name = urllib.quote_plus(object_name) # make sure it works for filenames with spaces, etc.

    expires = int(time.time()+300) # PUT request to S3 must start within X seconds
    amz_headers = "x-amz-acl:public-read" # set the public read permission on the uploaded file
    resource = '%s/%s' % (bucket_name, object_name)
    str_to_sign = "PUT\n\n{mime_type}\n{expires}\n{amz_headers}\n/{resource}".format(
        mime_type=mime_type,
        expires=expires,
        amz_headers=amz_headers,
        resource=resource
    )
    sig = urllib.quote_plus(base64.encodestring(hmac.new(secret_key, str_to_sign, sha).digest()).strip())

    url = 'https://%s.s3.amazonaws.com/%s' % (bucket_name, object_name)
    return as_json({
        'signed_request': '{url}?AWSAccessKeyId={access_key}&Expires={expires}&Signature={sig}'.format(
            url=url,
            access_key=access_key,
            expires=expires,
            sig=sig
        ),
        'url': url
    }, 200)
