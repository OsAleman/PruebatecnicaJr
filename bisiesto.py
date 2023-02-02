anio=int(input("Ingrese un anio:"))
if(anio % 4==0):
    if(anio % 100!=0 or anio % 400==0):
            print("El anio",anio,"es BISIESTO")
else:
    print("El anio",anio,"NO ES BISIESTO")
    
