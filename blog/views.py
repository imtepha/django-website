# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Post, Portfolio
#def render(request, template_name, context=None, content_type=None, status=None, using=None)
# Create your views here.
# ouerysets doc https://docs.djangoproject.com/en/2.0/ref/models/querysets/
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request,'blog/index.html', {'posts':posts}) #the curly braclet will be use in the html

def portfolio_list(request):
    portfolios = Portfolio.objects(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/index.html', {'portfolios':portfolios}) #the curly braclet will be use in the html
    

