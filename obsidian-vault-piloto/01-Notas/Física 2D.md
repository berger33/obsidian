---
tipo: ficha
status: semente
camada: jogos2d
hub: "[[MOC - Desenvolvimento de Jogos 2D]]"
tags: [jogos2d, fisica, gameplay]
conexoes_chave: ["[[Colisão 2D]]", "[[Game loop]]", "[[Sistemas determinísticos]]", "[[Performance em jogos 2D]]"]
---

# Física 2D

#jogos2d #fisica #gameplay

## Resumo
Simula movimento, forças, gravidade e contatos quando a experiência pede comportamento físico.

## Pergunta que esta nota responde
A física deve ser simulação emergente ou controle manual com sensação calibrada?

## Definição operacional
Física 2D pode usar motores prontos ou lógica customizada. Platformers frequentemente misturam controle manual com colisão para preservar responsividade.

## Quando usar
- Quando objetos empurram, caem, quicam ou deslizam.
- Quando o jogo depende de massa, força e impulso.
- Quando o movimento do personagem precisa de consistência.

## Sinais de boa aplicação
- A sensação de controle vem antes do realismo.
- Timestep é estável.
- Parâmetros são ajustáveis para design.

## Conexões
- [[Colisão 2D]]
- [[Game loop]]
- [[Sistemas determinísticos]]
- [[Performance em jogos 2D]]
- [[Level design 2D]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Desenvolvimento de Jogos 2D]].
