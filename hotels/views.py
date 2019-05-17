from django.shortcuts import render

from . models import Hotel

from django.views.generic import DetailView

# Create your views here.
def hotel_view(request):
    hotel_list = Hotel.objects.all()
    return render(request, 'hotels/hotel.html', {'hotel_list':hotel_list})


class hotel_page(DetailView):
    model = Hotel
    template_name = 'hotels/hotel_page_new.html'
