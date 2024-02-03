from django.contrib import admin
from django.urls import path, include
from ChainTech.views import Hello

urlpatterns = [
    path("admin/", admin.site.urls),
    path('hello/', Hello),
    path('', include('my_app.urls')),
    
]
