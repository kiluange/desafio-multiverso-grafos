[![N|Solid](http://solutis.com.br/images/logo.png)](http://solutis.com.br)

#SOLUÇÃO PROPOSTA

Utilizar o algoritimo de Dijkstra (custo uniforme) para buscar a menor rota de um ponto a outro, para os pontos intermediários a busca sofre um split indo do ponto a ao ponto b depois do ponto b ao ponto c 

# EXECUÇÃO

`python3 Uniforme.py <ponto_atual> <ponto_destino> <nome_do_mapa.csv>`

`python3 Uniforme.py <ponto_atual> <ponto_intermediario - opcional> <ponto_destino> <nome_do_mapa.csv>`

## SAÍDA ESPERADA

`passo1 em B com distancia 0`

`passo2 em C com distancia 40`

`passo3 em E com distancia 60`

`run time 0.0002834796905517578 seconds`

# NOSSO DESAFIO RICK - GRAFOS
Na ficção científica, a viagem entre diferentes universos, é feita através de portais ou buracos de minhocas que conectam mundos diferentes ou até mesmo dimensões diferentes.

Imagine que você é um físico renomado que descobriu “buracos de minhocas” (rotas) que permitem o deslocamento entre universos. De acordo com sua descoberta, 
Todas as rotas são unidirecionais, ou seja, uma rota do universo A para o universo B não implica existência de uma rota do universo B para o universo A.
 
Mesmo quando existam rotas nos dois sentidos, elas são distintas e não possuem necessariamente a mesma distância (medidas em unidades de espaço-tempo).

O objetivo deste desafio é ajudar futuros viajantes a navegar entre os universos gastando a menor quantidade de espaço-tempo possível. 
Seu software deverá ser capaz de calcular o custo de deslocamento entre rotas, os números diferentes de rotas entre universos e as rotas mais econômicas.

Os universos e as rotas correspondem respectivamente aos vértices e arestas ponderadas do grafo abaixo:

[![N|Solid](https://github.com/solutisfsw/desafio-multiverso-grafos/raw/master/grafo.png)](Grafo)

Seu código deverá resolver os seguintes problemas:

* A distância de A a C passando por B?
* A distância entre A e D?
* A distância de A a C passando por D?
* O número de rotas saindo de C e voltando a C com no máximo 3 paradas?
* O número de rotas entre A e C com no máximo 4 paradas?
* A menor rota (em espaço-tempo) entre A e C?
* A menor rota (em espaço-tempo) saindo de B e voltando a B?
* O número de diferentes rotas saindo de C e voltando a C com distância máxima de 300 unidades de espaço-tempo?

A forma de entrada e saída dos dados fica a sua escolha.

## REGRAS GERAIS
Pedimos que você leia atentamente as instruções abaixo e crie uma solução de código usando Java, JavaScript, Ruby, ou Pyhton.

- Faça a [cópia](https://help.github.com/articles/fork-a-repo/) do repositório (fork), desenvolva e submeta uma [solicitação de mudança](https://help.github.com/articles/creating-a-pull-request/) (pull request) no branch master.
- Em caso de dúvidas basta abrir uma issue com sua pergunta (aqui mesmo no github) que nossa equipe irá respondê-lo assim que possível.
- Você não poderá usar bibliotecas externas ou ferramentas resolver o problema das rotas/grafo.
- Não será permitido o uso de bancos de dados orientedos a grafos.
- Avaliaremos uma variedade de aspectos, como design da solução, orientação a objeto, complexidade do código e a existência de testes unitários.
- Esperamos que você encaminhe um código que acredite ter qualidade, que possa ser executado e evoluído.
- Caso deseje evoluir a ideia seguindo essa base, fique à vontade: por exemplo, adaptar as entradas e saídas para ser um serviço web, criar uma interface gráfica, etc.

### BUILD E EXECUÇÃO
- Envie as instruções para execução do código
- De preferência, utilize um ferramenta como gradle, maven, npm ou yarn para realizar as tarefas necessárias de build.


# BOA SORTE!
