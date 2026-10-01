---
tipo: ficha
status: semente
camada: jogos2d
hub: "[[MOC - Desenvolvimento de Jogos 2D]]"
tags: [jogos2d, ia, algoritmos]
conexoes_chave: ["[[IA de inimigos 2D]]", "[[Tilemaps]]", "[[Performance em jogos 2D]]", "[[Sistemas determinísticos]]"]
---

# Pathfinding 2D

#jogos2d #ia #algoritmos

## Resumo
Calcula rotas por grades, grafos ou malhas navegáveis para agentes se moverem pelo cenário.

## Pergunta que esta nota responde
Que representação do espaço torna o caminho correto e barato?

## Definição operacional
Pathfinding em 2D frequentemente usa A*, grid, waypoints ou navmesh simplificada. A escolha depende do tipo de movimento, tamanho do mapa e necessidade de atualização dinâmica.

## Quando usar
- Quando inimigos precisam contornar obstáculos.
- Quando NPCs navegam tilemaps.
- Quando rotas precisam ser recalculadas sem travar o frame.

## Sinais de boa aplicação
- O espaço de busca é adequado ao jogo.
- Custos refletem design.
- Caminhos são suavizados quando necessário.

## Conexões
- [[IA de inimigos 2D]]
- [[Tilemaps]]
- [[Performance em jogos 2D]]
- [[Sistemas determinísticos]]
- [[Level design 2D]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Desenvolvimento de Jogos 2D]].
