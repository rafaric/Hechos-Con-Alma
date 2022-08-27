
from django.urls import path
from . import views
from .views import CrearCategoria, DetallePosteo, HomeView, CrearPosteo, ActualizarPosteo, BorrarPosteo, Categoria, Like, enviarMail

urlpatterns = [
    #path('', views.home, name='home'),
    path('bienvenida/', HomeView.as_view(), name='bienvenida'),
    path('', views.home, name='home'),
    path('posteo/<int:pk>/', DetallePosteo.as_view(), name='detalle_posteo'),
    path("agregar_posteo/", CrearPosteo.as_view(), name="agregar_posteo"),
    path("posteo/editar/<int:pk>/", ActualizarPosteo.as_view(), name="editar_posteo"),
    path("posteo/<int:pk>/borrar/", BorrarPosteo.as_view(), name="borrar_posteo"),
    path("agregar_categoria/", CrearCategoria.as_view(), name="agregar_categoria"),
    path('categoria/<str:cate>/', Categoria, name='categoria'),
    path('like/<int:pk>/', Like, name='like_post'),
    path('send_email/', views.enviarMail, name='mail'),
    path('quienessomos/', views.quienessomos, name='somos'),
]
