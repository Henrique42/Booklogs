from django.contrib import admin
from reviews.models import Publisher, Contributor, Book, BookContributor, Review

# Custom Admin Configuration for Book Model
class BookAdmin(admin.ModelAdmin):
    # Enable date-based navigation by publication date
    date_hierarchy = "publication_date"
    # Display these fields in the list view
    list_display = ("title", "isbn13")  
    # Add filter sidebar for these fields
    list_filter = ("publisher", "publication_date")  
    # Enable search for these fields (including publisher name via relation)
    search_fields = ("title", "isbn", "publisher__name")  

    # Custom display method for formatted ISBN-13
    @admin.display(
        ordering="isbn",  # Allows sorting by original ISBN field
        description="ISBN-13",  # Column header text
        empty_value="-/-"  # Display when ISBN is empty
    )
    def isbn13(self, obj):
        """'9780316769174' => '978-0-31-676917-4'"""
        return "{}-{}-{}-{}-{}".format(
            obj.isbn[0:3], obj.isbn[3:4], obj.isbn[4:6], obj.isbn[6:12], obj.isbn[12:13]
        )

# Custom Admin for Contributor Model
class ContributorAdmin(admin.ModelAdmin):
    # Display these fields in list view
    list_display = ("last_names", "first_names")  
    # Enable filtering by last names
    list_filter = ("last_names",)  
    # Search by last names (startswith) and first names
    search_fields = ("last_names__startswith", "first_names")  

# Custom Admin for Review Model
class ReviewAdmin(admin.ModelAdmin):
    # Organize fields into grouped sections
    fieldsets = (
        (None, {"fields": ("creator", "book")}),
        ("Review Content", {"fields": ("content", "rating")}),
    )

# Model Registrations
admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)