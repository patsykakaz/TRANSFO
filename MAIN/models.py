#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.sites.models import *
from django.utils.translation import ugettext, ugettext_lazy as _

from settings import MEDIA_ROOT
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText
from mezzanine.core.fields import RichTextField, FileField
from mezzanine.utils.sites import current_site_id, current_request
from mezzanine.utils.models import upload_to

from colorfield.fields import ColorField

class Client(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=128)
    is_active = True
    is_staff= False

class Archive(Page, RichText):
    illustration = models.CharField(max_length=200,verbose_name='illustration',null=True,blank=True)

    def save(self, *args, **kwargs):
        # in_menus empty pour exclure les archives des content_tree
        self.in_menus = []
        self.content = self.content.replace('src="','src="/static/archives/')
        super(Archive, self).save(*args, **kwargs)

class SiteExtension(Page):
    color = ColorField(default='#007099')
    img_logo = models.ImageField(upload_to=MEDIA_ROOT+'/SITES/logo', null=True, blank=True, verbose_name='logo')
    img_banner = models.ImageField(upload_to=MEDIA_ROOT+'/SITES/banner', null=True, blank=True, verbose_name='banner', help_text='bannière pour la page d\'acceuil du sous-site')
    css_class = models.CharField(max_length=100, null=True, blank=True)
    title_sub = models.CharField(max_length=128, null=True, blank=True)
    baseline = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.in_menus = []
        self.css_class = "ID_"+str(current_site_id())+self.color.replace('#','_')
        super(SiteExtension, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'EXTENSION_SITE'

class PageUnivers(Page, RichText):
    illustration = models.ImageField(upload_to=MEDIA_ROOT+'/SITES/universPNP', null=True, blank=True, verbose_name='illustration')

    def save(self, *args, **kwargs):
        self.in_menus = []
        super(PageUnivers, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'UNIVERS_PNP'

class Reportage(Page, RichText):

    def save(self, *args, **kwargs):
        self.in_menus = []
        super(Reportage, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'REPORTAGE'

class Reportage_pic(models.Model):
    Reportage = models.ForeignKey("Reportage")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("MAIN.Reportage", "Reportage"),
        format="Image", max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'GALLERIE'



