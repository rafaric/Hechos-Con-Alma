from unicodedata import name
from django.db import models

from accounts.models import User

# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    id= models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, null=False, blank=False)
    fechaHora = models.DateTimeField(auto_now_add=True)
    textoLargo = models.TextField()
    contador = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='img', blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-fechaHora']
    
    def __str__(self):
        return self.titulo
    