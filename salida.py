import json


    
def cargarDatos(ruta):
    with open(ruta) as contenido:
        resultado =json.load(contenido)
        print(resultado)

ruta = 'PythonDevTestJson.json'
cargarDatos(ruta)
