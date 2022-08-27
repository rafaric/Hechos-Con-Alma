
from urllib import request
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from .models import Categoria, Post
from .forms import EdicionForm, PosteoForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



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
    una_cate = models.Categoria.objects.filter(nombre=cate.replace('-', ' '))
    context = una_cate.get()
    descripcion = context.descripcion
    print(descripcion)
    post_categorizados = post_ordenados.order_by('-fecha')
    return render(request, 'categorias.html', { 'cate': cate.title().replace('-',' '), 'post_categorizados': post_categorizados, 'descri':context.descripcion})


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
       
    
    def get_success_url(self) -> str:
        return reverse_lazy('mail')

class ActualizarPosteo(UpdateView):
    model = Post
    form_class = EdicionForm
    template_name = 'editar_post.html'
    success_url: reverse_lazy("editar_posteo")
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
    model = Post
    ordering = ['-fecha']
    context = model.objects.all().order_by('-fecha')[:3]
    return render(request, 'bienvenida.html', {'context':context})




def enviarMail(request):
    mail_content = '''
    <h1>Hemos subido nuevo contenido a nuestra pagina web!! Vé a hecharle un vistazo!</h1>
    <a href="https://www.google.com">Hechos con Alma</a>
    '''

    sender_address = 'hechosconalmablog@gmail.com'
    sender_pass = 'rsooofxrvvuertno'
    receiver_address = ['rafaelstrongoli@gmil.com', 'supercuentas2000@gmil.com','rubeneduardoescobar@gmil.com']  
    for i in receiver_address:
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = i
        message['Subject'] = 'Nuevo contenido en Hechos con Alma!'  # The subject line
        # The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'html'))
        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(sender_address, sender_pass)  # login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, i, text)
        session.quit()
        print('Mail Sent')
    return render(request, 'enviocorreo.html', {})

def quienessomos(request):
    return render(request, 'quienessomos.html', {})
def proyectos(request):
    return render(request, 'proyectos.html', {})
def ayudas(request):
    return render(request, 'donaciones.html', {})