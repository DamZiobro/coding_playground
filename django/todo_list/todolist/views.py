from django.shortcuts import render
from todolist.models import Task, TaskCategory
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

class HelloView(TemplateView):
    template_name = "hello.html"
    
    def get_context_data(self, **kwargs):
        return {
            "header" : "TODO header",
            "message" : "TODO message",
        }

class ListTasks(ListView):
    template_name = "list_tasks.html"
    model = Task
    ordering = ["-created_at"]

def create(request):

    task = Task(
        title = "Task title",
        description = "Task description",
    )
    home_cat = TaskCategory(name="home")
    home_cat.save()

    task.category = home_cat
    task.save()

    return HttpResponse(f"created task {task.title}")
