import os
import shutil
import sys
from pydub import AudioSegment

origem = r"C:\Audios"

# Criando as pastas
os.mkdir(r"C:\Audios/PastaDois")
os.mkdir(r"C:\Audios/PastaTres")
os.mkdir(r"C:\Audios/PastaQuatro")
os.mkdir(r"C:\Audios/PastaCinco")
os.mkdir(r"C:\Audios/PastaSeis")
os.mkdir(r"C:\Audios/PastaSete")
os.mkdir(r"C:\Audios/PastaOito")
os.mkdir(r"C:\Audios/PastaNove")
os.mkdir(r"C:\Audios/PastaDez")
os.mkdir(r"C:\Audios/PastaOnze")
os.mkdir(r"C:\Audios/PastaDoze")

# Criando variaveis para cada pasta
caminho2 = r"C:\Audios\PastaDois"
caminho3 = r"C:\Audios\PastaTres"
caminho4 = r"C:\Audios\PastaQuatro"
caminho5 = r"C:\Audios\PastaCinco"
caminho6 = r"C:\Audios\PastaSeis"
caminho7 = r"C:\Audios\PastaSete"
caminho8 = r"C:\Audios\PastaOito"
caminho9 = r"C:\Audios\PastaNove"
caminho10 = r"C:\Audios\PastaDez"
caminho11 = r"C:\Audios\PastaOnze"
caminho12 = r"C:\Audios\PastaDoze"

os.chdir(origem)

# Lendo arquivos que contém 2 repetições
with open('dois.txt') as f:
    content2 = f.readlines()
content2 = [x.rstrip('\n') for x in content2]

# copiando para a pasta correspondente
for i in os.listdir(origem):
    if i in content2:
        print(f'Movendo {i}')
        shutil.copy(i, caminho2)
tamanho = len(content2)

os.chdir(caminho2)
# Lendo a lista que esta em ordem, abrindo os arquivos em suas variaveis e fazendo a concatenação
for x in range(0, tamanho, 2):
    a1, a2 = content2[x], content2[x + 1]
    s1, s2 = AudioSegment.from_mp3(a1), AudioSegment.from_mp3(a2)
    som_out = s1 + s2
    splitado = a1.split("_")
    som_out.export(f"1_{splitado[1]}.mp3", format="mp3", bitrate="320")
    print(f"Arquivos {a1} e {a2} concatenados para {splitado[1]}")


os.chdir(origem)
# Lendo arquivos que contém 3 repetições e copiando para a pasta correspondente
with open('tres.txt') as f:
    content3 = f.readlines()
content3 = [x.rstrip('\n') for x in content3]

for i in os.listdir(origem):
    if i in content3:
        shutil.copy(i, caminho3)
os.chdir(caminho3)
tamanho = len(content3)
for x in range(0, tamanho, 3):
    a1, a2, a3 = content3[x], content3[x + 1], content3[x + 2]
    s1, s2, s3 = AudioSegment.from_mp3(a1), AudioSegment.from_mp3(a2), AudioSegment.from_mp3(a3)
    som_out = s1 + s2 + s3
    splitado = a1.split("_")
    som_out.export(f"1_{splitado[1]}.mp3", format="mp3", bitrate="320")
    print(f"Arquivos {a1} e {a2} e {a3} concatenados para"
                               f" {splitado[1]}")

os.chdir(origem)
# Lendo arquivos que contém 4 repetições e copiando para a pasta correspondente
with open('quatro.txt') as f:
    content4 = f.readlines()
content4 = [x.rstrip('\n') for x in content4]

for i in os.listdir(origem):
    if i in content4:
        shutil.copy(i, caminho4)

os.chdir(caminho4)
tamanho = len(content4)
for x in range(0, tamanho, 4):
    a1, a2, a3, a4 = content4[x], content4[x + 1], content4[x + 2], content4[x + 3]
    s1, s2, s3, s4 = AudioSegment.from_mp3(a1), AudioSegment.from_mp3(a2), \
                     AudioSegment.from_mp3(a3), AudioSegment.from_mp3(a4)
    som_out = s1 + s2 + s3 + s4
    splitado = a1.split("_")
    som_out.export(f"1_{splitado[1]}.mp3", format="mp3", bitrate="320")
    print(f"Arquivos {a1} e {a2} e {a3} e {a4} "
                               f"concatenados para {splitado[1]}")


