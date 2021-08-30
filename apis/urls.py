from django.urls import path
from .views import ListTodo
from .views import DetailTodo

urlpatterns = [
    path('',ListTodo.as_view()),
    path('<int:pk>/',DetailTodo.as_view())
]