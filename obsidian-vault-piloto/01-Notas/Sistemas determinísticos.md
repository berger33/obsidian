---
tipo: ficha
status: semente
camada: ponte
hub: "[[MOC - Índice Geral]]"
tags: [arquitetura, jogos2d, simulacao]
conexoes_chave: ["[[Game loop]]", "[[Testes automatizados]]", "[[Física 2D]]", "[[CQRS]]"]
---

# Sistemas determinísticos

#arquitetura #jogos2d #simulacao

## Resumo
Produzem o mesmo resultado para a mesma sequência de entradas, facilitando testes, replay e depuração.

## Pergunta que esta nota responde
A simulação precisa ser reproduzível exatamente ou apenas consistente para o jogador?

## Definição operacional
Determinismo reduz incerteza em simulações. Em jogos, pode ajudar rollback netcode, replays, testes e debug, mas exige controle de tempo, aleatoriedade, ordem de atualização e ponto flutuante.

## Quando usar
- Quando bugs são difíceis de reproduzir.
- Quando replays ou multiplayer dependem de simulação idêntica.
- Quando testes precisam validar sequências de jogo.

## Sinais de boa aplicação
- Random usa seed controlada.
- Timestep e ordem de execução são definidos.
- Entradas podem ser gravadas e reproduzidas.

## Conexões
- [[Game loop]]
- [[Testes automatizados]]
- [[Física 2D]]
- [[CQRS]]
- [[Pathfinding 2D]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Índice Geral]].
