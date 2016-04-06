#-*- coding: utf-8 -*-

from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import *

from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost


class ArchiveAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets)

blog_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
# blog_fieldsets[0][1]["fields"].insert(-2, "archive")
#blog_fieldsets[0][1]["fields"].insert(-2, "resize")
#blog_fieldsets[0][1]["fields"].insert(-2, "highlight")
#class MyBlogPostAdmin(BlogPostAdmin):
#    fieldsets = blog_fieldsets

SiteExtensionAdmin_extra_fieldsets = (
                (None,
                        {'fields': ('color','img_logo','img_banner','title_sub','baseline')
                        }
                ),
        )


class SiteExtensionAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets) + SiteExtensionAdmin_extra_fieldsets

PageUnivers_extra_fieldsets = (
                (None,
                        {'fields': ('illustration','content')
                        }
                ),
        )
 
class PageUniversAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets) + PageUnivers_extra_fieldsets

class Reportage_picInline(admin.TabularInline):
    model = Reportage_pic

class ReportageAdmin(PageAdmin):
    inlines = (Reportage_picInline,)
    fieldsets = deepcopy(PageAdmin.fieldsets)

admin.site.register(Archive, ArchiveAdmin)
#admin.site.unregister(BlogPost)
#admin.site.register(BlogPost, MyBlogPostAdmin)
admin.site.register(SiteExtension, SiteExtensionAdmin)
admin.site.register(PageUnivers, PageUniversAdmin)
admin.site.register(Reportage, ReportageAdmin)

