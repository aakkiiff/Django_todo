
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.utils import timezone

from .models import Todo_list
# Create your views here.
def home(request):
    print('home page')
    todo_items = Todo_list.objects.all().order_by('-added_date')
    return render(request,'index.html',{'todo_items':todo_items})

def add_task(request):
    print('task accepted')
    current_time = timezone.now()
    #print(current_time)
    content = request.POST['content']
    #print(content)
    Todo_list.objects.create(title=content)
    #print('task added')
    return HttpResponseRedirect('/home/')


def delete_task(request,pk):
    print("at delete view")
    print(pk)
    delete = Todo_list.objects.get(id=pk).delete()
    print("task deleted")
    return HttpResponseRedirect('/home/')