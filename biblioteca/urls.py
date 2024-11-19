from django.contrib import admin
from django.urls import path, include  # Adicione a importação do include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # Adicione esta linha para incluir as URLs do aplicativo core
]