# Contribuições

## Ferramentas utilizadas

* [python 3.6](https://www.python.org/)
* [pip](https://pypi.python.org/pypi/pip)
* [virtualenv](https://virtualenv.pypa.io/en/stable/userguide/)
* [Flask](http://flask.pocoo.org/)

## Preparar o ambiente

### Clonar repositório

```
$ git clone git@github.com:unb-cic-esw/youtube-data-monitor.git
```

### Acesso à API do Youtube

Neste projeto, utilizamos
[a Youtube Data API v3](https://developers.google.com/youtube/v3/). Para que o
script funcione corretamente, é necessário que você registre seu projeto e
crie as credenciais necessárias para acesso à API. As instruções estão
disponíveis no [Create API Keys](https://developers.google.com/youtube/registering_an_application#Create_API_Keys).

Crie uma credencial do tipo API key e faça os seguintes procedimentos:

### Acessar o diretório do repositório clonado

- Abra o Terminal e digite o seguinte comando

```
$ cd youtube-data-monitor
```

### Instalar a aplicação

## Ubuntu

- Ainda no Terminal, digite:

```
$ bash youtube.sh install
```

- Será requisitada a chave da API do YouTube, adquirida no passo anterior.

- O Banco de Dados utilizado será o PostgreSQL. Insira um usuário e uma senha que desejar, quando solicitado.

- Após este procedimento, a aplicação estará instalada na sua máquina.

## MAC OS
 [Siga as instruções acima](#ubuntu)<br />
 Por fim, abra o arquivo activate que se encontra em venv/bin e adicione as seguintes linhas ao final da função deactivate():
 ```
 unset YOUTUBE_KEY
 unset DATABASE_URL/
 ```


### Executar a aplicação

- No diretório do repositório, digite:

```
$ bash youtube.sh run
```
- A aplicação começará a coletar os dados do dia. Somente poderá executar uma vez por dia.

- Para analisar os dados, basta executar:

```
$ flask run
```

- Com isso, os dados estarão dispostos nas seguintes rotas em seu browser:

```
Rota para todas as datas de coletas:
localhost:5000/dates

Rota para todos os atores políticos:
localhost:5000/actors

Rota para os dados de canal com DATA e ATOR específicos:
localhost:5000/<date>/canal/<actor>

Rota para os vídeos de DATA e ATOR específicos:
localhost:5000/<date>/canal/<actor>/videos
```

## Adicionar funcionalidades

Primeiramente procure uma tarefa para começar. [Temos uma lista de bugs e dívidas técnicas](CONTRIBUTING.md) ou você pode procurar uma nova funcionalidade na [API do Youtube](https://developers.google.com/youtube/v3/)
Para cada história a ser resolvida, seguir o seguinte procedimento:

- Clone o repositório
- Prepare o ambiente como foi explicado acima
- Crie uma branch (local e remoto) sobre o problema a ser resolvido, e.g.:

```
$ git checkout -b dev-subscribers
$ git push origin dev-subscribers
```

- Após resolver a issue, rode os devidos testes (rode mesmo porque seu PR não
  será aceito se seus testes não estiverem passando!)
- Abra um ticket de pull request no github com o sentido (base <- head):

 ```
 unb-cic-esw/youtube-data-monitor/master <- unb-cic-esw/youtube-data-monitor/dev-subscribers
 ```

- Espere o Travis CI executar os testes de integração
- Se os testes passarem o adm disponível no momento irá aceitar seu PR :rocket:



## Executar os testes
Todos os testes foram desenvolvidos utilizando a biblioteca
[unittest](https://docs.python.org/3/library/unittest.html) nativa do Python.

Os testes podem ser executados pelo seguinte comando:
```
$ bash youtube.sh test
```

Alternativamente, para executá-los, a partir da pasta raiz do projeto (dentro do environment), execute:

```
$ python -m unittest discover tests
```

## Checar estilo de código

Para seguir os padrões PEP8 de código python estamos usando a biblioteca
[pycodestyle](http://pycodestyle.pycqa.org/en/latest/).
Para cada novo módulo adicionado ao projeto é necessário criar um teste para
checar seu estilo de código (ver exemplos em [test_pep8](tests/test_pep8.py)).
Para executar a ferramenta e checar algum código, basta executar:

```
$ pip install pycodestyle
$ pycodestyle youtube/youtube.py
```

## Periodicidade e automatização da coleta dos dados

Para automatizar a execução do programa, utilizamos a ferramenta **crontab**.
Um script foi escrito para adicionar a rotina de coletar os dados da api do
Youtube à meia-noite como é possível ver no arquivo
[scheduler.sh](scheduler.sh). Para ativar a rotina basta escrever o seguinte
comando no terminal:
```
$ bash scheduler.sh
```
Para editar os crontabs:
```
$ crontab -e
```
Para listar os crontabs:
```
$ crontab -l
```

Em sistemas Linux, adicione a seguinte linha no arquivo aberto pelo comando
de editar crontab:
```
$ 0 0 * * * comando_a_ser_executado
```
O primeiro '0' diz respeito ao minuto, já o segundo '0' às horas. É usado o
sistema de 24 horas. Com o comando abaixo, o programa será executado todos os
dias à meia-noite.
```
$ 0 0 * * * cd $HOME/youtube/youtube-data-monitor && . venv/bin/activate && python -m youtube.update
```

## Executar servidor local

Para rodar o servidor local basta configurar a variável de ambiente do Flask:
```
$  FLASK_APP=server/main.py
```
E então executar o servidor com:
```
$ flask run
```

## Lista de Bugs e dívidas técnicas

### Dívidas técnicas

* [Comando Bash para instalação automática não é compatível totalmente com sistemas MAC OS](https://github.com/unb-cic-esw/youtube-data-monitor/issues/61);
* [As datas das coletas estão no formato: YYYY-MM-DD. O comportamento esperado seria: DD-MM-YYYY](https://github.com/unb-cic-esw/youtube-data-monitor/issues/62);
* [Adicionar versões para os endpoints que retornam arquivos CSV](https://github.com/unb-cic-esw/youtube-data-monitor/issues/63);

### Bugs

* [Sustentar mais de uma coleta por dia](https://github.com/unb-cic-esw/youtube-data-monitor/issues/64);
