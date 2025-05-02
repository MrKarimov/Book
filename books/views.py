from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
# Create your views here.

#Ma'lumotlar ro'yxatini chiqarish va Yangi  ma'lumot qo'shish uchun
class BookListCreateApiView(generics.ListCreateAPIView):
    queryset =  Book.objects.all()
    serializer_class = BookSerializer

#Ma'lumotlarni taxrirlash va o'chirish uchun
class BookDetailDeleteUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#Bittadan ma'lumot chiqrish uchun id bo'yicha 
class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#Ma'lumotni taxrirlash:
class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



#Ma'lumotlarni  O'chirish
class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class =BookSerializer