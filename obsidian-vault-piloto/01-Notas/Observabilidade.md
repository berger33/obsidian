---
tipo: ficha
status: semente
camada: software
hub: "[[MOC - Engenharia de Software]]"
tags: [software, operacao, qualidade]
conexoes_chave: ["[[Telemetria em jogos]]", "[[Performance em jogos 2D]]", "[[CI-CD]]", "[[Documentação viva]]"]
---

# Observabilidade

#software #operacao #qualidade

## Resumo
Permite entender o comportamento real do sistema por logs, métricas, traces ou telemetria.

## Pergunta que esta nota responde
Quando algo dá errado, que sinais mostram onde e por quê?

## Definição operacional
Observabilidade é a capacidade de fazer perguntas novas sobre o sistema sem precisar lançar uma versão especial para depuração. Em jogos, se aproxima de telemetria de sessões, eventos de erro, funis e métricas de performance.

## Quando usar
- Quando bugs só aparecem em máquinas específicas.
- Quando playtests geram dúvidas de comportamento.
- Quando performance precisa ser acompanhada.

## Sinais de boa aplicação
- Eventos têm contexto suficiente.
- Métricas influenciam decisões de produto.
- Logs não expõem dados sensíveis nem viram ruído.

## Conexões
- [[Telemetria em jogos]]
- [[Performance em jogos 2D]]
- [[CI-CD]]
- [[Documentação viva]]
- [[Dívida técnica]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Engenharia de Software]].
