from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views.generic import ListView, DetailView


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    #Statuses of available books in "in stock" status
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    #Authors of books
    num_authors = Author.objects.all().count()
    #Count visits on site with session
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1


    #Drawing html with data
    return render(request=request, 
                  template_name='index.html',
                  context={
                  'num_instances': num_instances,
                  'num_instances_available': num_instances_available,
                  'num_authors': num_authors,
                   'num_books': num_books,
                   'num_visits': num_visits,}
                   )

class BookListView(ListView):
    model=Book
    paginate_by = 3

class BookDetailView(DetailView):
    model = Book

class AuthorListView(ListView):
    model = Author
    paginate_by = 4