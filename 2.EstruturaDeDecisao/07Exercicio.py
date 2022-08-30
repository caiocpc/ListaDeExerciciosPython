'''
Faça um Programa que leia 
três números e mostre o 
maior e o menor deles.
'''
n = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

n_maior = n > n2 and n > n3
#n_menor = n < n2 and n < n3
n2_maior = n2 > n and n2 > n3
#n2_menor = n2 < n and n2 < n3
n3_maior = n3 > n and n3 > n
#n3_menor = n3 < n and n3 < n2

if(n_maior and n2 < n3):
    print(n, n2)
elif(n_maior and n3 < n2):
    print(n, n3)
elif(n2_maior and n < n3):
    print(n2, n)
elif(n2_maior and n3 < n2):
    print(n2, n3)
elif(n3_maior and n2 < n):
    print(n3, n2)
elif(n3_maior and n < n2):
    print(n3, n)
else:
    print('Tem números repetidos')

