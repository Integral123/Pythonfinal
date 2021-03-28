import string

print(string.ascii_lowercase)

ll = input("Ingrese el abecedario alterado que desea: ")

s = input("Ingrese oracion que quiere encriptar con el abecedario anteriormente proporcionado: ")

ll = ll.lower()

s=s.lower()

acumulador=[]

for i in s:    
    for j in string.ascii_lowercase:
        indice = string.ascii_lowercase.index(j)
        if i == j:


            for k in ll:
                indice1 = ll.index(k)
                if j == k:
                    acumulador.append(indice1) 




acumulador1=[]
for i in acumulador:    
    acumulador1 = acumulador1 + [i]    

h = ""  

for i in acumulador1:
    h = h + string.ascii_lowercase[i]
print (h)