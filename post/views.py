from django.shortcuts import render
from .models import Area, Post
# Create your views here.

def home(request):
    posts = Post.objects.filter(area=2).order_by('-fechaHora')[:1] | Post.objects.filter(area=1).order_by('-fechaHora')[:1]
    return render(request, 'index.html', {'posts': posts})