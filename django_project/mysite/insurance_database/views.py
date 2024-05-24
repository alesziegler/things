from django.shortcuts import render

# Create your views here.
def customer_detail(request):
  return render(
    request, "insurance_database/customer_detail.html",
    dict(name="Josef Novak", age=30, contact="222111000")
  )