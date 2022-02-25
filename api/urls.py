from django.urls import path, include
from rest_framework import routers
# from .views import article_list, article_detail
from . import views

router = routers.DefaultRouter()
router.register('articles', views.ArticleView)

urlpatterns = [
    # path('list/', article_list, name='list'),
    # path('<int:pk>/', article_detail, name='detail'),

    # class base view
    # path('list/', views.ArticleList.as_view(), name='list'),
    # path('<int:pk>/', views.ArticleDetail.as_view(), name='detail'),

    # GenericApiView
    # path('list/', views.ArticleListView.as_view(), name='list'),
    # path('<int:pk>/', views.ArticleDetailView.as_view(), name='detail'),

    path('', include(router.urls)),
]

urlpatterns += [
    path('auth/', include('rest_framework.urls')),
]
