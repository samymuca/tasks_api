from django.contrib import admin
from .models import Task, UserProfile

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created_at',
        'finished_at',
        'is_completed'
    )

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'user',
        'email',
        
    )
