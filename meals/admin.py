from django.contrib import admin

# Register your models here.
from .models import Meals, Category    

class MealsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

admin.site.register(Meals)
admin.site.register(Category)


