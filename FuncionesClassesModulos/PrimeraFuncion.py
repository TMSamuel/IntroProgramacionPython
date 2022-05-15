from inspect import Attribute


def saludar(nombre):
    print(f"Hola {nombre}")

def sumar(a,b):
    return (a+b)

def addColores(colores,color):
    try: 
        colores.append(color)
        return True
    except AttributeError:
        return False


saludar('Samuel')
saludar('Billy')
saludar('Helena')


print(sumar(5,5))
print(sumar(7,5))

Colores=[]
addColores(Colores,'Azul')
addColores(Colores,'Rojo')
addColores(Colores,'Verde')
addColores(Colores,'Negro')