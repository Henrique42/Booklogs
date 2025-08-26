from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

import reviews.views

# Website urls
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", reviews.views.index),
    path("book-search/", reviews.views.book_search, name="book_search"),
    # Includes the urls of the "reviews" app
    path("", include("reviews.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)