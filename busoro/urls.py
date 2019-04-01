from django.urls import path

from . import views

app_name = "busoro"

urlpatterns = [
   path('', views.busoro, name="busoro_pay"),
   path('add-payment', views.add_payment_view, name="add_payment"),
   path('list-of-transactions', views.transaction_list_view, name="transaction_list"),
]
