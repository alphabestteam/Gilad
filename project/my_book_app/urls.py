from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookDetail
from my_book_app import views

router = DefaultRouter()
router.register(r'books', BookList, BookDetail)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/books/', views.get_all_books, name='get-all-books'),
    path('api/books-by-genre/<str:genre>/', views.get_all_books, name='get-all-books'),
    path('api/books/', BookList.as_view(), name='book-list'),
    path('api/books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    ]
