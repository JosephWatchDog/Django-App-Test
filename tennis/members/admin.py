from django.contrib import admin
from .models import JoueurTennis

# Register your models here.

class JoueurAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date",)
    
admin.site.register(JoueurTennis, JoueurAdmin)
