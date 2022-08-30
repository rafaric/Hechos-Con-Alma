

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from .models import Categoria, Post, Suscriptores
from .forms import EdicionForm, PosteoForm, suscripcion
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.contrib import messages
import environ
#from .tasks import emailsendertask


# Create your views here.
#def home(request):
#    return render(request, 'home.html', {})





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
        
        
        context = super(DetallePosteo, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        
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
    context = model.objects.all().order_by('-fecha')[:3]
    form = suscripcion()
    if request.method == 'POST':
        #print(request.POST)
        form = suscripcion(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'bienvenida.html', {'context':context, 'form':form})



def enviarMail(request):
    env = environ.Env()
    environ.Env.read_env()
    recipient = Suscriptores.objects.all()
    receiver_address = []
    for i in recipient:
        receiver_address.append(i.correo)
    
    mail_content = '''
        <div id="intro" class="bg-image shadow-2-strong">
            <div class="mask" style="background-color: #98dcdacc;">
                <div class="container d-flex align-items-center justify-content-center text-center h-100">
                <div class="text-white">
                    <h1 class="mb-3" style="text-align: center;">Hechos Con Alma</h1>
                    <h3 class="mb-4" id="lema" style="text-align: center;">No es por Vista, es por Fe</h3>
                    
                </div>
                </div>
            </div>
            </div>
            <!-- Background image -->

        <!--Main Navigation-->

        <!--Main layout-->


            
            
            <section>
                <div class="row">
                <div class="col-md-4 gx-5 mb-4">
                    <p >
                        <div class="mask" style="text-align: center; background-color: hwb(182 61% 16% / 0.39); font-size: 26;">¡Hemos subido nuevo contenido
                        a nuestra página web!! ¡Vé a echarle un vistazo haciendo click en nuestro logo!</div>
                    </p>
                    
                    </div>
                </div>
                </div>
                <div style="text-align: center;">
                    <a style="margin-left: auto; margin-right: auto;" href="http://www.google.com" target="_blank"><img src="https://i.postimg.cc/9FnVBbSJ/Hc-A-sin-fondo.png" alt=""></a>
                </div>
            </section>
    '''

    #sender_address = 'hechosconalmablog@gmail.com'
    #sender_pass = 'rsooofxrvvuertno'  
    for i in receiver_address:
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = env("MAILFROM")
        message['To'] = i
        message['Subject'] = 'Nuevo contenido en Hechos con Alma!'  # The subject line
        # The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'html'))
        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(env("MAILFROM"), env("MAILPASS"))  # login with mail_id and password
        text = message.as_string()
        session.sendmail(env("MAILFROM"), i, text)
        session.quit()
        print('Mail Sent')
    return render(request, 'enviocorreo.html', {})

def quienessomos(request):
    return render(request, 'quienessomos.html', {})
def proyectos(request):
    return render(request, 'proyectos.html', {})
def ayudas(request):
    return render(request, 'voluntariado.html', {})
def tienda(request):
    return render(request, 'tienda.html', {})
def duelo(request):
    return render(request, 'duelo.html', {})
def huerta(request):
    return render(request, 'huerta.html', {})
def merendero(request):
    return render(request, 'merendero.html', {})
def objetivos(request):
    return render(request, 'objetivos.html', {})
def radio(request):
    return render(request, 'radio.html', {})
def religion(request):
    return render(request, 'religion.html', {})

def suscribir(request):
    form = suscripcion()
    return render(request, 'bienvenida.html', {'form':form})

def post_likes(request, pk):
    model = Post
    post = model.objects.get(pk=pk)
    identify_post = 'has_liked '+str(post.id)
    if request.session.get(identify_post, False):
        messages.success(request, 'Ya has dado me gusta')
        return redirect('detalle_posteo', pk)
    post.likes = post.likes + 1
    post.save()
    request.session[identify_post] = True
    messages.success(request, 'Gracias por dar Me Gusta!')
    return redirect('detalle_posteo', pk)