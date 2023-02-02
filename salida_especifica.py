import json

with open("PythonDevTestJson.json") as archivo:
   datos=json.load(archivo)
   print(datos["OpenPositions"][5]["RequestedBy"])
    