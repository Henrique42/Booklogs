from django import forms
from .models import Publisher, Review

# Book search form
class SearchForm(forms.Form):
    # Fields to be searched
    SEARCH_CHOICES = (
        ["title", "Title"],
        ["contributor", "Contributor"]
    )
    
    # Search query
    search = forms.CharField(min_length=3)
    # "Fields to be search" selector
    search_in = forms.ChoiceField(required=False, choices=SEARCH_CHOICES)

# Publisher form for creation and updates
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ("name", "website", "email")

# Review form for creation and updates
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("content", "rating", "creator")

    rating = forms.IntegerField(min_value=0, max_value=5)