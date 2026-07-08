from django.urls import path
from core.views import say_hello, home, post_list

urlpatterns = [
    path('hello/', say_hello, name='say_hello'),
    path('home/<username>/', home, name='home'),
    path('post/', post_list, name='post_list'),
]
