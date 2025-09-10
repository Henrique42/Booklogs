from django import forms
from .models import Book

# Form for the book catalog
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author']