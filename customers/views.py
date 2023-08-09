from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomerModel
from .forms import CustomerForm


def index(request):
    customers = CustomerModel.objects.all()
    return render(request, 'customers/index.html', {'customers': customers})


def add_customer(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('index')
    else:
        customer_form = CustomerForm()
    return render(request, 'customers/add-customer.html', {'customer_form': customer_form})

def delete_customer(request, pk):
    customer = get_object_or_404(CustomerModel, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('index')
    
    return redirect('index')