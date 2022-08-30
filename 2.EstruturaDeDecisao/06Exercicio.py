'''
Faça um Programa que leia 
três números e mostre o 
maior deles.
'''

n = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

n_maior = n > n2 and n > n3
n2_maior = n2 > n and n2 > n

if(n_maior):
    print(n)
elif(n2_maior):
    print(n2)
else:
    print(n3)