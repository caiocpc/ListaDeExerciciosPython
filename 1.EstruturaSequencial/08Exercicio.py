"""
Faça um Programa que pergunte quanto você ganha por 
hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.
"""

valor_hora = float(input('Digite o seu sálario por hora trabalhada:\n'))
hora = float(input('Digite o número de horas trabalhada no mês:\n'))
salario = valor_hora * hora

print(f'{salario:.2f}')
