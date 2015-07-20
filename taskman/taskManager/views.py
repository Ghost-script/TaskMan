from django.shortcuts import render
from django.core.urlresolvers import reverse
from models import Task,TaskLog
from django.shortcuts import redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from forms import TaskCreate,TaskRemove,TaskUpdateDeadline,MultipleSelect
from datetime import datetime

@login_required(login_url='/login')
def create_task(request):
    """
    Function to create new Tasks 
    inputs via POST request:
    title,(optional)details,complete_by(date field)
    """
    if request.method == 'POST':
        form = TaskCreate(request.POST)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data['title']
            status = "INCOMPLETE"
            deadline = form.cleaned_data['complete_by']
            added = timezone.now()
            detail = form.cleaned_data['details']
            new_task = Task(user=user,title=title,detail=detail,status=status,
                            deadline_date=deadline,added_date=added)
            new_task.save()
    form = TaskCreate()
    form.message = "Succesfully created the task"
    return render(request,"create_task.html",{'form':form})
"""
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
"""

@login_required(login_url='/login')
def update_task(request):
    if request.method == 'POST':
        form2 = TaskCreate(request.POST)
        if form.is_valid(): 
            user = request.user
            title = form.cleaned_data['title']
            deadline = form.cleaned_data['complete_by']
            task = Task.objects.get(user=user,title=title)
            task.deadline_date = deadline
            task.save()
        return render(request,"dashboard.html",{'form2':form2})

def show_task(request,**kwargs):
    """
    fetches the task list

    operations currently supported are:
    order_by column desc/asc
    """
    
    user = request.user
    if kwargs['order'] =='desc':
        order = kwargs['col'].desc()
    else:
        order = kwargs['col']
    task = Task.objects.filter(user=user).order_by(order).all()
    return task

def show_logs(request):
    """
    Task tracker logs
    """

    user = request.user
    log = TaskLog.objects.filter(user=user).order_by('-id').all()
    return log


def update_multiple(request):
    """
    Updating/Deleting Multiple Tasks
    """

    if request.method == 'POST':
        form=MultipleSelect(request.POST)
        for er in form.errors:
            print form.errors['task_selected']
        if form.is_valid():
            action = request.POST.get('action')
            task_list = request.POST.getlist('task_selected')
            if action != "DELETE":
                no_of_updates = Task.objects.filter(title__in=task_list).update(status=action)
            else:
                Task.objects.filter(title__in=task_list).delete()
                no_of_updates=len(task_list)
            if no_of_updates > 2:
                temp="{task1},{task2} and {others} other"
            elif no_of_updates ==2:
                temp="{task1} and {task2}"
            elif no_of_updates ==1:
                temp="{task1}"
            else:
                return redirect('home')
            task = temp.format(task1=task_list[0],task2=task_list[1],others=len(task_list)-2)
            obj = TaskLog(user=request.user,task=task,action=action)
            obj.save()
            return redirect('home')
    
        else:
            return HttpResponse("tsetj")