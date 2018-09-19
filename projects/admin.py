from django.contrib import admin
from .models import Category, Project
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category, CategoryAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_per_page = 20
admin.site.register(Project, ProjectAdmin)
