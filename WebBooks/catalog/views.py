from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import AuthorsForm
from .models import Book, Author, BookInstance, Genre
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

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

class LoanedBookByUserListView(LoginRequiredMixin, ListView):
    """A class for presenting books in a specific user's order."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='2').order_by('due_back')

def authors_add(request):
    """Function add new author for user"""
    author = Author.objects.all()
    authorsform = AuthorsForm()
    return render(request, "catalog/authors_add.html", {"form": authorsform, "author": author})

def create(request):
    """Function create new Author in user-form"""
    if request.method == "POST":
        author = Author()
        author.first_name = request.POST.get("first_name")
        author.second_name = request.POST.get("second_name")
        author.date_of_birth = request.POST.get("date_of_birth")
        author.date_of_death = request.POST.get("date_of_death")
        author.save()
        return HttpResponseRedirect("/authors_add/")

def delete(request, id):
    """Function delete Author on id"""
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect("/authors_add/")
    except Author.DoesNotExist:
        return HttpResponseNotFound("<h2>Автор не найден, повторите еще раз.</h2>")

def edit_1(request, id):
    author = Author.objects.get(id=id)
    if request.method == "POST":
        author.first_name = request.POST.get("first_name")
        author.second_name = request.POST.get("second_name")
        author.date_of_birth = request.POST.get("date_of_birth")
        author.date_of_death = request.POST.get("date_of_death")
        author.save()
        return HttpResponseRedirect("/authors_add/")
    else:
        return render(request, "catalog/edit_1.html", {"author": author})
    
class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')
