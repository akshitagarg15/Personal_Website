
from django.urls import path

from . import views

urlpatterns = [

    path('',views.Index,name='index',),
    path('contact',views.Contact,name='contact'),
    path('portfolio',views.Portfolio,name='portfolio'),
]
