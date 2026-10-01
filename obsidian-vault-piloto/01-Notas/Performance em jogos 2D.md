---
tipo: ficha
status: semente
camada: ponte
hub: "[[MOC - Desenvolvimento de Jogos 2D]]"
tags: [jogos2d, performance, arquitetura]
conexoes_chave: ["[[Observabilidade]]", "[[Sprites e atlases]]", "[[Renderização 2D]]", "[[Game loop]]"]
---

# Performance em jogos 2D

#jogos2d #performance #arquitetura

## Resumo
Mantém frame rate, memória e responsividade dentro de limites adequados à plataforma.

## Pergunta que esta nota responde
Qual gargalo realmente impede a experiência desejada?

## Definição operacional
Performance 2D envolve draw calls, fill rate, física, alocação, scripts, carregamento, pathfinding e partículas. Otimizar cedo demais atrapalha, mas ignorar medições cria dívida.

## Quando usar
- Quando frames caem em cenas representativas.
- Antes de lançar em hardware limitado.
- Quando sistemas multiplicam entidades ou efeitos.

## Sinais de boa aplicação
- Medições vêm antes de otimização.
- Há orçamento de frame e memória.
- Otimizações preservam clareza quando possível.

## Conexões
- [[Observabilidade]]
- [[Sprites e atlases]]
- [[Renderização 2D]]
- [[Game loop]]
- [[Dívida técnica]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Desenvolvimento de Jogos 2D]].
