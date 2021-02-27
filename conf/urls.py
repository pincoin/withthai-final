from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',
         views.HomeView.as_view(), name='home'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns \
                  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
                  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
