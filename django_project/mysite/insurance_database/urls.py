from django.urls import path
from . import views

urlpatterns = [
path("main_table/", views.MainTable.as_view(), name="customer_index"),
path("add_customer/", views.AddCustomer.as_view(), name="add_customer"),
]