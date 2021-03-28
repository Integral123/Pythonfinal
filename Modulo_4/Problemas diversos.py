#problema1:
with open('./src/tabla-n.txt','a') as f:
    f.write('\nmás lineas')
    pass

fichero = open('./src/tabla-n.txt','w')
fichero.write("La tabla de multiplicar ")
fichero.write('\n')
texto = int(input("Ingrese un numero [1-10] : "))
for j in range(0,13):
    p=j*texto 
    fichero.write(str(texto)) 
    fichero.write("x") 
    fichero.write(str(j)) 
    fichero.write(" = ") 
    fichero.write(str( p ))    
    fichero.write('\n')
fichero.close()

#problema2:

import os

fichero = open('./src/tabla-n.txt','w')
if os.path.exists('./src/tabla-n.txt'):
    print("El archivo existe")   
    fichero.write("La tabla de multiplicar ")
    fichero.write('\n')
    texto = int(input("Ingrese un numero [1-10] : "))
    for j in range(0,13):
        p=j*texto 
        fichero.write(str(texto)) 
        fichero.write("x") 
        fichero.write(str(j)) 
        fichero.write(" = ") 
        fichero.write(str( p ))    
        fichero.write('\n')
        print(f"{texto}x{j}={p}")
else:
    print("El archivo no exixte")
fichero.close()

#ultimo: ya estaba :,v


regex = r""

emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']
for example in emails:

    if re.match(regex, example):

        print("The email {email_example} is a valid email".format(email_example=example))
    else:
        print("The email {email_example} is invalid".format(email_example=example))   