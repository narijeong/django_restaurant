from django.shortcuts import render
from meals.models import Meals, Category
from blog.models import Post

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
        
    context = {
        'meal_list': meal_list,
        'specialty_list':specialty_list,
        'categories': categories,
        'posts': posts,
        'latest_post': latest_post,
    }

    return render(request, 'home/index.html', context)