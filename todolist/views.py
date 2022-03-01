from pickle import NONE
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import TaskList
from .form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required  # for restriction in login

@login_required         # thats view get accessed only if the user logged in in our current applications
def todo(request):
    if request.method =="GET":
        all_tasks = TaskList.objects.filter(manager = request.user)
        # first arg is in which object we are going to set paginator, second hw much we have to display in one page
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get("pg")
        
        all_tasks = paginator.get_page(page)
        context = {
            "all_tasks": all_tasks,
        }
        return TemplateResponse(request,'todo.html',context)
    elif request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).manager = request.user
            form.save()
        messages.success(request,("New Task Added!!"))
        return redirect('todo')

@login_required  
def delete_task(request,task_id):
    task = TaskList.objects.get(id=task_id)
    if task.manager == request.user:
        task.delete()
    else:
        messages.error(request,("Access Restricted, You Are Not Allowed!!"))
    return redirect('todo')

@login_required  
def edit_task(request,task_id):
    if request.method == "POST":
        task = TaskList.objects.get(id=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task Edited!!"))
        return redirect('todo')
    else:
        taskObj = TaskList.objects.get(id=task_id)
        return TemplateResponse(request,"edit.html",context={"taskObj" : taskObj})

@login_required       
def complete_task(request,task_id):
    task = TaskList.objects.get(id=task_id)
    if task.manager == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request,("Access Restricted, You Are Not Allowed!!"))
    return redirect('todo')

@login_required  
def pending_task(request,task_id):
    task = TaskList.objects.get(id=task_id)
    task.done = False
    task.save()
    return redirect('todo')

@login_required  
def contact(request):
    context = {
        "Welcome_text": "Welcome Contact Page.",
    }
    return TemplateResponse(request,'contact.html',context)


def about(request):
    context = {
        "Welcome_text": "Welcome About Page.",
    }
    return TemplateResponse(request,'about.html',context)


def index(request):
    context = {
        "Welcome_text": "Welcome Index Page.",
    }
    return TemplateResponse(request,'index.html',context)