os.chdir(origem)
# Lendo arquivos que contém 5 repetições e copiando para a pasta correspondente
with open('cinco.txt') as f:
    content5 = f.readlines()
content5 = [x.rstrip('\n') for x in content5]

for i in os.listdir(origem):
    if i in content5:
        shutil.copy(i, caminho5)


os.chdir(caminho5)
tamanho = len(content5)
for x in range(0, tamanho, 5):
    a1, a2, a3, a4, a5 = content5[x], content5[x + 1], \
                         content5[x + 2], content5[x + 3], content5[x + 4]
    s1, s2, s3, s4, s5 = AudioSegment.from_mp3(a1), AudioSegment.from_mp3(a2), \
                         AudioSegment.from_mp3(a3), AudioSegment.from_mp3(a4), \
                         AudioSegment.from_mp3(a5)
    som_out = s1 + s2 + s3 + s4 + s5
    splitado = a1.split("_")
    som_out.export(f"1_{splitado[1]}.mp3", format="mp3", bitrate="320")
    print(f"Arquivos {a1}"
                               f" e {a2}"
                               f" e {a3}"
                               f" e {a4}  "
                               f"e {a5} "
                               f"concatenados para {splitado[1]}")

os.chdir(origem)
# Lendo arquivos que contém 6 repetições e copiando para a pasta correspondente
with open('seis.txt') as f:
    content6 = f.readlines()
content6 = [x.rstrip('\n') for x in content6]

for i in os.listdir(origem):
    if i in content6:
        shutil.copy(i, caminho6)

os.chdir(caminho6)
tamanho = len(content6)
for x in range(0, tamanho, 6):
    a1, a2, a3, a4, a5, a6 = content6[x], content6[x + 1], \
                             content6[x + 2], content6[x + 3], content6[x + 4], \
                             content6[x + 5]
    s1, s2, s3, s4, s5, s6 = AudioSegment.from_mp3(a1), AudioSegment.from_mp3(a2), \
                             AudioSegment.from_mp3(a3), AudioSegment.from_mp3(a4), \
                             AudioSegment.from_mp3(a5), AudioSegment.from_mp3(a6)
    som_out = s1 + s2 + s3 + s4 + s5 + s6
    splitado = a1.split("_")
    som_out.export(f"1_{splitado[1]}.mp3", format="mp3", bitrate="320")
    print(f"""Arquivos {a1}
                                 e {a2}
                                 e {a3}
                                 e {a4}  
                                e {a5}
                                e {a6}
                                concatenados para {splitado[1]}""")

os.chdir(origem)
# Lendo arquivos que contém 7 repetições e copiando para a pasta correspondente
with open('sete.txt') as f:
    content7 = f.readlines()
content7 = [x.rstrip('\n') for x in content7]

for i in os.listdir(origem):
    if i in content7:
        shutil.copy(i, caminho7)

os.chdir(caminho7)
tamanho = len(content7)
for x in range(0, tamanho, 7):
    a1, a2, a3, a4, a5, a6, a7 = content7[x], content7[x + 1], \
                                 content7[x + 2], content7[x + 3], content7[x + 4], \
                                 content7[x + 5], content7[x + 6]
    s1, s2, s3, s4, s5, s6, s7 = AudioSegment.from_mp3(a1), AudioSegment.from_mp3(a2), \
                                 AudioSegment.from_mp3(a3), AudioSegment.from_mp3(a4), \
                                 AudioSegment.from_mp3(a5), AudioSegment.from_mp3(a6), \
                                 AudioSegment.from_mp3(a7)
    som_out = s1 + s2 + s3 + s4 + s5 + s6 + s7
    splitado = a1.split("_")
    som_out.export(f"1_{splitado[1]}.mp3", format="mp3", bitrate="320")
    print(f"""Arquivos {a1}
                                e {a2}
                                e {a3}
                                e {a4}  
                               e {a5}
                               e {a6}
                               e {a7}
                               concatenados para {splitado[1]}""")

