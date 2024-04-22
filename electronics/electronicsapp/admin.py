from django.contrib import admin
from .models import ElectronicsModel, ElectroCategory, OfferModel

# Register your models here.

@admin.register(ElectronicsModel)
class ElectronicsModelAdmin(admin.ModelAdmin):
    fields = ['name', 'content', 'price', 'photo', 'slug', 'is_available', 'category']
    list_display = ['name', 'content', 'price', 'is_available', 'slug', 'category']
    list_display_links = ('name', )
    list_editable = ['is_available']
    save_on_top = True
    list_per_page = 5

@admin.register(ElectroCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    ordering = ('slug', )

@admin.register(OfferModel)
class OfferModelAdmin(admin.ModelAdmin):
    fields = ['name', 'content', 'price', 'photo', 'slug', 'up_to']
    list_display = ['name', 'content', 'price', 'slug', 'up_to']
    list_display_links = ['name']
    list_per_page = 5