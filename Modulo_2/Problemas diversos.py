#1

import os
import val as v

Alum =[]
for i in range(0,v.alumnos):
    print(f"Ingrese datos del alumno {i+1} ")
    Datos={
        'Nombre': input('Nombre : '),
        'Nota 1': input('Nota 1 : '),
        'Nota 2': input('Nota 2 : '),
        'Nota 3': input('Nota 3 : ')
    }
    Alum.append(Datos)
print(Alum)

#2

aprobadas=0
desaprobadas=0
suma=0
sumapro=0
for i in range(0,v.alumnos):
    print("Ingrese nota del estudiante "+str(i+1)+": ")
    
    for n in range(0,3):
        notas=int(input("Ingrese nota  " +str(n+1)+": " ))
        suma=suma +notas
        promedio=suma/3
    pass
    if promedio>=4:
        aprobadas+=1
    else:
        desaprobadas+=1
print("la suma de notas es: ", suma)
print("cantidad de aprobados ", aprobadas)
print("cantidad de desaprobados ", desaprobadas)

#3

aprobadas=0
desaprobadas=0
suma=0
sumapro=0
for i in range(0,v.alumnos):
    print("Ingrese nota del estudiante "+str(i+1)+": ")
    
    for n in range(0,3):
        notas=int(input("Ingrese nota  " +str(n+1)+": " ))
        suma=suma +notas
        promedio=suma/3
    pass
print("la suma de notas es: ", suma)
print("promedio del curso es: ", suma/v.alumnos)

#4

Promedios=[]
for i in range(0,v.alumnos):
    print("Ingrese nota del estudiante "+str(i+1)+": ")
    sum=0
    for n in range(0,3):
        notas=int(input("Ingrese nota  " +str(n+1)+": " ))
        sum=sum+notas  
        prom=sum/3
    pass
    Promedios.append(prom)
    
print("El promedio es: ",Promedios)
maximo=max(Promedios)
minimo=min(Promedios)
if maximo>minimo:
    print("El promedio mayor es: ", maximo)
    print("El promedio menor es: ", minimo)

#5