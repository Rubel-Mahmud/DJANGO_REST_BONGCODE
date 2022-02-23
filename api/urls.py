from django.urls import path
from .views import article_list, article_detail

urlpatterns = [
    path('list/', article_list, name='list'),
    path('<int:pk>/', article_detail, name='detail'),
]
