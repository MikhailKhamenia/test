from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.utils.datetime_safe import date

from .models import Reader, Book, Borrowing
from .forms import ReaderForm


def menu(request):
    return render(request, 'library/menu.html')

def login(request):
    if request.method == 'POST':
        last_name = request.POST.get('last_name')
        try:
            reader = Reader.objects.get(last_name=last_name)
        except Reader.DoesNotExist:
            return redirect('add_reader')
        request.session['reader_id'] = reader.id
        return redirect('menu')
    return render(request, 'library/login.html')

def add_reader(request):
    if request.method == 'POST':
        form = ReaderForm(request.POST)
        if form.is_valid():
            reader = form.save()
            request.session['reader_id'] = reader.id
            return redirect('menu')
    else:
        form = ReaderForm()
    return render(request, 'library/add_reader.html', {'form': form})

def book_list(request):
    borrowed_books = Borrowing.objects.filter(date_returned__isnull=True).values_list('book_id', flat=True)
    books = Book.objects.exclude(id__in=borrowed_books)
    return render(request, 'library/book_list.html', {'books': books})

def take_book(request, book_id):
    book = Book.objects.get(id=book_id)
    reader_id = request.session['reader_id']
    borrowing = Borrowing.objects.create(book=book, reader_id=reader_id, date_taken=timezone.now())
    return redirect('book_list')

def return_book(request, book_id):
    if request.method == 'POST':
        book_code = request.POST['book_code']
        try:
            book = Book.objects.get(code=book_code)
            borrowing = Borrowing.objects.get(book=book, reader_id=request.session['reader_id'], date_returned__isnull=True)
        except (Book.DoesNotExist, Borrowing.DoesNotExist):
            return render(request, 'library/return_book.html', {'error': 'Invalid book code or borrowing record not found'})
        borrowing.date_returned = timezone.now()
        borrowing.save()
        return redirect('menu')
    else:
        try:
            book = Book.objects.get(id=book_id)
            borrowing = Borrowing.objects.get(book=book, reader_id=request.session['reader_id'], date_returned__isnull=True)
            return render(request, 'library/return_book.html', {'book': book, 'borrowing': borrowing})
        except (Book.DoesNotExist, Borrowing.DoesNotExist):
            return render(request, 'library/return_book.html', {'error': 'Invalid book or borrowing record not found'})


def borrowed_books(request):
    reader_id = request.session['reader_id']
    borrowings = Borrowing.objects.filter(reader_id=reader_id, date_returned__isnull=True)
    return render(request, 'library/borrowed_books.html', {'borrowings': borrowings})
