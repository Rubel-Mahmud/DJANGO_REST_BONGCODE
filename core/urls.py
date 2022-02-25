from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('articles/', include('api.urls')),
    path('', include('api.urls')), # This path for DefaultRouter
    path('messages/', include('postman.urls', namespace='postman')),
]
