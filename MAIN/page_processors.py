#-*- coding: utf-8 -*-

from __future__ import unicode_literals

# from django.utils.translation import ugettext as _

from mezzanine.pages.page_processors import processor_for
# from mezzanine.core.request import current_request
from .models import *

@processor_for('/')
def processor_home(request, page):
    print "ok"
    reportage = Reportage.objects.last()
    print "page processors says %s" % reportage.title
    return locals()


