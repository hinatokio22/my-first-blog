from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ecuaciones/', views.ecuaciones),
    url(r'^integrales/', views.integrales),
    url(r'^bases/', include('apps.bases.urls')),

]
