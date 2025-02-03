from django.contrib import admin
from django.urls import path
from banks.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # New URL pattern for the index view
]
