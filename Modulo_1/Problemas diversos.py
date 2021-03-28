#Problema1:

c = float(input("Ingrese Cantidad a depositar: "))

i = 0.04

for j in range (1,4):
    a = c*((1+i)**j)
    print("La cantidad del ",j,"° año es: {0:.2f}".format(a))

#Problema2:

import math

a=int(input("Introduzca el primer coeficiente:"))
b=int(input("Introduzca el segundo coeficiente:"))
c=int(input("Introduzca el tercer coeficiente:"))

if a != 0:
    dis = (b**2)-4*a*c
    
    if dis > 0:
        print("Tiene 2 soluciones distintas:")
        Sol1= (-b +  math.sqrt(dis))/(2*a)
        Sol2= (-b -  math.sqrt(dis))/(2*a)
        print("X1:",Sol1)
        print("X2:",Sol2)
    elif dis == 0:
        print("Una solucion doble:")
        Sol1= (-b +  math.sqrt(dis))/(2*a)
        Sol2= (-b -  math.sqrt(dis))/(2*a)
        print("X1:",Sol1)
        print("X2:",Sol2)
    else:
        print("No tiene solucion real")