# Engenharia de Software

## Práticas Ágeis

Um dos objetivos principais desse projeto foi aprender como implementar práticas ágeis no desenvolvimento de um sistema.
As práticas adotadas serão listadas a seguir.

### Histórias

Histórias são uma parte essencial para o desenvolvimento ágil, pois elas são responsáveis pelos requisitos.
Essas histórias são funcionalidades ou requisitos técnicos discutidos com o(s) cliente(s), tendo em mente
para qual tipo de usuário (ou desenvolvedor) essa funcionalidade ou requisito será utilizada; o que o usuário espera com esse requisito e
com qual finalidade;
Além disso, para a criação de uma história poder ser dita "concluída", é necessário estabelecer um acordo com o cliente.
Esse acordo é chamado de "teste de aceitação", e é ele que define se a história pode ser concluída ou não no final de todo o processo.

### Kanban

O kanban foi utilizado para acompanhar o progresso das atividades que estavam em desenvolvimento pela equipe. Foi utilizado tanto o
kanban físico (um cartaz onde colocamos post-its) quanto o virtual que, em nossa equipe, foi escolhido o ZenHub. Ambos ambientes de
acompanhamento foram divididos em cinco categorias, sendo essas:

* Backlog
* Business Analisys
* In Progress
* Review/ QA
* Closed

O "Backlog" é o campo responsável por manter as histórias que foram acordadas com os clientes, ou seja, as funcionalidades e/ou alterações
que foram debatidas e aceitas para entrarem em desenvolvimento.
"Business Analisys" é a coluna aonde são mantidas as histórias que já foram debatidas pelo próprio time de desenvolvimento. O debate sobre
essas histórias incluem as dificuldades que a equipe espera encontrar ao longo da complitude dessa história, bem como o que será necessário
para, de fato, implementá-la.
A coluna "In Progress" é utilizada para acompanhar as histórias que já começaram a ser desenvolvidas pela equipe.
"Review/ QA" é a coluna utilizada para acompanhar histórias cujo desenvolvimento já foi finalizado, mas ainda não foram aprovadas pelo
cliente.
Por fim, a coluna "Closed" é onde são mantidas as histórias cujos processos já foram concluídos, tanto de desenvolvimento quanto de aprovação.

### Tracking de horário

A cada sprint era escolhido um tracker para verificar e avaliar a pontualidade de cada integrante do time. Sendo assim, um integrante que chegasse atrasado para o showcase teria uma penalidade de pontos.

### Stand Up

Essa prática consiste em uma reunião rápida, de aproximadamente cinco minutos, na qual a equipe discute o progresso que teve durante a atual etapa
do desenvolvimento e desde a última reunião stand up. Além disso, é durante esse tempo que a equipe muda as histórias de coluna, e, consequentemente, de etapa no kanban.

### Sprint (Iteração)

A cada iteração são desenvolvidas as históras, passando pelo processo de aceitação inicial do cliente, que serão trabalhadas pelo time.
No caso do projeto desenvolvido nessa disciplina, as iterações tiveram duração de 15 dias.

### Showcase

O showcase é realizado no final de cada sprint. Esse é o momento em que o time de desenvolvimento demonstra o progresso obtido durante a sprint decorrida.
Também é o momento no qual o cliente aprova as histórias concluídas, por meio dos testes de aceitação previamente definidos.

### Planejamento de Iteração

No inicio de cada iteração, era realizada uma reunião entre o cliente e os integrantes do time. As histórias da próxima sprint eram definidas e aceitas pelos clientes. Além disso, eram definidas as duplas que seriam responsáveis por cada história.

### Pareamento

A cada iteração a equipe era dividia aleatoriamente em pares, e as histórias acordadas com o(s) cliente(s) eram atribuídas à esses pares.
Além disso, foi realizado o "tracking", ou seja, o acompanhamento, de quais duplas já haviam sido pareadas, para não haver repetições
dos integrantes das duplas.

### Refatoração

Em determinados momentos no decorrer do projeto, eram realizadas refatorações no código para retirar códigos desnecessários, organizar a code base e comentar determinados pontos do código para deixa-lo de fácil entendimento.

### Integração Contínua

Nosso time de desenvolvimento utilizou a prática de integração contínua para a realização do projeto. Foi utilizado a plataforma Travis para colocar em prática essa técnica de desenvolvimento ágil. Ao realizar qualquer push para as branches remotas e/ou master, o Travis executava todos os requeriments e, também, executava todos os testes realizados no projeto. Caso algum dos testes falhasse, era necessário a correção desse bug. Além disso, para realizar um merge com a master, utilizamos pull-requests para que antes de um merge direto, houvesse alguém (membro do time de desenvolvimento) para revisar o código do pedido de pull request e evitar a integração de um código, contendo bugs, na master.

### Test Driven Development

Ao implementar uma nova funcionalidade, primeiramente era escrito o código de teste para checar a futura implementação. Feito isso, a nova funcionalidade era implementada e checada de acordo com o código de testes previamente feito. Por fim, eram realizadas pequenas refatorações para deixar o código com um determinado nível qualidade.

## Histórias Desenvolvidas
[Coletar os canais dos atores que estão presentes no YouTube](https://github.com/unb-cic-esw/youtube-data-monitor/issues/8)
[Número de visualizações dos canais](https://github.com/unb-cic-esw/youtube-data-monitor/issues/9)
[Quantidade de vídeos dos canais](https://github.com/unb-cic-esw/youtube-data-monitor/issues/10)
[Número de visualizações de cada vídeo dos canais](https://github.com/unb-cic-esw/youtube-data-monitor/issues/11)
[Quantidade de inscritos de cada canal](https://github.com/unb-cic-esw/youtube-data-monitor/issues/12)
[Implementar o CircleCI para integração contínua](https://github.com/unb-cic-esw/youtube-data-monitor/issues/13)

## Lista de Bugs

## Apresentações de Showcase

## Fotos
