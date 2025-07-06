from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Admin configuration for Task model
    """
    list_display = ('title', 'user', 'complete', 'due_date', 'created', 'is_overdue')
    list_filter = ('complete', 'created', 'due_date', 'user')
    search_fields = ('title', 'description', 'user__username')
    list_editable = ('complete',)
    date_hierarchy = 'created'
    ordering = ('complete', '-created')
    
    fieldsets = (
        ('Task Information', {
            'fields': ('user', 'title', 'description')
        }),
        ('Status & Dates', {
            'fields': ('complete', 'due_date'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',),
            'description': 'These fields are automatically managed.'
        })
    )
    
    readonly_fields = ('created', 'updated')
    
    def is_overdue(self, obj):
        """Display overdue status in admin"""
        return obj.is_overdue
    is_overdue.boolean = True
    is_overdue.short_description = 'Overdue'
    
    def get_queryset(self, request):
        """Optimize queryset with select_related"""
        return super().get_queryset(request).select_related('user')
