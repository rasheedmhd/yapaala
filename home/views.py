from django.shortcuts import render, get_object_or_404

from . models import House, Category

from django.views.generic import DetailView

from django.views.generic.list import ListView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#configuring cloudinary
from django import forms
from django.http import HttpResponse

from cloudinary.forms import cl_init_js_callbacks
from .models import Photo
from .forms import PhotoForm

def upload(request):
    context = dict(backend_form = PhotoForm())

    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()

    return render(request, 'home/property_form.html', context)

'''
# Create your views here.
def home_view(request):
    house = House.objects.all()
    paginator = Paginator(house, 3)
    page = request.GET.get('page')
    try:
        houses = paginator.page(page)
    except PageNotAnInteger:
        houses = paginator.page(1)
    except EmptyPage:
        houses = paginator.page(paginator.num_pages)

    return render(request, 'home/home.html', {'listed_houses':house})
'''


def category_list(request):
    category = Category.objects.all()
    return render(request, 'home/category_list_none.html', {'category': category})


class home_view(ListView):
    model = House
    paginate_by = 6
    #context_object_name = 'house_items'
    template_name = 'home/home2.html'

class all_areas_view(ListView):
    model = House
    paginate_by = 12
    template_name = 'home/all_areas.html'


def about(request):
    return render(request, 'home/about.html', {})

class house_details(DetailView):
    model = House
    template_name = 'home/house_details.html'


class PostCategory(ListView):
    model = House
    template_name = 'home/categories.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return House.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(PostCategory, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


def coming_soon_view(request):
    return render(request, 'coming_soon.html')
