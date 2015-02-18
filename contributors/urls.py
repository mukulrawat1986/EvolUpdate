from django.conf.urls import patterns, url
from contributors import views

urlpatterns = patterns('',
    url(r'^$', views.main, name='main'),
    url(r'^article/(?P<article_id>\d+)', views.article, name='article'),
    url(r'^contributors', views.contributors, name='contirbutors'),
    url(r'^library', views.archive, name='archive'),
    url(r'^about', views.about, name='about'),
    url(r'^submitted/', views.submitted, name='submitted'),
    url(r'^mailing/', views.mailinglist, name='mailinglist'),
    url(r'^contact/', views.contact, name='contact'),
)
