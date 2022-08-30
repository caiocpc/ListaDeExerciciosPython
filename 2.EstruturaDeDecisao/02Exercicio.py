"""
Faça um Programa que peça um valor e mostre 
na tela se o valor é positivo ou negativo.
"""

n = float(input('Digite um número: '))
negativo = n < 0

if(negativo):
    print('Negativo')
else:
    print('Positivo')
