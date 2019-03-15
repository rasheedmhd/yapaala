from django.shortcuts import render, get_object_or_404

from . models import House, Category

from django.views.generic import DetailView

from django.views.generic.list import ListView

'''
# Create your views here.
def home_view(request):
    house = House.objects.all()
    return render(request, 'home/home.html', {'listed_houses':house})'''

def category_list(request):
    category = Category.objects.all()
    return render(request, 'home/category_list.html', {'category': category})

class home_view(ListView):
    model = House
    paginate_by = 6
    template_name = 'home/home.html'


class all_areas_view(ListView):
    model = House
    paginate_by = 12
    template_name = 'home/all_areas.html'


def about(request):
    return render(request, 'home/about.html', {})

def contact(request):
    return render(request, 'home/contact.html', {})

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


def comming_soon_view(request):
    return render(request, 'comming_soon.html')
