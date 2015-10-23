from django.shortcuts import render, get_object_or_404 #ERROR QUE DAN LAS PAGINAS WEB CUANDO INTENTAMOS ENTRAR A UNA PAG Q NO EXISTE
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Postear
from .forms import PostForm

# Create your views here.
def listar_publicaciones(request):
    publicaciones= Postear.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar_publicaciones.html', {'publicaciones':publicaciones})

def detalle_publicaciones(request, pk):
    post = get_object_or_404(Postear, pk=pk)
    return render(request, 'blog/detalle_publicaciones.html', {'post': post})

def nuevo_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('blog.views.detalle_publicaciones', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/editar_post.html', {'form': form})

def editar_post(request, pk):
        post = get_object_or_404(Postear, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.save()
                return redirect('blog.views.detalle_publicaciones', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/editar_post.html', {'form': form})
