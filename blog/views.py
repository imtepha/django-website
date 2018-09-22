# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

#def render(request, template_name, context=None, content_type=None, status=None, using=None)
# Create your views here.
def post_list(request):
    return render(request,'blog/post_list.html', {})
