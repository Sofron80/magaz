from django.contrib import admin
from .models import Category, Tovar, Svoistvo_tovar
# Register your models here.

class SvoistvoAdmin(admin.TabularInline):
	model = Svoistvo_tovar
	extra = 1


class TovarAdmin(admin.ModelAdmin):
	inlines = [SvoistvoAdmin,]
	prepopulated_fields = {"slug": ("name",)}

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}



admin.site.register(Category, CategoryAdmin)
admin.site.register(Tovar, TovarAdmin)
