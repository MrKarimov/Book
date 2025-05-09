from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
# Create your views here.

#Ma'lumotlar ro'yxatini chiqarish va Yangi  ma'lumot qo'shish uchun
class BookListCreateApiView(generics.ListCreateAPIView):
    queryset =  Book.objects.all()
    serializer_class = BookSerializer

class BookListApiView(APIView):
  def get(self,request):
    items = Book.objects.all()
    serializer = BookSerializer(items,many = True).data
    data = {
       "status": f"Returned {len(items)} books",
       "books": serializer
    }
    return Response(data)
  
class BookCreateApiView(APIView):
   def post(self, request):
      items = Book.objects.all()
      serializer = BookSerializer(data=request.data)
    #   data = {
    #      "status": f"Returned {len(items)} books",
    #      "books": serializer
    #   }
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status = status.HTTP_201_CREATED)
      return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)




#Ma'lumotlarni taxrirlash va o'chirish uchun
class BookDetailDeleteUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
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