from django.db import models
from django.shortcuts import reverse


class ElectroCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class ElectronicsModel(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nom de l'appareil électronique")
    slug = models.SlugField(unique=True, max_length=150, verbose_name='URL')
    price = models.IntegerField(default=0, verbose_name='Prix')
    photo = models.ImageField(upload_to='electronics', blank=True, default=None, verbose_name='Photo')
    content = models.TextField(blank=True, verbose_name='Contenu')
    category = models.ForeignKey('ElectroCategory', related_name='electronics', on_delete=models.CASCADE, verbose_name='Catégorie')
    is_available = models.BooleanField(default=False, verbose_name='Disponible')

    def get_absolute_url(self):
        return reverse('electronic', kwargs={'electronic_slug': self.slug})

    def __str__(self):
        return self.name


class OfferModel(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    up_to = models.DateTimeField(default=None)
    photo = models.ImageField(upload_to='offers', blank=True, default=None)
    content = models.TextField(blank=True)
    price = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('offer-item', kwargs={'offer_slug': self.slug})

    def __str__(self):
        return self.name

