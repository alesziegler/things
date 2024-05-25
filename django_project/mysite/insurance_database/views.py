from django.shortcuts import render
from django.views import generic

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
    form = self.form_class(None)
    return render(request, self.template_name, {"form": form})

  def get(self, request):
    #this is probably an equivalent of the part of an interface interacting with validation?
    form = self.form_class(None)
    return render(request, self.template_name, {"form": form})
