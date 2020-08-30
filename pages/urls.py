from django.urls import path
from .views import home_page_view


urlpatterns = [
    path('', home_page_view, name='home'),
    # Here will be patterns for some pages like main page, about page etc.
]