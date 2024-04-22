from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from .models import ElectronicsModel, ElectroCategory, OfferModel
from .forms import ElectronicForm

# Create your views here.

menu_lst = [
    {'title': "Page d'accueil", 'name': 'home'},
    {'title': 'Offres gourmandes', 'name': 'offer'},
    {'title': 'Magasins', 'name': 'shops'},
    {'title': 'Services', 'name': 'services'},
    {'title': 'Contacts', 'name': 'сontacts'},
]


contacts = [
    {'name': 'Oleg Orlov', 'stud': 1132233495, 'job': 'Directeur'},
    {'name': 'Dobrin Sergueï', 'stud': 1132233496, 'job': 'Créateur de site internet'},
    {'name': 'Riabinin Vladislav', 'stud': 1132233497, 'job': 'Concepteur créatif'},
    {'name': 'Protsenko Nikita', 'stud': 1132233516, 'job': 'Photo responsable'},
]

def offer(request):
    offers = OfferModel.objects.all()
    data = {
        'title': 'Offres gourmandes',
        'menu': menu_lst,
        'offers': offers,
    }
    return render(request, 'electronics/offer.html', data)


def shops(request):
    text = "Pour l'instant, nous travaillons uniquement à la station de métro Belyaevo, rue Miklukho-Maklaya, 6"
    return render(request, 'electronics/shops.html', {'title': 'Magasins', 'menu': menu_lst, 'content': text})


def services(request):
    if request.method == 'POST':
        form = ElectronicForm(request.POST, request.FILES)
        if form.is_valid():
            ElectronicsModel.objects.create(is_available=False, **form.cleaned_data)
            return redirect('home')
    else:
        form = ElectronicForm()
    data = {
        'form': form,
        'menu': menu_lst,
        'title': 'Services',
    }
    return render(request, 'electronics/services.html', data)


def сontacts(request):
    data = {
        'contacts': contacts,
        'title': 'Contacts',
        'menu': menu_lst
    }
    return render(request, 'electronics/сontacts.html', data)


def electronic(request, electronic_slug):
    item = get_object_or_404(ElectronicsModel, slug=electronic_slug)
    return render(request, 'electronics/electronic-item.html', {'title': item.name, 'item': item, 'menu': menu_lst})


def offer_item(request, offer_slug):
    item = get_object_or_404(OfferModel, slug=offer_slug)
    return render(request, 'electronics/offer-item.html', {'title': item.name, 'item': item, 'menu': menu_lst})


class ElectronicShow(TemplateView):
    template_name = 'electronics/index.html'
    extra_context = {'title': "Page d'accueil", 'menu': menu_lst, 'items': ElectronicsModel.objects.all()}


def show_category(request, cat_slug):
    category = get_object_or_404(ElectroCategory, slug=cat_slug)
    items = ElectronicsModel.objects.filter(category_id=category.pk).select_related('category')

    data = {
        'title': f'Rayon: {category.name}',
        'menu': menu_lst,
        'items': items,
        'cat_selected': category.pk,
    }
    return render(request, 'electronics/index.html', data)