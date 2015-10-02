from django.shortcuts import render

# Create your views here.
def listar_publicaciones(request):
    return render(request, 'blog/listar_publicaciones.html', {})
