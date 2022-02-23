from django.urls import path
# from .views import article_list, article_detail
from . import views

urlpatterns = [
    # path('list/', article_list, name='list'),
    # path('<int:pk>/', article_detail, name='detail'),

    # class base view
    path('list/', views.ArticleList.as_view(), name='list'),
    path('<int:pk>/', views.ArticleDetail.as_view(), name='detail'),
]
