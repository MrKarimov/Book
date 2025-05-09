
from django.contrib import admin
from django.urls import path,include

#swagger and redoct uchun
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title = "Elektron kutubxona",
        default_version = "v1",
        description = "Ushbu api orqali Elektron kutubxon ma'lumotlarini ko'rish o'zgartirish taxrirlash mumkin!",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="islom199906@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public = True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('books.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
