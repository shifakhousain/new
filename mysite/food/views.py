from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Item
from django.template import loader

def index(request):
    item_list = Item.objects.all()  # Fetch all items from the database
    template = loader.get_template('food/index.html')
    context = {
        'item_list': item_list
    }
    return HttpResponse(template.render(context, request))

def item(request):
    return HttpResponse('<h1>This is an item view</h1>')

def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)  # Corrected line
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)
