# Estrutura do código

## youtube

### youtube.py

Nesse arquivo, encontramos a classe YoutubeAPI. Nesta classe existem diversos métodos que tem como objetivo buscar informações sobre os canais dos atores políticos, alguns exemplos são o numero de inscritos (get_channel_subscribers) e o número de visualizações totais do canal (get_channel_total_view_count).

### videos.py  
Esse arquivo contém a classe Videos, seus métodos tem como objetivo buscar informações, disponibilizadas pela API do Youtube, sobre os vídeos publicados por cada um dos atores políticos. Alguns exemplos são:
get_all_video_items, que busca todos os tipos de informações disponibilizadas em cada video; get_category_info, que retorna todas as informações de uma categoria;
