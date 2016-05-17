from django.shortcuts import render
from .models import Tovar, Category

# Create your views here.
def index(request):

	
	tovars = Tovar.objects.all().order_by('-id')
		
	return render(request, 'index.html', {'test': tovars})