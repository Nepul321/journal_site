from django.urls import path
from .views import (
    AllArticles,
    ArticleDetails,
)

urlpatterns = [
    path("all/", AllArticles, name="all"),
    path("articles/<str:slug>/", ArticleDetails, name="article-detail"),
]
