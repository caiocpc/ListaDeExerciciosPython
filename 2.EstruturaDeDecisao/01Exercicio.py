'''
Faça um Programa que peça dois números 
e imprima o maior deles.
'''

n = float(input('Digite primeiro número: '))
n2 = float(input('Digite o segundo número: '))

maior_n = n > n2
maior_n2 = n2 > n

if(maior_n):
    print(f'O maior número é o {n}')
elif(maior_n2):
    print(f'O maior número é o {n2}')
else:
    print('Os números são iguais.')
