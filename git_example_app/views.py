from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
  return render(request, 'index.html')

def add_user(request):
  if request.method == "POST":
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    age = request.POST['age']
    User.objects.create(first_name=first_name, last_name=last_name, age=age)
    return redirect("/")