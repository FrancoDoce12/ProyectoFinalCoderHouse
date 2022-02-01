from django.http import HttpResponse

from datetime import  datetime

def saludo(request):
    return HttpResponse('HOLA PRIMERA PAGINA caca pedooooooooooooooooooooooooooooooooooooooooooooooooooooo')

def dia_De_Hoy(request):
    return HttpResponse(f"hoy es: {datetime.now()}") 

def nombre_de(request,nombre):
    return HttpResponse(f'HOLAAAA!! {nombre}')

