from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.

def index(request):
  # view function for home page of site

  # generate counts of some of the main objects
  num_books=Book.objects.all().count()
  num_instances=BookInstance.objects.all().count()
 
  # available books (status = 'a')
  num_instances_available=BookInstance.objects.filter(status__exact='a').count()
  num_authors=Author.objects.count() # the 'all() is implied by default

  # render the html template index.html with the data in the context variable
  return render(
    request,
    'index.html',
    context={'num_books':num_books,'nums_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors },
)

class BookListView(generic.ListView):
  model = Book
  paginate_by = 10
class BookDetailView(generic.DetailView):
  model = Book
