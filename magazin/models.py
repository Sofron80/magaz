from django.db import models
from django.conf import settings

# Create your models here.


class Category(models.Model):
	"""docstring for Category"""
	name = models.CharField(max_length=200, verbose_name="Наименование категории")
	slug = models.CharField(max_length=250, verbose_name='url')
	desc = models.CharField(max_length=250, blank=True, verbose_name='Описание категории')
	kwd = models.CharField(max_length=250, blank=True, verbose_name='Ключевые слова категории')
	text = models.TextField()
	active = models.BooleanField(default=False, verbose_name='Активность')

	def url(self):
		return '/'.join([settings.BASE_URL,'category', self.slug])+'.html'
	def __str__(self):
		return self.name

	class Meta():
		unique_together = ('slug',)
		verbose_name = 'Категория товаров'
		verbose_name_plural = 'Категории товаров'

class Tovar(models.Model):
	name = models.CharField(max_length=200, verbose_name="Наименование товара")
	slug = models.CharField(max_length=250, verbose_name='url')
	desc = models.CharField(max_length=250, blank=True, verbose_name='Описание товара')
	kwd = models.CharField(max_length=250, blank=True, verbose_name='Ключевые слова товара')
	text = models.TextField()
	price = models.CharField(max_length=50)
	img = models.ImageField(blank=True, upload_to='tovar')
	category = models.ForeignKey(Category)
	active = models.BooleanField(default=False, verbose_name='Активность')
	def get_url(self):
		return '/'.join([settings.BASE_URL, 'category', self.category.slug,self.slug])+'.html'
	
	def __str__(self):
		return self.name

	class Meta():
		unique_together = ('slug',)
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'
	
class Svoistvo_tovar(models.Model):
	name = models.CharField(max_length=200, verbose_name="Наименование свойства")
	text = models.CharField(max_length=200, verbose_name="Свойство")
	tovar = models.ForeignKey(Tovar)

	def __str__(self):
		return self.name
	class Meta():
		verbose_name = 'Свойство товара'
		verbose_name_plural = 'Свойства товаров'
	

################### Статьи ###########################
class Article(models.Model):
	title = models.CharField(max_length=250)
	slug = models.CharField(max_length=250)
	text = models.TextField()
	kwd = models.CharField(max_length=250, blank=True)
	desc = models.CharField(max_length=250, blank=True)
	img = models.ImageField(blank=True, upload_to='article')
	active = models.BooleanField(default=False, verbose_name='Активность')
	date_create = models.DateTimeField(auto_now_add=True)
	date_change = models.DateTimeField(auto_now=True)

	def get_url(self):
		return '/'.join([settings.BASE_URL, 'articles', self.slug])+'.html'

	def __str__(self):
		return self.title

	class Meta():
		unique_together = ('slug',)
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'

################### Новости ###########################
class News(models.Model):
	title = models.CharField(max_length=250)
	slug = models.CharField(max_length=250)
	text = models.TextField()
	kwd = models.CharField(max_length=250, blank=True)
	desc = models.CharField(max_length=250, blank=True)
	img = models.ImageField(blank=True, upload_to='news')
	active = models.BooleanField(default=False, verbose_name='Активность')
	date_create = models.DateTimeField(auto_now_add=True)
	date_change = models.DateTimeField(auto_now=True)

	def get_url(self):
		return '/'.join([settings.BASE_URL, 'news', self.slug])+'.html'

	def __str__(self):
		return self.title

	class Meta():
		unique_together = ('slug',)
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'