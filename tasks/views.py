from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


from .models import *
from .forms import *


# Create your views here.

def index(request):
	tasks = Task.objects.all()

	form = TaskForm()

	if request.method == 'POST':
		form = TaskForm(request.POST) #pass post method
		if form.is_valid():
			form.save()	#saves to the database
		return redirect('/') #send back to same url path


	context = {'tasks': tasks, 'form':form}
	return render(request, 'task/list.html', context)

def user(request):
	context = {'user': {'name': 'Jamie'}}
	return render(request, 'task/user.html', context)

def updateTask(request, pk): #pk is a url pattern
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method =='POST':
		form = TaskForm(request.POST, instance=task) 
		#need 'instance=' because if not then it will make a new instance
		if form.is_valid():
			form.save()
			return redirect ('/')

	context = {'form':form}

	return render(request, 'task/update_task.html', context)

def deleteTask (request, pk):
	item = Task.objects.get(id=pk)

	if request.method =='POST':
		item.delete()
		return redirect ('/')

	context = {'item':item}
	return render(request, 'task/delete.html', context)

