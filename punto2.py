print("***Salpicon sura***")

frutas=[]

for i in range(3):
    fruta={}
    fruta['nombre']=input(f'Ingrese el nombre de la fruta: ')
    fruta['color']=input(f'Ingrese el color de la fruta: ')
    fruta['precio']=input(f'Ingrese el precio de la fruta: ')
    frutas.append(fruta)

print("las frutas ingresadas son: ",frutas)