from django.shortcuts import render
from django.core.urlresolvers import reverse
from models import Task, TaskLog
from django.shortcuts import redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from forms import TaskCreate,MultipleSelect
from datetime import datetime
from django.db.models import Q
from django.views.decorators.http import require_http_methods


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
            try:
                Task.objects.get(title=title)
                form.error = "Duplicate Title Not Allowed"
            except Task.DoesNotExist:
                new_task = Task(user=user,
                                title=title,
                                detail=detail,
                                status=status,
                                deadline_date=deadline,
                                added_date=added)
                new_task.save()
                form = TaskCreate()
                form.message = "Succesfully created the task"
            except Exception as e:
                #log here
                print e
        return render(request, "create_task.html",
                      {'form': form,
                       'page': 'create'})
    form = TaskCreate()
    return render(request, "create_task.html",
                  {'form': form,
                   'page': 'create'})


@login_required(login_url='/login')
def update_task(request):
    """
    Edit task #to be implemented
    """
    if request.method == 'POST':
        form = TaskCreate(request.POST)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data['title']
            deadline = form.cleaned_data['complete_by']
            task = Task.objects.get(user=user, title=title)
            task.deadline_date = deadline
            task.save()
        return render(request, "dashboard.html", {'form': form})


def show_task(request, **kwargs):
    """
    fetches the task list

    operations currently supported are:
    order_by column desc/asc
    """

    user = request.user
    if kwargs['order'] == 'desc':
        order = "-"+kwargs['col']
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



@require_http_methods(["POST"])
def update_multiple(request):
    """
    Updating/Deleting Multiple Tasks
    """

    if request.method == 'POST':
        form = MultipleSelect(request.POST)
        if form.is_valid():
            action = request.POST.get('action')
            task_list = form.cleaned_data['task_selected']
            if action != "DELETE":
                no_of_updates = Task.objects.filter(id__in=task_list).update(
                    status=action)
            else:
                Task.objects.filter(id__in=task_list).delete()
                no_of_updates = len(task_list)

            task_list = Task.objects.filter(id__in=task_list).all()
            if no_of_updates > 1:
                temp = "{task1} and {others} other"
            elif no_of_updates == 1:
                temp = "{task1}"
            else:
                return redirect('home')

            task = temp.format(task1=task_list[0].title,
                               others=len(task_list) - 1)
            obj = TaskLog(user=request.user,
                          task=task,
                          action=action,
                          row_affected=no_of_updates)
            obj.save()
            return redirect('home')
        else:
            return HttpResponse("Invalid Form Data")
