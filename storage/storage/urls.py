from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('docs.urls', namespace='docs')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
]
