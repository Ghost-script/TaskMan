from django.shortcuts import render
from django.core.urlresolvers import reverse
from models import Task,TaskLog
from django.shortcuts import redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from forms import TaskCreate,TaskRemove,TaskUpdateDeadline,TaskUpdateStatus
from datetime import datetime
# Create your views here.

@login_required(login_url='/login')
def create_task(request):
    if request.method == 'POST':
        form = TaskCreate(request.POST)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data['title']
            status = "INCOMPLETE"
            deadline = form.cleaned_data['complete_by']
            print deadline
            #deadline = datetime.strptime(form.cleaned_data['complete_by'],'%d %b %Y')
            #deadline = timezone.make_aware(deadline,timezone="Asia/Kolkata")
            added = timezone.now()
            detail = form.cleaned_data['details']
            new_task = Task(user=user,title=title,detail=detail,status=status,deadline_date=deadline,added_date=added)
            new_task.save()
        return render(request,"dashboard.html",{'form':form})
    form = TaskCreate()
    return render(request,"create_task.html",{'form':form})

@login_required(login_url='/login')
def delete_task(request):
    if request.method == 'POST':
        form = TaskRemove(request.POST)
        form2 = TaskCreate()
        if form.is_valid():
            user = request.user
            title = form.cleaned_data['title']
            task = Task.objects.get(user=user,title=title).delete()

        return render(request,"dashboard.html",{'form':form1,'form2':form2})

@login_required(login_url='/login')
def update_task(request):
    if request.method == 'POST':
        form2 = TaskCreate()
        print 'status' in request.POST.keys()
        print request.POST.get('status')

        if 'complete_by' in request.POST.keys():
            form = TaskUpdateDeadline(request.POST)
        
            if form.is_valid(): 
                user = request.user
                title = form.cleaned_data['title']
                deadline = form.cleaned_data['complete_by']
                task = Task.objects.get(user=user,title=title)
                task.deadline_date = deadline
                task.save()
        if 'status' in request.POST.keys():
            form = TaskUpdateStatus(request.POST)
        
            if form.is_valid(): 
                user = request.user
                title = form.cleaned_data['title']
                status = form.cleaned_data['status']
                task = Task.objects.get(user=user,title=title)
                task.status = status
                task.save()
        return render(request,"dashboard.html",{'form2':form2})

def show_task(request):
    user = request.user
    task = Task.objects.filter(user=user).all()
    return task

def show_logs(request):
    user = request.user
    log = TaskLog.objects.filter(task__user=user).all()
    return log
