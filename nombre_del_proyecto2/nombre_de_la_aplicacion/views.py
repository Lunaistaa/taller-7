from django.shortcuts import render
from .models import TipoDocumento
from django.http import JsonResponse

def obtener_tipodocumento(request):
    tipodocumentos = TipoDocumento.objects.all()
    context = {'tipodocumentos': tipodocumentos}
    return render(request, 'nombre_de_la_aplicacion/tipodocumento.html', context)

def tipodocumento_list(request):
    tipodocumentos = TipoDocumento.objects.all()
    tipodocumentos_data = [
        {
            'id': tipodocumento.id,
            'nombre': tipodocumento.nombre,
            'descripcion': tipodocumento.descripcion
        }
        for tipodocumento in tipodocumentos
    ]
    return JsonResponse(tipodocumentos_data, safe=False)