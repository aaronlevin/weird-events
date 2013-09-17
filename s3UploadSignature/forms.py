from django import forms

class S3UploadForm(forms.Form):
    s3_object_name = forms.CharField()
    s3_object_type = forms.CharField()
