'''
Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em 
metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 
1 litro para cada 3 metros quadrados e que 
a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a 
quantidades de latas de tinta a serem 
compradas e o preço total.
'''
import math

metros = int(input('Metros:\n'))
cobertura_da_tinta_por_litro = 3
lata_de_tinta = 18
preco = 80

area = metros / cobertura_da_tinta_por_litro
lata = math.ceil(area / lata_de_tinta)# Ceil arredonda números inteiros para mais.
preco_total = area * preco

print(f'Você vai precisar de {lata} lata(s) de tinta e o preço total de {preco_total:.2f} reais.')

