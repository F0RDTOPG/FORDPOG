from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

def home(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductForm()
    else:
        form = ProductForm()

    products = Product.objects.all()
    context = {'form': form, 'products': products}
    return render(request, 'produse/home.html', context)


def about(request):
    return render(request,'produse/about.html')


def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'produse/delete_confirm.html', {'product': product})


def delete_confirm(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'produse/delete.html', {'product': product})
