from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home),
    path('add_task/', views.add_task),
    path('delete_task/<int:pk>/', views.delete_task)

]
