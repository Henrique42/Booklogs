from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views import View
from .forms import BookForm
from .models import Book

success_page = '/book_management/entry_success'
form_page = 'book_form.html'

#CBV responsible for rendering the book catalog
class BookRecordFormView(FormView):
    template_name = form_page
    form_class = BookForm
    success_url = success_page

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

#Renders de success message    
class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Book record saved successfully")
    

##################
#####OPTIONAL#####
##################

# "C"RUD => Object Creation
class BookCreateView(CreateView):
    model = Book
    fields = ['name', 'author']
    template_name = form_page
    success_url = success_page

# C"R"UD => Object View
class BookRecordDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

# CR"U"D => Object Update
class BookUpdateView(UpdateView):
    model = Book
    fields = ['name', 'author']
    template_name = form_page
    success_url = success_page

# CRU"D" => Object Deletion
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete_form.html'
    success_url = '/'