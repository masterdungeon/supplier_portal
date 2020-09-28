from django.urls import path

from .views import IndexView, RegistrationView, GetProfileView


urlpatterns = [
    path('', (IndexView.as_view()), name='index'),
    path('registration/', (RegistrationView.as_view()), name='registration'),
    path('get_profile/', (GetProfileView.as_view()), name='get_profile'),
]
