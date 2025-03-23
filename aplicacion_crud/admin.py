from django.contrib import admin
from .models import Citas

# Register your models here.
class CitasAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)
    
admin.site.register(Citas, CitasAdmin)
