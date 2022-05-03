# Números primos
num = input("Introduce un número: ")
div = 2
Prim = True
if(num.isdigit()):
    num=int(num)
    if(num==1):
        print(f"El Numero {num} es primo")
    else:
        while(Prim == True and num>div):
            if(num%div == 0):
                Prim=False
            else:
                div=div+1
        #FIN MIENTRAS
    if(Prim == True):
        print(f"El Numero {num} es primo")
    else:
        print(f"El Numero {num} no es primo")
else:
    print("Introduzca un numero entero")
