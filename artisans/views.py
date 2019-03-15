from django.shortcuts import render

# Create your views here.
def artisans_home(request):
    return render(request, 'artisans/artisans_home.html')
