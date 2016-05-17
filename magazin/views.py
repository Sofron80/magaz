from django.shortcuts import render
from .models import Tovar

# Create your views here.
def index(request):
	date = {
		'tovars': Tovar.objects.all().order_by('-id'),
		'title' : 'Главная страница твоу мать',
		}
	return render(request, 'index.html', date)