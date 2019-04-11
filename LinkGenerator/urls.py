from django.urls import path, include
from .views import index_view

urls = [
    path('', index_view)
]