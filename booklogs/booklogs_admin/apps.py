from django.contrib.admin.apps import AdminConfig

class BooklogsAdminConfig(AdminConfig):
    default_site = 'booklogs_admin.admin.BooklogsAdmin'