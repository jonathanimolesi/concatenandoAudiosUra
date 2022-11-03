import os

# Caminho onde estão todos os áudios para serem analisados
caminho = r"C:\Audios"
os.chdir(caminho)

# Criando arquivo listando todos os áudios
meus_audios = open("quantos.txt", 'a')
for arq in os.listdir(caminho):
    meus_audios.write(arq + '\n')