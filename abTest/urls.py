from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^setExperiment/(.+)$', 'abTest.views.setExperiment', name='setExperiment'),
    url(r'^sessionAdmin/$', 'abTest.views.sessionAdmin', name='sessionAdmin'),

)
