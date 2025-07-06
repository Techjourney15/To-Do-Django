from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Task
from .forms import CustomUserCreationForm, TaskForm


def home_view(request):
    """
    Home page view - redirects based on authentication status
    """
    if request.user.is_authenticated:
        return redirect('task-list')
    else:
        return redirect('login')


class CustomLoginView(LoginView):
    """
    Custom login view with Bootstrap styling
    """
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('task-list')
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    """
    Custom logout view with message
    """
    next_page = 'login'
    http_method_names = ['get', 'post']  # Allow both GET and POST
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request, 'You have been logged out successfully.')
        return super().dispatch(request, *args, **kwargs)


def register_view(request):
    """
    User registration view
    """
    if request.user.is_authenticated:
        return redirect('task-list')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome {user.first_name}! Your account has been created successfully.')
            return redirect('task-list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})


class TaskListView(LoginRequiredMixin, ListView):
    """
    Display list of tasks for the logged-in user
    """
    model = Task
    template_name = 'todoapp/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10
    login_url = 'login'
    
    def get_queryset(self):
        """Return tasks for the current user only"""
        return Task.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add statistics
        user_tasks = self.get_queryset()
        context['total_tasks'] = user_tasks.count()
        context['completed_tasks'] = user_tasks.filter(complete=True).count()
        context['pending_tasks'] = user_tasks.filter(complete=False).count()
        context['overdue_tasks'] = sum(1 for task in user_tasks if task.is_overdue)
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    """
    Create a new task
    """
    model = Task
    form_class = TaskForm
    template_name = 'todoapp/task_form.html'
    success_url = reverse_lazy('task-list')
    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Task created successfully!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update an existing task
    """
    model = Task
    form_class = TaskForm
    template_name = 'todoapp/task_form.html'
    success_url = reverse_lazy('task-list')
    login_url = 'login'
    
    def get_queryset(self):
        """Ensure users can only update their own tasks"""
        return Task.objects.filter(user=self.request.user)
    
    def form_valid(self, form):
        messages.success(self.request, 'Task updated successfully!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete a task with confirmation
    """
    model = Task
    template_name = 'todoapp/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
    login_url = 'login'
    
    def get_queryset(self):
        """Ensure users can only delete their own tasks"""
        return Task.objects.filter(user=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Task deleted successfully!')
        return super().delete(request, *args, **kwargs)


@login_required
def toggle_task_complete(request, pk):
    """
    Toggle task completion status via AJAX or direct call
    """
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.complete = not task.complete
    task.save()
    
    status = 'completed' if task.complete else 'marked as pending'
    messages.success(request, f'Task "{task.title}" {status}!')
    
    return redirect('task-list')
