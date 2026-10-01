---
tipo: ficha
status: semente
camada: ponte
hub: "[[MOC - Desenvolvimento de Jogos 2D]]"
tags: [jogos2d, eventos, produto]
conexoes_chave: ["[[Event-driven]]", "[[Telemetria em jogos]]", "[[Estado do jogo]]", "[[Testes automatizados]]"]
---

# Sistema de conquistas

#jogos2d #eventos #produto

## Resumo
Reconhece marcos e comportamentos do jogador por eventos e condições verificáveis.

## Pergunta que esta nota responde
Que conquistas reforçam a experiência sem distorcer o jogo?

## Definição operacional
Um sistema de conquistas observa eventos e estados para desbloquear marcos. Ele deve ser desacoplado do gameplay principal para não espalhar condições de conquista pelo código inteiro.

## Quando usar
- Quando progressão e retenção precisam de metas extras.
- Quando eventos de gameplay já existem.
- Quando plataformas externas exigem integração.

## Sinais de boa aplicação
- Conquistas observam fatos, não controlam regras centrais.
- Condições são testáveis.
- A recompensa não incentiva comportamento ruim.

## Conexões
- [[Event-driven]]
- [[Telemetria em jogos]]
- [[Estado do jogo]]
- [[Testes automatizados]]
- [[Balanceamento]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Desenvolvimento de Jogos 2D]].
