from django.urls import path
from .views import *
from . import views

urlpatterns = [
path('', homeListView.as_view(), name='homeListView'),
path('gallery', galleryListView.as_view(), name='galleryListView'),
path('details/<int:pk>',photoDetailsView.as_view(), name='photoDetailsView'),
path('frames/', views.framesView, name='framesView'),

]