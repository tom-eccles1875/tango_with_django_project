from django.shortcuts import render
from rango.models import Category
from rango.models import Page


from django.http import HttpResponse
def index(request):
       return HttpResponse("Rango says hey there partner!  <a href='/rango/about/'>About</a>")


def show_category(request, category_name_slug):
       context_dict = {}
       try:
              category = Category.objects.get(slug=category_name_slug)
              pages = Page.objects.filter(category=category)
              context_dict['pages'] = pages
              context_dict['category'] = category
       except Category.DoesNotExist:
              context_dict['category'] = None
              context_dict['pages'] = None
       return render(request, 'rango/category.html', context=context_dict)



def about(request):
    
    return HttpResponse("Rango says here is the about page.  <a href='/rango/'>Index</a>")
