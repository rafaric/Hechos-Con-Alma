
from django.urls import path
from . import views

from .views import CrearCategoria, DetallePosteo, HomeView, CrearPosteo, ActualizarPosteo, BorrarPosteo, Categoria, post_likes

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
    #path('like/<int:pk>/', Like, name='like_post'),
    path('send_email/', views.enviarMail, name='mail'),
    path('quienessomos/', views.quienessomos, name='somos'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('ayudas/', views.ayudas, name='ayudas'),
    path('tienda/', views.tienda, name='tienda'),
    path('duelo/', views.duelo, name='duelo'),
    path('huerta/', views.huerta, name='huerta'),
    path('merendero/', views.merendero, name='merendero'),
    path('objetivos/', views.objetivos, name='objetivos'),
    path('radio/', views.radio, name='radio'),
    path('religion', views.religion, name='religion'),
    path('likes/<int:pk>',views.post_likes, name='likes'),
]
