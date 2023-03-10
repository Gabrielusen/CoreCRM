from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead
from .forms import LeadForm

# Create your views here.


def index(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, 'leads/lead_list.html', context)


def lead_detail(request, pk):
    leads = Lead.objects.get(id=pk)
    context = {
        'leads': leads
    }
    return render(request, 'leads/lead_detail.html', context)


def lead_create(request):
    context = {
        "form": LeadForm()
    }
    return render(request, 'leads/lead_create.html', context)
