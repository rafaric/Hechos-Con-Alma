
from django.urls import path
from .views import CrearUsuarioView


urlpatterns = [
    path('registracion/', CrearUsuarioView.as_view(), name='registro')
]
