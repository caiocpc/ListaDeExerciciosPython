"""
Faça um Programa que peça a temperatura 
em graus Celsius, transforme e mostre 
em graus Fahrenheit.
"""

temperatura = float(input('Temperatura em graus Celsius:\n'))
conversao = temperatura * 1.8000 +32

print(f'{conversao}°F')