from django.shortcuts import render
from .models import Tovar, Category
from django.conf import settings

# Create your views here.
def index(request):
	date = {
		'tovars': Tovar.objects.all().order_by('-id'),
		'title' : 'Главная страница твоу мать',
		}
	return render(request, 'index.html', date)

def category(request, cat_slug):
	category = Category.objects.get(slug = cat_slug)
	date = {
		
		 'category': category,
		 'tovar': Tovar.objects.filter(category = category)
		}
	return render(request, 'category.html', date)

def tovar(request, cat_slug, tov_slug):
	date = {
		
		 'tovar': Tovar.objects.get(slug = tov_slug),
		 'base_url': settings.BASE_URL
		}
	return render(request, 'tovar.html', date)
