from django.shortcuts import render

# Create your views here.

def busoro(request):
    return render(request, 'busoro/busoro_pay_home.html')


def add_payment_view(request):
    return render(request, 'busoro/add_payment.html')

def transaction_list_view(request):
    return render(request, 'busoro/transaction_list.html')
