
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        #return reverse('detalle_posteo', args=(str(self.id,)))
        return reverse('home')


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = RichTextField(blank=True, null=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='images/')
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.TextField(max_length=100, default='General')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo + ' - ' + self.autor.username
    
    def get_absolute_url(self):
        #return reverse('detalle_posteo', args=(str(self.id,)))
        return reverse('home')

    def total_likes(self):
        return self.likes.count()

class Suscriptores(models.Model):
    apellido = models.CharField(max_length=50, null=False)
    nombre = models.CharField(max_length=120, null=False)    
    correo = models.EmailField(max_length=80, null=False)

    def __str__(self):
        return self.apellido + ', ' + self.nombre + ' - ' + self.correo