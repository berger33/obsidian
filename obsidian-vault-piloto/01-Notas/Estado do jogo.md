---
tipo: ficha
status: semente
camada: ponte
hub: "[[MOC - Desenvolvimento de Jogos 2D]]"
tags: [jogos2d, arquitetura, gameplay]
conexoes_chave: ["[[Game loop]]", "[[Sistema de save]]", "[[Event-driven]]", "[[CQRS]]"]
---

# Estado do jogo

#jogos2d #arquitetura #gameplay

## Resumo
Conjunto de dados que representa a situação atual da partida, fase, menus e progressão.

## Pergunta que esta nota responde
Onde mora a verdade sobre o que está acontecendo no jogo?

## Definição operacional
Estado do jogo inclui posição, vida, inventário, flags, fase atual, pausa, diálogo e progressão. O desenho arquitetural deve deixar claro quem pode ler, alterar, salvar e observar esse estado.

## Quando usar
- Quando bugs surgem por duplicação de informação.
- Quando menus, HUD e gameplay discordam.
- Quando o save precisa restaurar uma sessão.

## Sinais de boa aplicação
- Há uma fonte de verdade clara.
- Transições de estado são nomeadas.
- UI observa o estado sem dominar as regras.

## Conexões
- [[Game loop]]
- [[Sistema de save]]
- [[Event-driven]]
- [[CQRS]]
- [[Modelagem de domínio]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Desenvolvimento de Jogos 2D]].
