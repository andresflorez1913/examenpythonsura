numero = 1
negativos = 0
positivos = 0
while (numero<=20):
    n = int(input(f'Ingresa el número {numero}: '))
    if(n<0):
        negativos+=1
    numero+=1

print(f'{negativos} son números son negativos')


