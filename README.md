# modelo-vitrinedev
# Concatenação áudios URA

Concatenando áudios que são divididos automáticamente pela Ura

| :placard: Vitrine.Dev |     |
| -------------  | --- |
| :sparkles: Nome        | **Concatenando Áudios da Ura*
| :label: Tecnologias | python


# concatenandoAudiosUra
Concatenação de Áudios da Ura

# Solução pessoal para concatenação de Áudios da Ura
# Minha Ura, faz uma divisão dos áudios por duração de ligação.
# A cada 5 minutos na mesma ligação um novo áudio é criado.
Todo áudio tem a caracteristica no nome: 1_xxxxxxxxxxx_xxxxxxxxxxx.mp3
Cada ligação tem o primeiro id (os primeiros 11 x) diferentes. Porém quando é áudio com mais de 5 minutos e ocorre a divisão, o áudio mantém a primeira sequencia identica. O que diferencia a ordem é a segunda sequencia.

No primeiro arquivo python: 

Passo01-Verificando.py

Estamos preparando o ambiente. Entrando dentro do diretório onde estão os áudios.
Depois criamos um arquivo txt colocando o nome de cada arquivo que contém no diretório.

Segundo arquivo python:

Passo02-Verificando_repeticoes.py

Aqui criamos algumas listas vazias para serem preenchidas automáticamente.
 Checando os arquivos em mp3 no diretório, abrindo o arquivo quantos.txt criado no Passo 01
 depois contando as ocorrências de repetição de nomes dos áudios
 Na minha estrutura Ura, os arquivos de áudios são salvos no formato: 1_xxxxxxxxxxxx_xxxxxxxxxxxx.mp3
 Nesse caso, estamos dividindo o nome do arquivo por _
 Depois estamos novamente adicionando o prefixo 1_ para fazer a contagem dos nomes
 Essa ação é necessária, pois encontrei áudios com as duas sequencias(xxxxxx_xxxxx) identicas, o que levava a contagem
 incorreta. Dessa forma evitamos isso.
Depois:
 Aqui estamos lendo as listas criadas e criando um arquivo txt separando áudios por vezes de repetição
 Ex: áudios que são necessários 2 concatenações, 3, 4 etc.

Terceiro arquivo python:
Passo03-Criando_pastas-Copiando_arquivos-e-Concatenando.py

Criando as pastas
Criando variaveis para cada pasta
Lendo arquivos que contém x repetições
Copiando para a pasta correspondente
Lendo a lista que esta em ordem, abrindo os arquivos em suas variaveis e fazendo a concatenação


Para meu caso, foi identificado arquivos até com 12 separações. Portanto foi o máximo necessário. #vitrinedev
