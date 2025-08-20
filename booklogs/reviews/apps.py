from django.apps import AppConfig

# Changes the standard behavior of the fields on the "reviews" app
class ReviewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviews'
