from booklogs.views import profile
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin, auth
from django.urls import include, path

import booklogs.views
import reviews.views

# Website urls
urlpatterns = [
    path("admin/", admin.site.urls),
    #Includes the urls for django's standard user authentication
    path(
        "accounts/", include(("django.contrib.auth.urls", "auth"), namespace="accounts")
    ),
    path(
        "accounts/password_reset/done/",
        auth.views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "accounts/reset/done/",
        auth.views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    # Export read books by the current user
    path('accounts/profile/reading_history', booklogs.views.reading_history, name='reading_history'),
    #Includes the profile view
    path("accounts/profile/", profile, name="profile"),
    #Includes the urls for the review app
    path("", reviews.views.index),
    path("book-search/", reviews.views.book_search, name="book_search"),
    path("", include("reviews.urls")),
    #Includes the urls for the book management app
    path('book_management/', include('book_management.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)