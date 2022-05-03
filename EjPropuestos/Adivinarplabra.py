# Adivinar palabra
palabra=input("intruduce la palabra base: ")
while(True):
    adiv=input("Intenta adivinar la palabra (N para salir): ")
    if(palabra==adiv):
        print("Genial has adivinado la palabra!!")
        break
    if(adiv=='N'):
        break 
    else:
        print("No has adivinado la palabra sigue intentandolo: ")

