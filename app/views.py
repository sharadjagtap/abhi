from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import Beer
from django.core.urlresolvers import reverse_lazy


class BeerListView(ListView):
    model = Beer

class BeerDetailView(DetailView):
    model = Beer

class BeerCreateView(CreateView):
    model = CreateView
    fields = '__all__'

class BeerUpdateView(UpdateView):
    model = Beer
    fields = ('taste','color','price')

class BeerDeleteView(DetailView):
    model = Beer
    success_url=reverse_lazy('home')