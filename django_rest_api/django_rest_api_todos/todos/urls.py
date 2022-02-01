from django.urls import path
from todos import views

urlpatterns = [
    path('todos/', views.todos),
    path('todos/<int:pk>/', views.todo_detail),
]