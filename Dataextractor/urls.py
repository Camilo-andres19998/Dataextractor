from django.contrib import admin
from django.urls import include, path
from Appdataextractor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('informacion/', include('Appdataextractor.urls')),
    path('ver_informacion/', views.ver_informacion, name='ver_informacion'),
]
