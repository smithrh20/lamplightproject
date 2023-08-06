from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Photo


def framesView(request):
    context={}
    return render (request, 'frames.html', context)

class homeListView(ListView):
    model = Photo
    template_name = 'homeB.html'

class galleryListView(ListView):
    model = Photo
    template_name = 'galleryB.html'

class photoDetailsView(DetailView):
    model = Photo
    template_name = 'detailsB.html'
