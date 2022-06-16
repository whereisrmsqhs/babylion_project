from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

def home(request):
    posts = Item.objects.all()
    return render(request, 'home.html', {'posts':posts})


def modelform(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'form_create.html', {'form':form})

def details(request, post_id):
    post_detail = get_object_or_404(Item, pk=post_id)

    return render(request, 'details.html', {'post_detail':post_detail})