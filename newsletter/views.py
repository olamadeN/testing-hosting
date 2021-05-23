from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.



def newspage(request):
    collection = Article.objects.all().order_by('date')
    return render(request, 'newsletter.html', {'art':collection} )

def article_detail(request, slug):
    details = Article.objects.get(slug = slug)
    return render(request, 'art_details.html', {'collection':details})
