def num(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False


n = input('Escriba un número entero: ')

while num(n) is False:
    n = input('El numero que ingreso no es un numero: ')

n = int(n)    
    
while n < 0 or n > 8:
    n = int(input("Ingrese un valor entre 1 y 8: "))

for i in range (n+1):
    print(" "*(n-i)+"#"*i)