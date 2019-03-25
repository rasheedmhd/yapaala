from django.shortcuts import render

# Create your views here.

def busoro(request):
    return render(request, 'busoro/busoro.html')
