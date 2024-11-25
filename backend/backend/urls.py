from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('automata/', include('automata.urls')),
    path('auth/', include('authentication.urls')),
]
