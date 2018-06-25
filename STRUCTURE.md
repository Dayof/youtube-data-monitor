# Estrutura do código

## youtube

### youtube.py

Nesse módulo, encontramos a classe YoutubeAPI. Nesta classe existem diversos métodos que tem como objetivo buscar informações sobre os canais dos atores políticos, alguns exemplos são o numero de inscritos (get_channel_subscribers) e o número de visualizações totais do canal (get_channel_total_view_count).

### videos.py  
Esse módulo contém a classe Videos, seus métodos tem como objetivo buscar informações, disponibilizadas pela API do Youtube, sobre os vídeos publicados por cada um dos atores políticos. Alguns exemplos são:
* get_all_video_items, que busca todos os tipos de informações disponibilizadas em cada video;
* get_category_info, que retorna todas as informações de uma categoria;

### update.py
Esse módulo possui funcionalidades que requisitam todas as informações de canais, vídeos e vídeos relacionados da API. Bem como, realiza a inserção das informações coletadas no banco de dados.


## config

### actors.json

Contém o nome, id e username de cada ator político predeterminado em formato JSON. Essas informações podem ser alteradas, para atender a necessidade do usuário.

### error_messages.json

Esse módulo possui mensagens para cada código de erro do flask. Esse módulo pode, também, ser alterado de acordo com a necessidade do usuário.

### parameters.json

Esse módulo contém parâmetros que podem ser alterados de acordo com a necessidade do usuário. São eles:
* Número limite de vídeos e vídeos relacionados que a aplicação busca na API;
* Data referência para coleta. Só irão ser coletados vídeos publicados após essa data e devem seguir o seguinte formato (YYYY-MM-DDTHH:MM:SS.ss-ss:ss);

### routes_help.json

O módulo acima descreve todas as rotas utilizadas no flask e seu propósito.

## server

### main.py
Determina todas as rotas dos endpoints do flask, busca as requisições de banco de dados e retorna as respostas obtidos em um JSON. Esses resultados ficam visíveis ao acessar cada endpoint pelo seu navegador.

### models.py
Modela todas as tabelas do banco de dados, definindo sua estrutura. As tabelas são:
* Actor
* Videos
* Relationship_Actor_Videos
* Relationship_Videos

A tabela Actor contém as informações de todos os atores coletados;<br />
A tabela Videos contém as informações de todos os videos coletados;<br />
A tabela Relationship_Actor_Videos contém as informações da relação entre as tabelas Actors e Videos;<br />
A tabela Relationship_Videos contém informações das relações entre os vídeos (Ex: vídeos e vídeos relacionados);<br />

### queries.py
A classe DBYouTube possui os métodos que descrevem cada query do banco de dados, alguns exemplos são:
* get_dates, que retorna as datas das coletas realizadas;
* get_actor_videos, que retorna os videos de um determinado ator;
