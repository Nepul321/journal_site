from django.urls import path
from .views import (
    AllArticles,
    ArticleDetails,
)

urlpatterns = [
    path("all/", AllArticles, name="all"),
    path("articles/<int:id>/", ArticleDetails, name="article-detail"),
]
