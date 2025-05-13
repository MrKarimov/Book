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


#APIView yaratish uchun misol
class BookListApiView(APIView):
  def get(self):
    items = Book.objects.all()
    serializer = BookSerializer(items,many = True).data
    data = {
       "status": f"Returned {len(items)} books",
       "books": serializer
    }
    return Response(data)
  

#Yangi m'alumot yaratish uchun
class BookCreateApiView(APIView):
   def post(self, request):
      items = request.data
      serializer = BookSerializer(data=items)
      data = {
         "status": f"Returned  books",
         "books": items
      }
      if serializer.is_valid():
         serializer.save()
         return Response(data, status = status.HTTP_201_CREATED)
      return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
   
#Detail view orqali Harbi ma'lumotni ko'rish
class BookDetailApiView(APIView):
   def get(self,requests,pk):
      try:
        items = Book.objects.get(id=pk)
        serializer_data = BookSerializer(items).data
        respons_data = {
         "status":"SUCCESSFULL",
         "book" : serializer_data
       }
        return Response(respons_data,status=status.HTTP_200_OK)
      except Exception:
        return Response(
           {"status":False,
            "massges":"Book is not found "},status=status.HTTP_404_NOT_FOUND)


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