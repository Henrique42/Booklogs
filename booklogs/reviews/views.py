from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    name = "nômade"
    return render(request, "base.html", {"name": name})

def book_search(request):
    search_string = request.GET.get("string") or "world"
    return render(request, "book_search.html", {"search_string": search_string})