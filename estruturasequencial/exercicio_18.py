# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
# (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo = float(input('Digite o tamanho do arquivo em (MB): '))
velocidade_de_download = float(input('Digite a velocidade da internet em (Mbps): '))
tempo = arquivo / velocidade_de_download
download_em_minutos = tempo * 60
print(f'O tempo aproximado de download será de: {download_em_minutos:.0f} minutos')
