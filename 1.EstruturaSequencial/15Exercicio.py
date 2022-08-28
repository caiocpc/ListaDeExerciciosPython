'''
Faça um Programa que pergunte quanto você 
ganha por hora e o número de horas 
trabalhadas no mês. 
Calcule e mostre o total do seu salário no 
referido mês, sabendo-se que são 
descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, 
faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

salario_por_hora = float(input('Digite o seu salário por hora trabalhada:\n'))
horas_trabalhada = float(input('Digite o total trabalhado no mês:\n'))
salario = salario_por_hora * horas_trabalhada
porcentagem = 100
ir= 11
inss = 8
sindicato = 5

imposto_renda = salario * (ir / porcentagem)
inss_desconto = salario * (inss / porcentagem)
sindicato_desconto = salario * (sindicato / porcentagem)

desconto = imposto_renda + inss_desconto + sindicato_desconto
salario_liquido = salario - desconto

print(f'+ Salário Bruto : R$ {salario:.2f}')
print(f'- IR ({ir}%) : R$ {imposto_renda:.2f}')
print(f'- INSS ({inss}%) : R$ {inss_desconto:.2f}')
print(f'- Sindicato ({sindicato}%) : R$ {sindicato_desconto:.2f}')
print('+------------------------------+')
print(f'|   + Salário Bruto: {salario:.2f}   |')
print(f'|      - Desconto: {desconto:.2f}      |')
print(f'|  = Salário Líquido: {salario_liquido:.2f}  |')
print('+------------------------------+')





