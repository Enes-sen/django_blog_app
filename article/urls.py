from django.contrib import admin
from django.urls import path
from . import views
app_name = "article"
urlpatterns = [
    path("dashboard", views.Dashboard, name="dashboard"),
    path("addarticle", views.AddArticle, name="addarticle"),
    path("article/<int:id>", views.DetailArticle, name="article"),
    path("update/<int:id>", views.UpdateArticle, name="update"),
    path("delete/<int:id>", views.DeleteArticle, name="delete"),
     path("comment/<int:id>", views.AddCommentArticle, name="addcomment"),
    path('', views.AllArticles, name="articles"),
]