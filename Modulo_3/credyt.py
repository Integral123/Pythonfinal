def validar(tarj):
    
    t = ""
    x = ""
    par = 0
    impar = 0
    
    if not tarj.isdigit():
        return 1,""

    if len(tarj)<14 or len(tarj) > 17:
        return 2,""

    for i in range(0,len(tarj),2):
        x=str(int(tarj[i])*2)

        if len(x) == 2:
            par+=(int(x[0])+int(x[1]))

        else:
            par+=int(x)

    for i in range(1,len(tarj),2):
        impar+= int(tarj[i])

    if(par + impar) % 10 != 0:
        return 3," "

    if int(tarj[0:2]) > 49 and int(tarj[0:2]) < 56:
        t = "MasterCard"

    if tarj[0:2] == "34" or tarj[0:2] == "37":
        t = " American Express"

    if tarj[0] == "4":
        t = "VISA"

    return 4,t

msg = (0,"")

while msg[0] != 4:

    msg = validar(input('Ingrese Numero de tarjeta :'))
    if msg[0] == 1: 
        print("Ingrese solo numeros  0-9 ")

    if msg[0] == 2:
        print("Se admite valores mayores a 13 digitos y menores a 16 digitos ")
        
    if msg[0] == 3:   
        print("Numero invalido")
        
print('Tipo : ' + msg[1])
print('Tarjeta Valida')