def Fibonacci(N):
    if N < 2:
        return N
    else:
        return Fibonacci(N-1) + Fibonacci(N-2)

n=input("Que numero de la serie de Fibonacci quiere (Introduce un numero):")
try:
    n=int(n)
    serie_fibonacci=[]
    if(n>0):
        Num=n-1
        for i in range(0,n):
            actual=Fibonacci(i)
            serie_fibonacci.append(actual)
        print("El numero es:",actual)
        print("La serie es:",*serie_fibonacci)
    else:
        print("Debe entrar numero mayor que 0")
except ValueError:
    print("Entre un numero valido")
except:
    print("introduce un numero mayor que 0")