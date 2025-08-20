from django.contrib import admin

# Personalization of the standard Django admin module
class BooklogsAdminSite(admin.AdminSite):
    title_header = 'Booklogs Admin'
    site_header = 'Booklogs administration'
    index_title = 'Booklogs site admin'