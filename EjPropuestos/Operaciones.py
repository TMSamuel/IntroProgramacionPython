nro=input("Introduce un numero: ")
if(nro.isdigit()):
    nro=int(nro)
    print(f"Operación suma de {nro}+{nro}:",nro+nro)
    print(f"Operación resta de {nro}-{nro}:",nro-nro)
    print(f"Operación multiplicación de {nro}x{nro}:",nro*nro)
    print(f"Operación división de {nro}/{nro}:",nro/nro)
else:
    print("Introduce un numero valido")
    
