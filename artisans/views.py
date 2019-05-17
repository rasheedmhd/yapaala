from django.shortcuts import render

from .models import Artisan

# Create your views here.
def artisans_home(request):
    return render(request, 'artisans/artisans_home.html')


def all_artisans_view(request):
    artisans = Artisan.objects.all()
    return render(request, 'artisans/all_artisans.html', {"artisan":artisans})
