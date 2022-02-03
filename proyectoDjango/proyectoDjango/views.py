from contextvars import Context
from django.http import HttpResponse

from django.template import Template

from django.template.context import Context

from datetime import  datetime

def saludo(request):
    return HttpResponse('HOLA PRIMERA PAGINA caca pedooooooooooooooooooooooooooooooooooooooooooooooooooooo')

def dia_De_Hoy(request):
    return HttpResponse(f"hoy es: {datetime.now()}") 

def nombre_de(request,nombre):
    return HttpResponse(f'HOLAAAA!! {nombre}' )

def template1(request):
    template_1 = open('proyectoDjango/templates/primerTemplate.html')
    template = Template(template_1.read())
    template_1.close()
    
    contexto = Context()
    
    documento = template.render(contexto)
    
    return HttpResponse(documento)

def en_que_ano_naciste(request,edad):
    año_actual = datetime.now().year
    edad_int = int(edad)
    return HttpResponse(f'Hola vos naciste masomenos en el año {año_actual - edad_int}')
