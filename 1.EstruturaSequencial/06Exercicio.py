# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
from cmath import pi
import math

raio = float(input('Insira o valor do raio: \n'))
pi = math.pi # função para o valor de PI
A = pi * math.pow(raio, 2) # Usando pow para realizar o calculo de potência

print(f'{A:.2f} Metros².') # (:.2f) formatando em duas casas 