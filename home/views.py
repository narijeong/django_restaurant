from django.shortcuts import render
from meals.models import Meals, Category
from blog.models import Post

# Create your views here.
def home(request):
    meal_list = Meals.objects.all()
    specialty_list = Meals.objects.filter(specialty=True)
    categories = Category.objects.all()
    posts = Post.objects.order_by('created')[:3]
    context = {
        'meal_list': meal_list,
        'specialty_list':specialty_list,
        'categories': categories,
        'posts': posts,
    }

    return render(request, 'home/index.html', context)