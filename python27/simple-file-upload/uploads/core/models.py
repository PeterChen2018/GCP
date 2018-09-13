from __future__ import unicode_literals

"""
from django.db import models

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
"""

from django.db import models
import os, datetime
from django.utils.text import slugify

UPLOAD_PATH = "image_uploader/"


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class UploadedImage(models.Model):
    def generate_upload_path(self, filename):
        filename, ext = os.path.splitext(filename.lower())
        filename = "%s.%s%s" % (slugify(filename),datetime.datetime.now().strftime("%Y-%m-%d.%H-%M-%S"), ext)
        return '%s/%s' % (UPLOAD_PATH, filename)

    image = models.ImageField(blank=True, null=True, upload_to=generate_upload_path)

