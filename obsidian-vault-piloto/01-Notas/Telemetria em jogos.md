---
tipo: ficha
status: semente
camada: ponte
hub: "[[MOC - Índice Geral]]"
tags: [jogos2d, observabilidade, produto]
conexoes_chave: ["[[Observabilidade]]", "[[Event-driven]]", "[[Feedback ao jogador]]", "[[Balanceamento]]"]
---

# Telemetria em jogos

#jogos2d #observabilidade #produto

## Resumo
Coleta eventos de uso para entender comportamento real, dificuldade, retenção e problemas.

## Pergunta que esta nota responde
Que eventos ajudam a melhorar o jogo sem invadir a privacidade do jogador?

## Definição operacional
Telemetria em jogos registra eventos como início de fase, morte, item coletado, tempo de sessão, abandono, erro e vitória. Ela deve servir perguntas de design e produto, não acumular dados sem propósito.

## Quando usar
- Durante playtests.
- Ao balancear dificuldade.
- Quando decisões dependem de comportamento real e não só opinião.

## Sinais de boa aplicação
- Eventos têm pergunta associada.
- Privacidade e consentimento são considerados.
- Métricas geram ações concretas.

## Conexões
- [[Observabilidade]]
- [[Event-driven]]
- [[Feedback ao jogador]]
- [[Balanceamento]]
- [[UX em jogos]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Índice Geral]].
