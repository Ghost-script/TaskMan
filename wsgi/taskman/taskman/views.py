from django.shortcuts import render, HttpResponse, redirect
from forms import LoginForm, RegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from taskManager.forms import TaskCreate,MultipleSelect
from taskManager.views import show_task, show_logs


def index(request):
    """
    Handles user login
    """

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                if user.error is None:
                    login(request, user)
                    return redirect('home')
                else:
                    form.message = "Email/Password Mismatch"
                    return render(request, 'index.html', {'form': form})
            form.message = "Email not found"
            return render(request, 'index.html',
                          {'form': form,
                           'page': 'index'})
        else:
            form.message = "Invalid Email"
            return render(request, 'index.html',
                          {'form': form,
                           'page': 'index'})
    else:
        form = LoginForm()

    return render(request, 'index.html', {'form': form, 'page': 'index'})


def register_user(request):
    """
    Handles user Registration
    """

    form = RegistrationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm = form.cleaned_data['confirm']
            try:
                user = User.objects.get(email=email)
                form.error = "Email already registered!"
                return render(request, 'registration.html', {'form': form})
            except User.DoesNotExist:
                if password == confirm:
                    user = User(username=username,
                                email=email,
                                password=password)
                    user.save()
                    form = RegistrationForm()
                    form.message = "Success"
                else:
                    form.message = "Comfirm and Password field do not match"
                return render(request, 'registration.html',
                              {'form': form,
                               'page': 'reg'})
            except Exception as e:
                #logging be implemented here
                print e

        else:
            form.error = "Invalid form feild Values"
            return render(request, 'registration.html',
                          {'form': form,
                           'page': 'reg'})
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form, 'page': 'reg'})


@login_required(login_url="/")
def dashboard(request):
    """
    Handles dashboard tasklist request
    functions: Sorting the tasks , Showing TrackerLogs
    """

    col = request.GET.get('sortby', 'id')
    order = request.GET.get('order', 'asc')
    task = show_task(request, col=col, order=order)
    logs = show_logs(request)
    form = MultipleSelect()
    return render(request, 'dashboard.html',
                  {'tasks': task,
                   'logs': logs,
                   'form': form,
                   'page': 'home'})


def logout_user(request):
    """
    Logs user Out
    """

    logout(request)
    return redirect('/')
