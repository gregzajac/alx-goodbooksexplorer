from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


# Create your views here.

def books_list(request):

    q = request.GET.get("q", "")
    num_page = request.GET.get("page", 1)
    per_page = request.GET.get("per_page", 25)

    books = Book.objects.all()
    if q:
        books = books.filter(title__icontains=q)

    p = Paginator(books, per_page)
    page_obj = p.page(num_page)

    # avg_num_pages = Book.objects.aggregate(Avg('num_pages'))

    return render(
        request,
        "books/list.html",
        {
            "page_obj": page_obj,
            "q": q
        }
    )