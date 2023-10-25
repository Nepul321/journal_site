from django.urls import path
from .views import (
    AllArticles,
    ArticleDetails,
    ArticleCreateView,
    ArticleUpdateView
)

urlpatterns = [
    path("all/", AllArticles, name="all"),
    path("articles/view/<str:slug>/", ArticleDetails, name="article-detail"),
    path("articles/create/", ArticleCreateView, name="article-create"),
    path("articles/update/<int:id_>/", ArticleUpdateView, name="article-update"),
]
