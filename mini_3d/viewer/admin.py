from django.contrib import admin
from .models import ThreeDModel

# Register your models here.
@admin.register(ThreeDModel)
class ThreeDModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'format', 'created_at', 'updated_at']
    list_filter = ['format', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']
    