import reviews.views
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", reviews.views.index),
    path("book-search/", reviews.views.book_search, name="book_search"),
    path("", include("reviews.urls")),
]