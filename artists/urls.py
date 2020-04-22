from django.urls import path

from . import views

urlpatterns = [
        path('', views.home, name='home.html'),
        path('<int:pk>/', views.edit, name='edit'),
        path('add_artist/', views.add, name='add'),
]
