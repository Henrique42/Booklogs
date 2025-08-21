from django import forms

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

    