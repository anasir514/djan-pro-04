from django.shortcuts import render, redirect
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages


# Create your views here.
def homepage(request):
    return render(request = request,
                  template_name='homepage.html',
                  context = {"tutorials":Tutorial.objects.all})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "register.html",
                  context={"form":form})

def delete_task(request):
    return render(request, 'homepage.html', {})

def complete_task(request):
    return render(request, 'homepage.html', {})

def pending_task(request):
    return render(request, 'homepage.html', {})

def edit_task(request):
    return render(request, 'edit.html', {})

 
def about(request):
   context = {
       'welcome_text':"welcome from about."
   }
   return render(request, 'about.html', context)
 
def contact(request):
   context = {
       'welcome_text':"welcome from contact."
   }
   return render(request, 'contact.html', context)


def pricing(request):
   context = {
       'welcome_text':"welcome from contact."
   }
   return render(request, 'pricing.html', context)