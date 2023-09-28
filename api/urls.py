from django.urls import path, include 
from api import views 
urlpatterns = [
    path ('book/', views.BookList.as_view()),
    path ('book/<int:pk>/', views.BookDetail.as_view()),
    path ('category/', views.CategoryList.as_view()),
    path ('category/<int:pk>/', views.CategoryDetail.as_view()),


]
