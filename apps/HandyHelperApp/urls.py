from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^register$',views.register),
    url(r'^home$',views.home),
    url(r'^add$',views.newJob),
    url(r'^save$',views.saveNewJob),
    url(r'^login$',views.login),
    url(r'^logout$',views.logout),
    url(r'^edit/(?P<id>\d+)$',views.editJob),
    url(r'^saveJob/(?P<id>\d+)$',views.saveJob),
    url(r'^cancel/(?P<id>\d+)$',views.cancel),
    url(r'^jobs/view/(?P<id>\d+)$',views.view),
    url(r'^jobs/add/(?P<id>\d+)$',views.addJob),
    url(r'^jobs/done/(?P<id>\d+)$',views.doneJob) 
]