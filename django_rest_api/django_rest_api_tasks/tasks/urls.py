
from django.urls import path 
from tasks import views

# define the urls
urlpatterns = [
    path('tasks/', views.tasks),
    path('tasks/<int:pk>/', views.task_detail),
]