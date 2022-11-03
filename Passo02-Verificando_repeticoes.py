import os

caminho = r"C:\Audios"
os.chdir(caminho)

# Criando listas vazias para preencher com os id's dos áudios
dois = []
tres = []
quatro = []
cinco = []
seis = []
sete = []
oito = []
nove = []
dez = []
onze = []
doze = []
outros = []

# Checando os arquivos em mp3 no diretório, abrindo o arquivo quantos.txt criado no Passo 01
# depois contando as ocorrências de repetição de nomes dos áudios
# Na minha estrutura Ura, os arquivos de áudios são salvos no formato: 1_xxxxxxxxxxxx_xxxxxxxxxxxx.mp3
# Nesse caso, estamos dividindo o nome do arquivo por _
# Depois estamos novamente adicionando o prefixo 1_ para fazer a contagem dos nomes
# Essa ação é necessária, pois encontrei áudios com as duas sequencias(xxxxxx_xxxxx) identicas, o que levava a contagem
# incorreta. Dessa forma evitamos isso.

for arq in os.listdir(caminho):
    if arq.endswith(".mp3"):
        a = arq.split("_")
        palavra = str(f'{a[0]}_{a[1]}')
        with open('quantos.txt') as f:
            ocorrencias = f.read().count(palavra)
        if ocorrencias == 2:
            dois.append(arq)
        elif ocorrencias == 3:
            tres.append(arq)
        elif ocorrencias == 4:
            quatro.append(arq)
        elif ocorrencias == 5:
            cinco.append(arq)
        elif ocorrencias == 6:
            seis.append(arq)
        elif ocorrencias == 7:
            sete.append(arq)
        elif ocorrencias == 8:
            oito.append(arq)
        elif ocorrencias == 9:
            nove.append(arq)
        elif ocorrencias == 10:
            dez.append(arq)
        elif ocorrencias == 11:
            onze.append(arq)
        elif ocorrencias == 12:
            doze.append(arq)
        else:
            outros.append(arq)


# Aqui estamos lendo as listas criadas e criando um arquivo txt separando áudios por vezes de repetição
# Ex: áudios que são necessários 2 concatenações, 3, 4 etc.

meus_audios = open("dois.txt", 'a')
for i in dois:
    meus_audios.write(i + '\n')
meus_audios.close()

meus_audios = open("tres.txt", 'a')
for i in tres:
    meus_audios.write(i + '\n')
meus_audios.close()

meus_audios = open("quatro.txt", 'a')
for i in quatro:
    meus_audios.write(i + '\n')
meus_audios.close()

meus_audios = open("cinco.txt", 'a')
for i in cinco:
    meus_audios.write(i + '\n')
meus_audios.close()

meus_audios = open("seis.txt", 'a')
for i in seis:
    meus_audios.write(i + '\n')
meus_audios.close()

meus_audios = open("sete.txt", 'a')
for i in sete:
    meus_audios.write(i + '\n')
meus_audios.close()

meus_audios = open("oito.txt", 'a')
for i in oito:
    meus_audios.write(i + '\n')
meus_audios.close()

meus_audios = open("nove.txt", 'a')
for i in nove:
    meus_audios.write(i + '\n')
meus_audios.close()

meus_audios = open("dez.txt", 'a')
for i in dez:
    meus_audios.write(i + '\n')

meus_audios = open("onze.txt", 'a')
for i in onze:
    meus_audios.write(i + '\n')

meus_audios = open("doze.txt", 'a')
for i in doze:
    meus_audios.write(i + '\n')

meus_audios = open("outros.txt", 'a')
for i in outros:
    meus_audios.write(i + '\n')