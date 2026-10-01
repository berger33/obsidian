---
tipo: ficha
status: semente
camada: jogos2d
hub: "[[MOC - Desenvolvimento de Jogos 2D]]"
tags: [jogos2d, leveldesign, renderizacao]
conexoes_chave: ["[[Level design 2D]]", "[[Pipeline de assets]]", "[[Colisão 2D]]", "[[Renderização 2D]]"]
---

# Tilemaps

#jogos2d #leveldesign #renderizacao

## Resumo
Representam cenários por blocos reutilizáveis, facilitando produção de fases e colisões discretas.

## Pergunta que esta nota responde
O mundo 2D é melhor descrito por grade, objetos livres ou uma mistura?

## Definição operacional
Tilemaps usam tiles em uma grade para construir ambientes. Eles reduzem custo de arte, simplificam colisão e permitem ferramentas de level design, mas podem gerar repetição visual se mal usados.

## Quando usar
- Em platformers, RPGs, puzzles e metroidvanias.
- Quando fases precisam ser editadas rápido.
- Quando colisões podem seguir uma grade.

## Sinais de boa aplicação
- Tiles têm semântica clara.
- Camadas separam visual, colisão e decoração.
- O pipeline permite variações sem retrabalho.

## Conexões
- [[Level design 2D]]
- [[Pipeline de assets]]
- [[Colisão 2D]]
- [[Renderização 2D]]
- [[Pathfinding 2D]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Desenvolvimento de Jogos 2D]].
