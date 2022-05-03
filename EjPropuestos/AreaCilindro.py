# Area y Volumen de un cilindro
import math
Rd=input("Introduce el Radio: ")
Ho=input("Introduce el Ho: ")
if(Rd.isdigit() and Ho.isdigit()):
    Rd=int(Rd)
    Ho=int(Ho)
    pi=math.pi
    print(f"El Area del Cilindro es:",(pi*2)*Rd*Ho+(pi*2)*(Rd*Rd),"y el Volumen del Cilindro es:",pi*(Rd*Rd)*Ho)
else:
    print("Introduce un numero valido")