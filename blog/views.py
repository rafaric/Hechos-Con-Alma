
from urllib import request
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from .models import Categoria, Post
from .forms import EdicionForm, PosteoForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.
#def home(request):
#    return render(request, 'home.html', {})


def Like(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('detalle_posteo', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-fecha']
    #context_object_name = 'posts'

    def get_context_data(self, *args, **kwargs):
        cat_menu = models.Categoria.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


def Categoria(request, cate):
    post_ordenados = Post.objects.filter(categoria=cate.replace('-', ' '))
    post_categorizados = post_ordenados.order_by('-fecha')
    return render(request, 'categorias.html', { 'cate': cate.title().replace('-',' '), 'post_categorizados': post_categorizados })


class DetallePosteo(DetailView):
    model = Post
    template_name = 'detalle_posteo.html'
    #context_object_name = 'post'

    def get_context_data(self, *args, **kwargs):
        cat_menu = models.Categoria.objects.all()
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes =  stuff.total_likes()
        context = super(DetallePosteo, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        return context

class CrearPosteo(CreateView):
    model = Post
    form_class = PosteoForm
    template_name = 'agregar_post.html'
    #fields = '__all__'
    #fields = ['titulo', 'contenido']

class ActualizarPosteo(UpdateView):
    model = Post
    form_class = EdicionForm
    template_name = 'editar_post.html'
    #fields =['titulo', 'contenido']

class BorrarPosteo(DeleteView):
    model = Post
    template_name = 'borrar_post.html'
    success_url = reverse_lazy('home')


class CrearCategoria(CreateView):
    model = Categoria
    #form_class = PosteoForm
    template_name = 'agregar_categoria.html'
    fields = '__all__'
    #fields = ['titulo', 'contenido']

def home(request):
    return render(request, 'bienvenida.html', {})