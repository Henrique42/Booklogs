from django.contrib import admin
from django.urls import include, path

import reviews.views

# Website urls
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", reviews.views.index),
    path("book-search/", reviews.views.book_search, name="book_search"),
    # Includes the urls of the "reviews" app
    path("", include("reviews.urls")),
]