os.chdir(origem)
# Lendo arquivos que contém 8 repetições e copiando para a pasta correspondente
with open('oito.txt') as f:
    content8 = f.readlines()
content8 = [x.rstrip('\n') for x in content8]

for i in os.listdir(origem):
    if i in content8:
        shutil.copy(i, caminho8)

os.chdir(caminho8)
tamanho = len(content8)
for x in range(0, tamanho, 8):
    a1, a2, a3, a4, a5, a6, a7, a8 = content8[x], content8[x + 1], \
                                     content8[x + 2], content8[x + 3], content8[x + 4], \
                                     content8[x + 5], content8[x + 6], content8[x + 7]
    s1, s2, s3, s4, s5, s6, s7, s8 = AudioSegment.from_mp3(a1), AudioSegment.from_mp3(a2), \
                                     AudioSegment.from_mp3(a3), AudioSegment.from_mp3(a4), \
                                     AudioSegment.from_mp3(a5), AudioSegment.from_mp3(a6), \
                                     AudioSegment.from_mp3(a7), AudioSegment.from_mp3(a8)
    som_out = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8
    splitado = a1.split("_")
    som_out.export(f"1_{splitado[1]}.mp3", format="mp3", bitrate="320")
    print(f"""Arquivos {a1}
                                e {a2}
                                e {a3}
                                e {a4}  
                               e {a5}
                               e {a6}
                               e {a7}
                               e {a8}
                               concatenados para {splitado[1]}""")

os.chdir(origem)

# Lendo arquivos que contém 9 repetições e copiando para a pasta correspondente
with open('nove.txt') as f:
    content9 = f.readlines()
content9 = [x.rstrip('\n') for x in content9]

for i in os.listdir(origem):
    if i in content9:
        shutil.copy(i, caminho9)

os.chdir(caminho9)
tamanho = len(content9)
for x in range(0, tamanho, 9):
    a1, a2, a3, a4, a5, a6, a7, a8, a9 = content9[x], \
                                         content9[x + 1], \
                                         content9[x + 2], content9[x + 3], content9[x + 4], \
                                         content9[x + 5], content9[x + 6], \
                                         content9[x + 7], \
                                         content9[x + 8]
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = AudioSegment.from_mp3(a1), \
                                         AudioSegment.from_mp3(a2), \
                                         AudioSegment.from_mp3(a3), AudioSegment.from_mp3(a4), \
                                         AudioSegment.from_mp3(a5), AudioSegment.from_mp3(a6), \
                                         AudioSegment.from_mp3(a7), AudioSegment.from_mp3(a8), AudioSegment.from_mp3(a9)
    som_out = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9
    splitado = a1.split("_")
    som_out.export(f"1_{splitado[1]}.mp3", format="mp3", bitrate="320")
    print(f"""Arquivos {a1}
                                 e {a2}
                                 e {a3}
                                 e {a4}  
                                e {a5}
                                e {a6}
                                e {a7}
                                e {a8}
                                e {a9}
                                concatenados para {splitado[1]}""")

os.chdir(origem)
# Lendo arquivos que contém 10 repetições e copiando para a pasta correspondente
with open('dez.txt') as f:
    content10 = f.readlines()
content10 = [x.rstrip('\n') for x in content10]

for i in os.listdir(origem):
    if i in content10:
        shutil.copy(i, caminho10)

os.chdir(caminho10)
tamanho = len(content10)
for x in range(0, tamanho, 10):
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = content10[x], \
                                              content10[x + 1], \
                                              content10[x + 2], content10[x + 3], content10[x + 4], \
                                              content10[x + 5], content10[x + 6], \
                                              content10[x + 7], \
                                              content10[x + 8], content10[x + 9]
    s1, s2, s3, s4, s5, s6, s7, s8, s9, s10 = AudioSegment.from_mp3(a1), \
                                              AudioSegment.from_mp3(a2), \
                                              AudioSegment.from_mp3(a3), AudioSegment.from_mp3(a4), \
                                              AudioSegment.from_mp3(a5), AudioSegment.from_mp3(a6), \
                                              AudioSegment.from_mp3(a7), AudioSegment.from_mp3(a8), \
                                              AudioSegment.from_mp3(a9), AudioSegment.from_mp3(a10)
    som_out = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10
    splitado = a1.split("_")
    som_out.export(f"1_{splitado[1]}.mp3", format="mp3", bitrate="320")

    print(f"""Arquivos {a1}
                                e {a2}
                                e {a3}
                                e {a4}  
                               e {a5}
                               e {a6}
                               e {a7}
                               e {a8}
                               e {a9}
                               e {a10}
                               concatenados para {splitado[1]}""")

