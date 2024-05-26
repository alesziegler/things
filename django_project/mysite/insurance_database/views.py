from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Customer
from .forms import CustomerForm

# Create your views here.
class MainTable(generic.ListView):

  template_name = "insurance_database/main_table.html"
  context_object_name = "customers"

  def get_queryset(self):
    return Customer.objects.all().order_by("name")
  

class AddCustomer(generic.edit.CreateView):

  form_class = CustomerForm
  template_name = "insurance_database/add_customer.html"

  def get(self, request):
    if not request.user.is_admin:
            messages.info(request, "Nemate prava pro upravy.")
            return redirect("main_table")
    form = self.form_class(None)
    return render(request, self.template_name, {"form": form})

  def post(self, request):
    """
    This part of validation handles credentials of users entering input.
    Validation in forms.py handles integrity of inputed data.
    """
    if not request.user.is_admin:
            messages.info(request, "Nemate prava pro upravy.")
            return redirect("main_table")
    form = self.form_class(request.POST)
    if form.is_valid():
            form.save(commit=True)
            return redirect("main_table")
    return render(request, self.template_name, {"form": form})
  

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        messages.info(request, "Nemůžeš se odhlásit, pokud nejsi přihlášený.")
    return redirect("login")
