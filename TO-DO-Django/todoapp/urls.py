from django.urls import path
from . import views

# URL patterns for the todoapp
urlpatterns = [
    # Home page
    path('', views.home_view, name='home'),
    
    # Task management URLs
    path('tasks/', views.TaskListView.as_view(), name='task-list'),
    path('task/create/', views.TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),
    path('task/<int:pk>/toggle/', views.toggle_task_complete, name='task-toggle'),
    
    # Authentication URLs
    path('register/', views.register_view, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]
