from django.shortcuts import render

from django.views.generic.list import ListView

from django.views.generic import DetailView

from .models import Land


def lands(request):
    lands = Land.objects.all()
    return render(request, 'blog/lands.html', {'lands':lands})

def mission_view(request):
    return render(request, 'master/our_mission.html')

def help_and_faq_view(request):
    return render(request, 'master/help_and_faq.html')

def privacy_and_terms_view(request):
    return render(request, 'master/terms.html')
