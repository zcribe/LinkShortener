from django.urls import path, include
from .views import index_view, response_view, redirect_view

urls = [
    path('', index_view),
    path('link', response_view),
    path('re/<slug:slug>', redirect_view)
]