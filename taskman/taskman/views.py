from django.shortcuts import render, HttpResponse , redirect
from forms import LoginForm,RegistrationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email =  form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email,password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            form.error = "email/password missmatch"
            return render(request,'index.html',{'form' : form})
            
    else:
        form = LoginForm()

    return render(request,'index.html',{'form' : form})

def register_user(request):
    form = RegistrationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            email =  form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
            	user = User(username=username,email=email,password=password)
            	user.save()
            except Exception as e:
            	print e
            form.message="Success"
            return render(request,'registration.html',{'form' : form})	
    	else:
            return render(request,'registration.html',{'form' : form})			 	       
    else:
        form = RegistrationForm()
    return render(request,'registration.html',{'form' : form})	

@login_required(login_url="/")
def dashboard(request):
	return render(request,'dashboard.html',{})

def logout_user(request):
	logout(request)
	return redirect('/')