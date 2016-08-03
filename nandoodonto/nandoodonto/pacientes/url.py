from django.conf.urls import patterns, include, url

urlpatterns = patterns('nandoodonto.pacientes.views',
    url(r'^$', some_view, name='index'),
)