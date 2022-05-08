#EDADES
import random
edades=[]
cont18=0
print("\nCompletamos la lista de las edades\n")
for i in range(0,100):
    edades.append(random.randint(1,120)) # LLENAMOS LA LISTA
    if(edades[i]>=18):
        cont18=cont18+1
media=(sum(edades))/100
print("Hay",cont18,"personas mayores de 18 años")
print("El mayor del grupo tiene",max(edades),"años")
print("El menor del grupo tiene",min(edades),"años")
print("La edad media es de {:.0f}".format(media),"años")  
