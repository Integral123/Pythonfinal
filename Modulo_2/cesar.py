import string

def num(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False

pasos = input("Ingrese el rango")

while num(pasos) is False:
    pasos = input('El dato que ingreso no es un numero o es un numero negativo: ')
    
t = input("Ingrese el texto")

sub = []

n = ""


for i in t:
    
    if i in string.ascii_lowercase:
        indice = string.ascii_lowercase.index(i)
        nuevo_indice = (indice + int(pasos)) % 26
        sub.append(string.ascii_lowercase[nuevo_indice])
        
    elif i in string.ascii_uppercase:
        indice = string.ascii_uppercase.index(i)
        nuevo_indice = (indice + int(pasos)) % 26
        sub.append(string.ascii_uppercase[nuevo_indice])
        
    else:
        sub.append(i)
        
for i in sub:
    n = n + i

print(n)