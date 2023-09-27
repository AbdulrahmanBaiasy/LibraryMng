from django.shortcuts import render, redirect, get_object_or_404
from .models import Book , Category
from .forms  import BookForm , CategoryForm

# Create your views here.


def index (request):

    if request.method == 'POST':
        add_book = BookForm (request.POST, request.FILES)
        if add_book.is_valid ():
            add_book.save()
            add_book = BookForm ()

        add_category = CategoryForm(request.POST)
        if add_category.is_valid ():
            add_category.save()
            add_category = CategoryForm ()



    context = {
        'category': Category.objects.all(),
        'book': Book.objects.all(),
        'form': BookForm(),
        'form_cat': CategoryForm(),
        'allbooks': Book.objects.filter(active= True).count(),
        'booksold': Book.objects.filter(status= 'sold').count(),
        'bookavailable': Book.objects.filter(status= 'available').count(),
        'bookrented': Book.objects.filter(status= 'rented').count(),


    }
    
    return render (request,'pages/index.html', context)


def books (request):

    search = Book.objects.all()
    title = None 
    if 'search_name' in request.GET: 
        title = request.GET['search_name']
        if title: 
            search = search.filter(title__icontains=title)


    context = {
        'category': Category.objects.all(),
        'book': search,
        'form_cat': CategoryForm(),


    }
    return render (request, 'pages/books.html',context)


def book_update (request, id ):
    book_id = Book.objects.get(id = id )
    if request.method == 'POST': 
        book_save = BookForm (request.POST , request.FILES , instance = book_id)
        if book_save.is_valid(): 
            book_save.save()
            return redirect ('/')
    else : 
        book_save = BookForm(instance = book_id) 
    context = {
        'form':book_save,
    }
    return render(request, 'pages/update.html',context)


def book_delete(request , id ): 
    book_id = get_object_or_404(Book, id = id )
    if request.method == 'POST':
        book_id.delete()
        return redirect('/')
    return render(request , 'pages/delete.html')