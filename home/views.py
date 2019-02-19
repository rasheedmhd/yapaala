from django.shortcuts import render

from . models import House

from django.views.generic import DetailView

# Create your views here.
def home_view(request):
    house = House.objects.all()
    return render(request, 'home/home.html', {'listed_houses':house})


class house_details(DetailView):
    model = House
    template_name = 'home/house_details.html'
