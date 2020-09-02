from django.urls import path, re_path
from users import views

urlpatterns = [
    path('signup/', views.signUp, name='signup'),
    path('activation_sent/', views.AccountActivationSent.as_view(), name='activation_sent'),
    # pattern for activation url
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]