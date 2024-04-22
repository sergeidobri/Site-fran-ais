from django.urls import path
from . import views

urlpatterns = [
    path('', views.ElectronicShow.as_view(), name='home'),
    path('offer', views.offer, name='offer'),
    path('shops', views.shops, name='shops'),
    path('services', views.services, name='services'),
    path('сontacts', views.сontacts, name='сontacts'),
    path('electronics/<slug:electronic_slug>', views.electronic, name='electronic'),
    path('category/<slug:cat_slug>', views.show_category, name='category'),
    path('offer/<slug:offer_slug>', views.offer_item, name='offer-item')
]
