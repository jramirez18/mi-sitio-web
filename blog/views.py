from django.shortcuts import render
from django.utils import timezone
from .models import Postear

# Create your views here.
def listar_publicaciones(request):
    publicaciones= Postear.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar_publicaciones.html', {'publicaciones':publicaciones})
