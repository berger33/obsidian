---
tipo: ficha
status: semente
camada: jogos2d
hub: "[[MOC - Desenvolvimento de Jogos 2D]]"
tags: [jogos2d, gameplay, fundamentos]
conexoes_chave: ["[[Sistemas determinísticos]]", "[[Estado do jogo]]", "[[Colisão 2D]]", "[[Performance em jogos 2D]]"]
---

# Game loop

#jogos2d #gameplay #fundamentos

## Resumo
Ciclo central que processa entrada, atualiza estado e desenha frames.

## Pergunta que esta nota responde
Em que ordem o jogo lê, simula, resolve e renderiza?

## Definição operacional
O game loop é a repetição contínua que mantém o jogo vivo. Ele recebe inputs, atualiza lógica, aplica física, resolve eventos, toca áudio e renderiza. Suas decisões afetam sensação, determinismo e performance.

## Quando usar
- Ao escolher timestep fixo ou variável.
- Ao depurar bugs que dependem de FPS.
- Ao organizar sistemas de gameplay.

## Sinais de boa aplicação
- A ordem de atualização é explícita.
- Sistemas críticos não dependem de FPS acidental.
- Renderização e simulação têm responsabilidades separadas.

## Conexões
- [[Sistemas determinísticos]]
- [[Estado do jogo]]
- [[Colisão 2D]]
- [[Performance em jogos 2D]]
- [[Requisitos jogáveis]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Desenvolvimento de Jogos 2D]].
