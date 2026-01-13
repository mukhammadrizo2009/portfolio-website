from django.contrib import admin
from .models import Education

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("institution", "degree", "start_year", "end_year")
