#Ahora hagamos algunos cambios en la clase que creamos en el ejercicio anterior de Python.
#Primero haga su función para que tome los parámetros: x e y. x será el número que se eleva, e será la potencia. 
#¡Entonces, los usuarios pueden elevar los números a cualquier potencia! También cambiemos el nombre de la función a "ElevarAlaPotencia".
#También agreguemos una representación de cadena rápidamente, de modo que cuando un usuario imprima la clase obtenga una descripción significativa.
#Puede ser algo como: Esta clase consistirá en operaciones matemáticas. Solo tenemos una función llamada ElevarAlaPotencia.

class myfunc:
    def ElevarAlaPotencia(x,y):
        print("Esta clase consistirá en operaciones matemáticas. Solo tenemos una función llamada ElevarAlaPotencia.")
        return x**y
        
ans1 = myfunc.ElevarAlaPotencia(5, 6)
print(ans1)

x=input("Introduce la base numerica:")
y=input("Introduce la potencia de la base")
try:
    x=int(x)
    y=int(y)
    ans2=myfunc.ElevarAlaPotencia(x,y)
    print(ans2)
except ValueError:
    print("Introduce un numero valido")