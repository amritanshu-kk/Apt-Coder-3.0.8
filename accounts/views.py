from django.contrib.auth.forms import UserCreationForm

# Create your views here.

from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def signin(request):
	#return render(request, 'signin.html')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username, password)
		if user is not None:
			form = login(request, user)
			message.succes(request, "welcome")
			return redirect('index')
		else:
			message.info(request, "please login")
	form = AuthenticationForm()
	return render(request, 'signin.html', {'form':form} )
# Create your views here.

def signup(request):
    if request.method == "POST":
	    form = RegisterForm(request.POST)
	    if form.is_valid():
	        form.save()

	    # return redirect("/home")
    else:
	    form = RegisterForm()

<<<<<<< HEAD
    return render(response, "signup.html", {"form":form})
=======
    return render(request, "signup.html", {"form":form})
>>>>>>> 546c170... added signup method
