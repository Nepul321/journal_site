
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('', include('posts.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('users.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/posts/', include('posts.api.urls')),
]
