from django.urls import path
from .views import BookListCreateApiView, BookDetailDeleteUpdateApiView, BookUpdateApiView, BookDeleteApiView

urlpatterns = [
    path('books/',BookListCreateApiView.as_view()),
    path('books/updatedelete/<int:pk>/',BookDetailDeleteUpdateApiView.as_view()),
    path('books/<int:pk>/update/',BookUpdateApiView.as_view()),
    path('books/<int:pk>/delete/',BookDeleteApiView.as_view()),


]
