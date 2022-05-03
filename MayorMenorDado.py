# Mayor menor numero dado
nro = input("Introduce un número: ")
dado=10
if(nro.isdigit()):
    nro=int(nro)
    if(nro<dado):
        print(f"El numero que has introducido es menor que: {dado}")
    if(nro>dado):
        print(f"El numero que has introducido es mayor que: {dado}")
    if(nro==dado):
        print(f"El numero que has introducido es igual que: {dado}")
else:
    print("Introduce un numero valido")
