from core.models import AnnouncedPuResults, Lga, PollingUnit
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView 
# from django.utils import timezone

# Create your views here.

class LgaselectView(CreateView):

    model = Lga
    fields = ['lga_name']
    template_name = "select.html"
    


class PollingUnitListView(ListView):

    model = AnnouncedPuResults
    template_name = 'index.html'
    context_object_name = 'announced_pu_results'

    
    