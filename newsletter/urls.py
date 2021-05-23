from django.urls import path, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



app_name = 'newsletter'

urlpatterns = [
    path('', views.newspage, name='art_list'),
    #let this be the last url in the list
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="art_details")
]

urlpatterns += staticfiles_urlpatterns()