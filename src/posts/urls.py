from django.urls import path
from .views import (
    AllArticles
)

urlpatterns = [
    path("all/", AllArticles, name="all")
]
