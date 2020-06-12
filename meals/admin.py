from django.contrib import admin

# Register your models here.
from .models import Meals, Category    

class MealsAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']

admin.site.register(Meals, MealsAdmin)
admin.site.register(Category)


