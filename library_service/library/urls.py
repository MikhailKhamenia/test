from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import login, add_reader, menu, book_list, take_book, return_book, borrowed_books
urlpatterns = [
    path('', login, name='login'),
    path('add_reader/', add_reader, name='add_reader'),
    path('menu/', menu, name='menu'),
    path('book_list/', book_list, name='book_list'),
    path('take_book/<int:book_id>/', take_book, name='take_book'),
    path('return_book/<int:book_id>/', return_book, name='return_book'),
    path('borrowed_books/', borrowed_books, name='borrowed_books'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)