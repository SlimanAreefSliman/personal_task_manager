from django.contrib import admin
from .models import Category, Task, Subtask

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at')
    list_filter = ('owner',)
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'status', 'priority', 'category', 'created_at')
    list_filter = ('status', 'priority', 'category', 'owner')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'

@admin.register(Subtask)
class SubtaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent_task', 'owner', 'status', 'created_at')
    list_filter = ('status', 'owner')
    search_fields = ('title', 'description')
