#Ahora imprima el origen del primer_elemento.
class Jets:
    model = None
    country = 0
    def __init__(self, name, country,cantidad=0):
        self.name = name
        self.origin = country
        self.quantity = cantidad
        
    def __str__(self):
        return "{}->{}".format(self.name,self.origin)

first_item = Jets("F16", "USA",87)
#Imprimir el nombre del primer_elemento.
a=first_item.name
#print(a)
b=first_item.origin
#print(b)
second_item=Jets("SU33","Russia")
third_item=Jets("AJS37","Sweden")
fourth_item=Jets("Mirage2000","France",35)
fifth_item=Jets("Mig29","USSR")
sixth_item=Jets("A10","USA")
#first_army=[first_item.name,second_item.name,third_item.name,fourth_item.name,fifth_item.name,sixth_item.name]
first_army=[str(first_item),str(second_item),str(third_item),str(fourth_item),str(fifth_item),str(sixth_item)]
print(first_army)

#Agregue otro atributo llamado "cantidad" al método de inicialización (generalmente denominado constructor o init).
# Luego defina "asignar" este atributo al atributo self.quantity dentro del constructor
# Luego cree 2 instancias para: F14 y Mirage2000 con cantidades 87 y 35.
first_item = Jets("F16", "USA",87)
second_item=Jets("Mirage2000","France",35)
total=first_item.quantity + second_item.quantity
print("Respuesta ejrcicio :",total)