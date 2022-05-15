def ProcesoInicial():
    print("Buscar una hoja de papel")

def ProcesoDos():
    print("Doblar la hoja")

def SaludarATodos(*nombres):
    for i in nombres:
        print(f"Hola:{i}")

def SaludarATodosDicc(**nombres):
    for i in nombres:
        print(f"Hola:{i} {nombres[i]}")

def ciudad(ciudad):
    print(ciudad)

ProcesoInicial()
ProcesoDos()

Colores=["Azul","Rojo","Amarillo"]

SaludarATodos("Olga")
SaludarATodos("Rafaela","Carla","Pedro")
SaludarATodos("Diego","Cynthia","Alvaro","Emiliano")
SaludarATodos(345,"Miriam",True)
SaludarATodos(Colores,"Hola")

SaludarATodosDicc(nombre="Billy",ape="Vanegas")

ciudad("Bogota","Colombia")
ciudad("Mexico","Ciudad de Mexico")
ciudad("Norguega","Oslo")