from django.shortcuts import render

# Create your views here.

def rental_pay_app(request):
    return render(request, 'pay_rent/rental_pay_home.html')


def add_payment_view(request):
    return render(request, 'pay_rent/add_payment.html')

def transaction_list_view(request):
    return render(request, 'pay_rent/transaction_list.html')
