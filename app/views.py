from dataclasses import field, fields
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from .models import Task


class CustomLoginView(LoginView):
    template_name = 'app/login.html'
    fields = '__all___'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task')


class TaskList(ListView):
    model = Task
    context_object_name = 'task'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'app/task.html'


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task')


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task')


class DeleteView(DeleteView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task')
