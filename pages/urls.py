from django.urls import path
from .views import base_page_view


urlpatterns = [
    path('', base_page_view, name='base_page'),
    # Here will be patterns for some pages like main page, about page etc.
]