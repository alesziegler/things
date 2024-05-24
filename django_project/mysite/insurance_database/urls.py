from django.urls import path
from . import views

urlpatterns = [
    path("", views.customer_detail, name="customer_detail"),
]