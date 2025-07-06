#!/usr/bin/env python
"""
Sample data creation script for Django To-Do List application.
Run this script to populate the database with sample tasks for testing.

Usage:
    python manage.py runscript create_sample_data
    OR
    python manage.py shell -c "exec(open('create_sample_data.py').read())"
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoproject.settings')
django.setup()

from django.contrib.auth.models import User
from todoapp.models import Task
from django.utils import timezone
from datetime import timedelta

def create_sample_data():
    """Create sample users and tasks for testing"""
    
    # Create sample users (if they don't exist)
    users_data = [
        {
            'username': 'john_doe',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'password': 'samplepass123'
        },
        {
            'username': 'jane_smith',
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane@example.com',
            'password': 'samplepass123'
        }
    ]
    
    created_users = []
    for user_data in users_data:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={
                'first_name': user_data['first_name'],
                'last_name': user_data['last_name'],
                'email': user_data['email']
            }
        )
        if created:
            user.set_password(user_data['password'])
            user.save()
            print(f"Created user: {user.username}")
        else:
            print(f"User {user.username} already exists")
        created_users.append(user)
    
    # Sample tasks data
    sample_tasks = [
        # Tasks for John Doe
        {
            'user': created_users[0],
            'title': 'Complete Django project',
            'description': 'Finish the Django To-Do list application with all features',
            'complete': False,
            'due_date': timezone.now() + timedelta(days=7)
        },
        {
            'user': created_users[0],
            'title': 'Buy groceries',
            'description': 'Milk, bread, eggs, vegetables for the week',
            'complete': True,
            'due_date': timezone.now() - timedelta(days=1)
        },
        {
            'user': created_users[0],
            'title': 'Schedule dentist appointment',
            'description': 'Call dentist office to schedule regular checkup',
            'complete': False,
            'due_date': timezone.now() + timedelta(days=3)
        },
        {
            'user': created_users[0],
            'title': 'Review pull requests',
            'description': 'Review and approve pending pull requests on GitHub',
            'complete': False,
            'due_date': None
        },
        {
            'user': created_users[0],
            'title': 'Plan weekend trip',
            'description': 'Research destinations and book hotel for weekend getaway',
            'complete': False,
            'due_date': timezone.now() + timedelta(days=14)
        },
        
        # Tasks for Jane Smith
        {
            'user': created_users[1],
            'title': 'Prepare presentation',
            'description': 'Create slides for quarterly business review meeting',
            'complete': False,
            'due_date': timezone.now() + timedelta(days=2)
        },
        {
            'user': created_users[1],
            'title': 'Workout routine',
            'description': 'Complete 30-minute cardio and strength training',
            'complete': True,
            'due_date': timezone.now()
        },
        {
            'user': created_users[1],
            'title': 'Read Python book',
            'description': 'Finish reading "Effective Python" - chapters 5-8',
            'complete': False,
            'due_date': timezone.now() + timedelta(days=10)
        },
        {
            'user': created_users[1],
            'title': 'Update resume',
            'description': 'Add recent projects and skills to resume',
            'complete': False,
            'due_date': None
        },
        {
            'user': created_users[1],
            'title': 'Call mom',
            'description': 'Weekly check-in call with family',
            'complete': True,
            'due_date': timezone.now() - timedelta(days=2)
        }
    ]
    
    # Create sample tasks
    created_count = 0
    for task_data in sample_tasks:
        task, created = Task.objects.get_or_create(
            user=task_data['user'],
            title=task_data['title'],
            defaults={
                'description': task_data['description'],
                'complete': task_data['complete'],
                'due_date': task_data['due_date']
            }
        )
        if created:
            created_count += 1
            print(f"Created task: '{task.title}' for {task.user.username}")
        else:
            print(f"Task '{task.title}' already exists for {task.user.username}")
    
    print(f"\nSample data creation complete!")
    print(f"Created {len(created_users)} users and {created_count} new tasks.")
    print("\nSample login credentials:")
    for user_data in users_data:
        print(f"Username: {user_data['username']}, Password: {user_data['password']}")

# Execute the function
if __name__ == "__main__":
    create_sample_data()
else:
    # When run via 'python manage.py shell'
    create_sample_data()
