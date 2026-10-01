---
tipo: ficha
status: semente
camada: arquitetura
hub: "[[MOC - Arquitetura de Software]]"
tags: [arquitetura, eventos, software]
conexoes_chave: ["[[Estado do jogo]]", "[[Telemetria em jogos]]", "[[CQRS]]", "[[Sistema de conquistas]]"]
---

# Event-driven

#arquitetura #eventos #software

## Resumo
Usa eventos para desacoplar produtores e consumidores de mudanças relevantes no sistema.

## Pergunta que esta nota responde
Quais fatos do sistema interessam a mais de uma parte?

## Definição operacional
Arquitetura orientada a eventos organiza comunicação por fatos: inimigo derrotado, item coletado, fase concluída, build publicada. Isso reduz dependências diretas, mas exige cuidado com ordem, rastreabilidade e excesso de eventos.

## Quando usar
- Quando múltiplos sistemas reagem ao mesmo fato.
- Quando módulos não devem se conhecer diretamente.
- Quando telemetria e conquistas observam gameplay.

## Sinais de boa aplicação
- Eventos são nomeados como fatos passados.
- Consumidores são independentes.
- Fluxos críticos ainda são rastreáveis.

## Conexões
- [[Estado do jogo]]
- [[Telemetria em jogos]]
- [[CQRS]]
- [[Sistema de conquistas]]
- [[Coesão e acoplamento]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Arquitetura de Software]].
