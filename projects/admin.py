from django.contrib import admin
from .models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_per_page = 20

admin.site.register(Project, ProjectAdmin)
