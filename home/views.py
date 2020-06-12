from django.shortcuts import render
from meals.models import Meals, Category
from blog.models import Post
from aboutus.models import Why_Choose_Us

# Create your views here.
def home(request):
    meal_list = Meals.objects.all()
    specialty_list = Meals.objects.filter(specialty=True)
    categories = Category.objects.all()
    posts = reversed(Post.objects.order_by('-created')[1:3])
    latest_post = None
    try:
        latest_post = Post.objects.latest('created')
    except:
        print('There is no post')

    why_choose_us = Why_Choose_Us.objects.all()
        
    context = {
        'meal_list': meal_list,
        'specialty_list':specialty_list,
        'categories': categories,
        'posts': posts,
        'latest_post': latest_post,
        'why_choose_us': why_choose_us,
    }

    return render(request, 'home/index.html', context)