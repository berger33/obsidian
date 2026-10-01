---
tipo: moc
status: ativo
camada: hub
tags: [moc, arquitetura, hub]
---

# MOC - Arquitetura de Software

#moc #arquitetura #hub

## Função deste mapa
Cluster de decisões estruturais, fronteiras e padrões arquiteturais.

## Navegação

### Estrutura e modularidade
- [[Monólito modular]]
- [[Arquitetura em camadas]]
- [[Arquitetura hexagonal]]

### Comunicação e fluxo de dados
- [[Event-driven]]
- [[CQRS]]
- [[Registro de decisões arquiteturais]]

### Pontes com jogos e produção
- [[Estado do jogo]]
- [[Ferramentas internas]]
- [[Pipeline de assets]]
- [[Sistemas determinísticos]]


## Regra visual do grafo
Este MOC é um hub. Ele deve se conectar a notas do mesmo cluster, mas não deve tentar conectar tudo. As notas-ponte fazem a ligação entre constelações para evitar um grafo com um único centro inchado.
