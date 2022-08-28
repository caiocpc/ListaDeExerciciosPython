'''
Faça um programa que peça o tamanho de 
um arquivo para download (em MB) e a 
velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de 
download do arquivo usando este link 
(em minutos).
'''

arquivo = int(input('Digite o tamanho do arquivo em MB: '))
velocidade = 10
velocidade_de_download = arquivo * 1000
tempo_de_download = velocidade_de_download / 1250


print(f'O tempo aproximadamente de download é de {tempo_de_download:.0f} segundos.')