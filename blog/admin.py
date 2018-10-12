# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# Register your models here.
from django.contrib import admin
#absolue import importing from outside current app
from .models import Post, Portfolio
#explicit relative import use when import from other module in current app
admin.site.register(Post)
admin.site.register(Portfolio)

