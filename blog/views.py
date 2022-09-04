from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Post, Categoria
from datetime import date

def home(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado=True)
    fecha = date.today()
    anio = fecha.strftime('%Y')
    print(anio)

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) | Q(descripcion__icontains = queryset)
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {'posts': posts, 'anio': anio} 

    return render(request, 'index.html', context)

def detalle_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post':post}
    return render(request, 'post.html', context)
