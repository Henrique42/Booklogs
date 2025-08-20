# Import Django's built-in AdminConfig class for admin app configuration
from django.contrib.admin.apps import AdminConfig

# Create a custom admin configuration class
class ReviewsAdminConfig(AdminConfig):
    # Override the default admin site with a custom implementation
    default_site = 'admin.BooklogsAdminSite'