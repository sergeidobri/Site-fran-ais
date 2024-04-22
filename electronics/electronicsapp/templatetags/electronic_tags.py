from django import template
from electronicsapp.models import ElectroCategory
from django.db.models import Q, Count


register = template.Library()


@register.inclusion_tag('electronics/list_categories.html')
def show_categories(cat_selected=0):
    cats = ElectroCategory.objects.annotate(total=Count('electronics')).filter(~Q(total=0))
    return {'cats': cats, 'cat_selected': cat_selected}
