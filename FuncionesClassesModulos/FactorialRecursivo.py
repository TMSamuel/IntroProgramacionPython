def Factorial(N):
    if N <=0:
        #Continuara ...
        raise
    if N <= 1:
        return 1
    else:
        print("return {} Factorial de ({}-1)".format(N,N))
        return N * Factorial(N-1)
        
n=input("Desea calcular el factorial de (Entre un numero):")
try:   
    n=int(n)
    r=Factorial(n)
    print("El factorial de:",n,"es",r)
except TypeError:
    print("Entre un numero valido")
except:
    print('No se permiten valores menores a 0')