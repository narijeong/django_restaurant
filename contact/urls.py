from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.send_email, name="send_email"),
    path('sucess/', views.send_sucess, name="send_sucess"),
]
