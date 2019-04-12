from django.urls import path, include
from .views import index_view, response_view

urls = [
    path('', index_view),
    path('link', response_view)
]