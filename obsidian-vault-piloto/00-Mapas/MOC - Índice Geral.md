---
tipo: moc
status: ativo
camada: hub
tags: [moc, indice, hub]
---

# MOC - Índice Geral

#moc #indice #hub

## Função deste mapa
Mapa central do vault-piloto. Mantém três constelações principais e notas-ponte para criar um grafo legível.

## Navegação

### Hubs principais
- [[MOC - Engenharia de Software]]
- [[MOC - Arquitetura de Software]]
- [[MOC - Desenvolvimento de Jogos 2D]]

### Notas-ponte que desenham conexões entre clusters
- [[Requisitos jogáveis]]
- [[Estado do jogo]]
- [[ECS]]
- [[Prototipagem jogável]]
- [[Pipeline de assets]]
- [[Sistemas determinísticos]]
- [[Telemetria em jogos]]
- [[Dívida técnica]]

### Como ler o grafo
- [[Documentação viva]]
- [[Registro de decisões arquiteturais]]
- [[Modelagem de domínio]]


## Regra visual do grafo
Este MOC é um hub. Ele deve se conectar a notas do mesmo cluster, mas não deve tentar conectar tudo. As notas-ponte fazem a ligação entre constelações para evitar um grafo com um único centro inchado.
