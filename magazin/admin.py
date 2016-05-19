from django.contrib import admin
from .models import (Category, Tovar, Svoistvo_tovar, Article, News)
# Register your models here.

class SvoistvoAdmin(admin.TabularInline):
	model = Svoistvo_tovar
	extra = 1


class TovarAdmin(admin.ModelAdmin):
	inlines = [SvoistvoAdmin,]
	prepopulated_fields = {"slug": ("name",)}

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}

class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}

class NewsAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tovar, TovarAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(News, NewsAdmin)