os.chdir(origem)
# Lendo arquivos que contém 11 repetições e copiando para a pasta correspondente
with open('onze.txt') as f:
    content11 = f.readlines()
content11 = [x.rstrip('\n') for x in content11]

for i in os.listdir(origem):
    if i in content11:
        shutil.copy(i, caminho11)

os.chdir(caminho11)
tamanho = len(content11)
for x in range(0, tamanho, 11):
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11 = content11[x], \
                                                   content11[x + 1], \
                                                   content11[x + 2], content11[x + 3], content11[x + 4], \
                                                   content11[x + 5], content11[x + 6], \
                                                   content11[x + 7], \
                                                   content11[x + 8], \
                                                   content11[x + 9], \
                                                   content11[x + 10]
    s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11 = AudioSegment.from_mp3(a1), \
                                                   AudioSegment.from_mp3(a2), \
                                                   AudioSegment.from_mp3(a3), AudioSegment.from_mp3(a4), \
                                                   AudioSegment.from_mp3(a5), AudioSegment.from_mp3(a6), \
                                                   AudioSegment.from_mp3(a7), AudioSegment.from_mp3(a8), \
                                                   AudioSegment.from_mp3(a9), \
                                                   AudioSegment.from_mp3(a10), AudioSegment.from_mp3(a11)
    som_out = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10 + s11
    splitado = a1.split("_")
    som_out.export(f"1_{splitado[1]}.mp3", format="mp3", bitrate="320")

    print(f"""Arquivos {a1}
                                 e {a2}
                                 e {a3}
                                 e {a4}  
                                e {a5}
                                e {a6}
                                e {a7}
                                e {a8}
                                e {a9}
                                e {a10}
                                e {a11}
                                concatenados para {splitado[1]}""")

os.chdir(origem)
# Lendo arquivos que contém 12 repetições e copiando para a pasta correspondente
with open('doze.txt') as f:
    content12 = f.readlines()
content12 = [x.rstrip('\n') for x in content12]

for i in os.listdir(origem):
    if i in content12:
        shutil.copy(i, caminho12)
os.chdir(caminho12)
tamanho = len(content12)
for x in range(0, tamanho, 12):
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12 = content12[x], \
                                                        content12[x + 1], \
                                                        content12[x + 2], content12[x + 3], content12[x + 4], \
                                                        content12[x + 5], content12[x + 6], \
                                                        content12[x + 7], \
                                                        content12[x + 8], \
                                                        content12[x + 9], \
                                                        content12[x + 10], \
                                                        content12[x + 11]
    s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12 = AudioSegment.from_mp3(a1), \
                                                        AudioSegment.from_mp3(a2), \
                                                        AudioSegment.from_mp3(a3), AudioSegment.from_mp3(a4), \
                                                        AudioSegment.from_mp3(a5), AudioSegment.from_mp3(a6), \
                                                        AudioSegment.from_mp3(a7), AudioSegment.from_mp3(a8), \
                                                        AudioSegment.from_mp3(a9), \
                                                        AudioSegment.from_mp3(a10), \
                                                        AudioSegment.from_mp3(a11), AudioSegment.from_mp3(a12)
    som_out = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10 + s11 + s12
    splitado = a1.split("_")
    som_out.export(f"1_{splitado[1]}.mp3", format="mp3", bitrate="320")
    print(f"""Arquivos {a1}  e {a2}
                 e {a3} e {a4}  
                 e {a5} e {a6}
                 e {a7} e {a8}
                 e {a9} e {a10}
                 e {a11} e {a12}
                         concatenados para {splitado[1]}""")

os.chdir(origem)


print('Arquivos copiados')