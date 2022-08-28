'''
Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros 
quadrados da área a ser pintada. Considere 
que a cobertura da tinta é de 1 litro para 
cada 6 metros quadrados e que a tinta é 
vendida em latas de 18 litros, que custam 
R$ 80,00 ou em galões de 3,6 litros, que 
custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
I.   Comprar apenas latas de 18 litros;
II.  Comprar apenas galões de 3,6 litros;
III. Misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
import math

metros = int(input('Metros:\n'))
cobertura_da_tinta = 6
lata_de_litro = 18
galao_de_litro = 3.6
preco_lata = 80
preco_galao = 25
porcentagem_de_sobra = 10
porcentagem = 100

area = metros / cobertura_da_tinta
lata = math.ceil(area / lata_de_litro)
galao = math.ceil(area / galao_de_litro)
margem_de_seguranca = metros + (metros * (porcentagem_de_sobra/porcentagem))
preco_total_lata = lata * preco_lata
preco_total_galao = galao * preco_galao
 

print(f'Você ira precisar de {lata} lata(s) de tinta que sairá a R$ {preco_total_lata}')
print(f'Você ira precisar de {galao} galão(ões) de tinta que sairá a R$ {preco_total_galao}')
print(f'Faltando o III')
