from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('api.urls')),
    path('', Home.as_view(),name="home"),
    
]+ static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
