'''
Faça um Programa que peça 2 números inteiros 
e um número real. Calcule e mostre:
A. o produto do dobro do primeiro com metade do segundo.
B. a soma do triplo do primeiro com o terceiro.
C. o terceiro elevado ao cubo.
'''
import math

n  = int(input('Digite primeiro número inteiro:\n'))
n2 = int(input('Digite segundo número inteiro:\n'))
n3 = float(input('Digite terceiro número real:\n'))

a = n*n
a2 = n2/2
b = (n*3) + n3
c = math.pow(n3, 3) #(n3 ** 3)

print(f'Dobro do primeiro que é {a} com a metade do segundo que é {a2}')
print(b)
print(c)