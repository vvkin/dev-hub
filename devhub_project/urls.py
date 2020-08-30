from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Admin panel
    path('accounts/', include('django.contrib.auth.urls')), # Auth system (registration, login etc)
    path('accounts/', include('users.urls')), # All pages needed for user
    path('', include('pages.urls')) # Some basic pages
]
