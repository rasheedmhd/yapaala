from django.shortcuts import render

from django.views.generic.list import ListView

from django.views.generic import DetailView

from .models import Blog


def blog_home(request):
    posts = Blog.objects.all()
    return render(request, 'blog/blog_home.html', {'posts':posts})


class blog_detail(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

'''
def blog_detail(request):
    posts = Blog.objects.all()
    return render(request, 'blog/blog_home.html', {'posts':posts})


class blog_home(ListView):
    model = Blog
    paginate_by = 6
    template_name = 'blog/blog_home.html'
'''

def mission_view(request):
    return render(request, 'master/our_mission.html')

def help_and_faq_view(request):
    return render(request, 'master/help_and_faq.html')

def privacy_and_terms_view(request):
    return render(request, 'master/terms.html')

def writing_view(request):
    return render(request, 'blog/how_to_become_a_writer.html')
