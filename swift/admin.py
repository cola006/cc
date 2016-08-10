from django.contrib import admin

from .models import Project, Income

class ProjectAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'type', 'start_date', 'due_date', 'progress')

admin.site.register(Project, ProjectAdmin)

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'signing_time', 'due_time', 'company', 'value')

admin.site.register(Income, IncomeAdmin)

