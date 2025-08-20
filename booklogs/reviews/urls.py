from django.urls import path
from . import views

# "reviews" app urls
urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail')
]