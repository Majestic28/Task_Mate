from email import message
from pyexpat.errors import messages
from django.shortcuts import redirect, render
#from django.contrib.auth.forms import UserCreationForm
from django.template.response import TemplateResponse
from django.contrib import messages
from users_app.forms import CustomRegisterForm

# django has in built user creation form

def register(request):
    if request.method == "POST":
        reg_form = CustomRegisterForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            messages.success(request,("New User Account Created!"))
            return redirect("register")
    elif request.method == "GET":
        reg_form = CustomRegisterForm()
        return TemplateResponse(request,"register.html",context={"register_form" : reg_form})