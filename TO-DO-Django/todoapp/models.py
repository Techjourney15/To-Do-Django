from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    """
    Task model representing a to-do item
    Each task belongs to a specific user
    """
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        help_text="The user who owns this task"
    )
    title = models.CharField(
        max_length=200,
        help_text="Short title for the task"
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Detailed description of the task"
    )
    complete = models.BooleanField(
        default=False,
        help_text="Whether the task is completed"
    )
    due_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text="When the task is due"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        help_text="When the task was created"
    )
    updated = models.DateTimeField(
        auto_now=True,
        help_text="When the task was last updated"
    )

    class Meta:
        ordering = ['complete', '-created']  # Show incomplete tasks first, then by creation date
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        """String representation of the task"""
        return self.title

    @property
    def is_overdue(self):
        """Check if the task is overdue"""
        if self.due_date and not self.complete:
            return timezone.now() > self.due_date
        return False
