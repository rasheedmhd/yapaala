from django.shortcuts import render

# Create your views here.

from .models import Payment
from .forms import TransactionForm

def rental_pay_app(request):
    return render(request, 'pay_rent/rental_pay_home.html')


def add_payment_view(request):
    if request.method == "POST":
        form  = TransactionForm(request.POST)
    else:
        form  = TransactionForm()
    return render(request, 'pay_rent/add_payment.html', {'form':form})

def transaction_list_view(request):
    return render(request, 'pay_rent/transaction_list.html')
