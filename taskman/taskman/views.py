from django.shortcuts import render, HttpResponse , redirect
from forms import LoginForm,RegistrationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from taskManager.forms import TaskCreate,TaskRemove,TaskUpdateStatus,TaskUpdateDeadline
from taskManager.views import show_task,show_logs

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

            form.message = "Email/Password Mismatch"
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
            confirm = form.cleaned_data['confirm']
            try:
            	user = User.objects.get(email=email)
                form.error = "Email already registered!"
            	return render(request,'registration.html',{'form' : form})		
            except User.DoesNotExist:
            	user = User(username=username,email=email,password=password)
            	user.save()
                form = RegistrationForm()
                form.message="Success"
                return render(request,'registration.html',{'form' : form})  
            except Exception as e:
            	print e
            
    	else:
            return render(request,'registration.html',{'form' : form})			 	       
    else:
        form = RegistrationForm()
    return render(request,'registration.html',{'form' : form})	

@login_required(login_url="/")
def dashboard(request):
    col=request.GET.get('sortby','id')
    order=request.GET.get('order','asc')
    task = show_task(request,col=col,order=order)
    logs = show_logs(request)
    return render(request,'dashboard.html',{'tasks':task,'logs':logs})

def logout_user(request):
	logout(request)
	return redirect('/')