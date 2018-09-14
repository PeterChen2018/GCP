# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __unicode__(self):  # Python 3:  def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    # image = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True)
    image = models.ImageField( blank=True )
    
    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __unicode__(self):  # Python 3:    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


# ctest = models.ForeignKey('Category', blank=True, null=True)
# ctest = models.ForeignKey('Category', blank=True, null=True)


"""
from django.db import models
import os, datetime
from django.utils.text import slugify

UPLOAD_PATH = "image_uploader/"

class UploadedImage(models.Model):
    def generate_upload_path(self, filename):
        filename, ext = os.path.splitext(filename.lower())
        filename = "%s.%s%s" % (slugify(filename),datetime.datetime.now().strftime("%Y-%m-%d.%H-%M-%S"), ext)
        return '%s/%s' % (UPLOAD_PATH, filename)

    image = models.ImageField(blank=True, null=True, upload_to=generate_upload_path)

class MyModel(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to='uploads/')
    # or...
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')

If you are using the default FileSystemStorage, 
the string value will be appended to your MEDIA_ROOT path to form the location 
on the local filesystem where uploaded files will be stored. If you are using a different storage, 
check that storage’s documentation to see how it handles upload_to.
"""