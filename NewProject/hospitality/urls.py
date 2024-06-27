# hospitality/urls.py

from django.contrib import admin
from django.urls import path
from allocation.views import upload_csv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload-csv/', upload_csv, name='upload_csv'),
]
