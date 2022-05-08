# Algoritmo Estadistica
import random
ContH=0 #CONTADOR PARA HOMBRRES
ContM=0 #CONTADOR PARA MUJERES
print("\n Leemos datos 1 a 1")
HyM=[]
for i in range(0,100):
    HyM.append(random.randint(0,1)) # LLENAMOS LA LISTA
    if(HyM[i]==0):
        ContM=ContM+1 #SUMAMOS SI ES UNA MUJER
    if(HyM[i]==1):
        ContH=ContH+1 #SUMAMOS SI ES UN HOMBRE
print("\n Lista Completada sigue el menú para ver los resultados\n")
while(True):
    dec=input((" S=SALIR \n H = para ver numero de Hombres \n M = Para ver numero de Mujeres \n PH = Preguntar si hay mas Hombres que Mujeres \n PM = Preguntar si hay mas Mujeres que hombres \n PI = Preguntar si hay igualdad entre ambos \n"))
    dec=dec.upper()
    if(dec=="H"):
        print(f"\nLa cantidad de Hombres es:{ContH}\n")
    if(dec=="M"):
        print(f"\nLa cantidad de Mujeres es:{ContM}\n")
    if(dec=="PH"):
        if(ContH>ContM):
            print(f"\nEl numero de Hombres h:{ContH} es mayor al de Mujeres m:{ContM}\n")
        else:
            print(f"\nLa Cantidad de Hombres h:{ContH} no es mayor al de las Mujeres m:{ContM}\n")
    if(dec=="PM"):
        if(ContM>ContH):
            print(f"\nEl numero de Mujeres m:{ContM} es mayor al de Mujeres h:{ContH}\n")
        else:
            print(f"\nLa Cantidad de Mujeres m:{ContM} no es mayor al de los Hombres h:{ContH}\n")
    if(dec=="PI"):
        if(ContH==ContM):
            print(f"\nEl numero de Hombres n:{ContH} es igual al de Mujeres n:{ContM}\n")
        else:
            print("\nNo hay igualdad\n")       
    if(dec=="S"):
        print("\n Gracias por usar este programa")
        break







