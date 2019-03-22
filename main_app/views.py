from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic.edit import CreateView

from .models import Item
from .forms import DeleteForm

# Create your views here.

def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {
        'items' : items,
    })

def delete(request):
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        items = Item.objects.all()
        item_id = int(request.POST.get('item_id'))
        item.delete()
        return render(request, 'home.html', {
            'items' : items,
        })

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/'

