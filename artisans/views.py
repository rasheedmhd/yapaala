from django.shortcuts import render

# Create your views here.
def artisans_home(request):
    return render(request, 'artisans/artisans_home.html')


def all_artisans_view(request):
    return render(request, 'artisans/all_artisans.html')
