from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from book.forms import BookForm
from book.models import Book


class BookList(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(BookList, self).get_context_data(**kwargs)
        books = Book.objects.all().order_by('author__name')
        print(books[0].title)

        context.update({
            'books': books,
        })
        return context


class CreateBook(CreateView):
    template_name = 'create.html'
    form_class = BookForm
    model = Book

    def get_success_url(self):
        return '/scrummers/'

    def form_valid(self, form):
        form.save()
        return super(CreateBook, self).form_valid(form)
