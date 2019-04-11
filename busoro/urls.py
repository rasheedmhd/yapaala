from django.urls import path

from . import views

app_name = "rental_pay"

urlpatterns = [
   path('', views.rental_pay_app, name="rental_pay"),
   path('add-payment', views.add_payment_view, name="add_payment"),
   path('list-of-transactions', views.transaction_list_view, name="transaction_list"),
]
