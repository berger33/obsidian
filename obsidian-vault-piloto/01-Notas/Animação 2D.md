---
tipo: ficha
status: semente
camada: jogos2d
hub: "[[MOC - Desenvolvimento de Jogos 2D]]"
tags: [jogos2d, arte, feedback]
conexoes_chave: ["[[Sprites e atlases]]", "[[Feedback ao jogador]]", "[[Game feel]]", "[[IA de inimigos 2D]]"]
---

# Animação 2D

#jogos2d #arte #feedback

## Resumo
Comunica estado, intenção, peso e resposta por movimento visual.

## Pergunta que esta nota responde
Que informação de gameplay a animação precisa tornar legível?

## Definição operacional
Animação 2D inclui spritesheets, skeletal animation, state machines, blending simples e efeitos. Ela não serve só para beleza: telegrava ataques, confirma ações e vende impacto.

## Quando usar
- Quando estados precisam ser lidos rapidamente.
- Quando ataques e dano precisam de antecipação.
- Quando o jogo parece rígido apesar da mecânica funcionar.

## Sinais de boa aplicação
- Cada estado importante tem pose reconhecível.
- Transições não escondem controle.
- Timing e feedback reforçam regras.

## Conexões
- [[Sprites e atlases]]
- [[Feedback ao jogador]]
- [[Game feel]]
- [[IA de inimigos 2D]]
- [[Pipeline de assets]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Desenvolvimento de Jogos 2D]].
