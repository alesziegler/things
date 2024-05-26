from django.urls import path
from . import views

urlpatterns = [
path("main_table/", views.MainTable.as_view(), name="main_table"),
path("add_customer/", views.AddCustomer.as_view(), name="add_customer"),
path("login/", views.UserViewLogin.as_view(), name="login"),
path("logout/", views.logout_user, name="logout"),
]