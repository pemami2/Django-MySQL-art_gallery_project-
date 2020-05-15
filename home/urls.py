from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^artists/$', views.artist, name='artists'),
    url(r'^styles/$', views.style, name='styles'),
    url(r'^locations/$', views.location, name='locations'),
    url(r'^artworks/$', views.artwork, name='artworks'),
    url(r'^contacts/$', views.contact, name='contacts'),
    url(r'^customers/$', views.customer, name='customers'),
    url(r'^artshows/$', views.artshow, name='artwhows'),
]