from django.conf.urls import url
#from django.conf.urls.defaults import *
from . import views

urlpatterns=[
    url(r'^convertir/', views.Bases, name="Bases"),
    url(r'^convermenu$', views.Menuieee),
    url(r'^32bits/', views.Ieeetd, name="Ieeetd"),
    url(r'^64bits/', views.Ieeesc, name="Ieeesc"),
    url(r'^biseccion/', views.Biseccion, name="Biseccion"),
    url(r'^reglafalsa/', views.Reglafalsa, name="Reglafalsa"),
    url(r'^newton/', views.Newton, name="Newton"),
    url(r'^secante/', views.Secante, name="Secante"),
    url(r'^evaluador/', views.Evaluador, name="Evaluador"),
    url(r'^polinomios/', views.Polinomios, name="Polinomios"),
    url(r'^simpson13/', views.Simpson13, name="Simpson13"),
    url(r'^trapecios/', views.Trape, name="Trape"),
    url(r'^rectangulos/', views.Rect, name="Rect"),
    url(r'^derivada/', views.derivada, name="derivada"),
]

"""urlpatterns=patterns(
    (r'^dsympy/',include('dsympy.urls'))
)"""
