---
tipo: ficha
status: semente
camada: ponte
hub: "[[MOC - Desenvolvimento de Jogos 2D]]"
tags: [jogos2d, arquitetura, persistencia]
conexoes_chave: ["[[Estado do jogo]]", "[[Arquitetura em camadas]]", "[[Arquitetura hexagonal]]", "[[Testes automatizados]]"]
---

# Sistema de save

#jogos2d #arquitetura #persistencia

## Resumo
Persistência confiável de progresso, configurações e estado relevante do jogador.

## Pergunta que esta nota responde
O que precisa sobreviver entre sessões e em que versão de dados?

## Definição operacional
Sistema de save serializa progresso, inventário, checkpoints, flags, configurações e metadados. Deve lidar com versões, corrupção, slots, autosave e compatibilidade futura.

## Quando usar
- Quando progressão passa de protótipo para produto.
- Quando estados precisam ser restaurados exatamente.
- Quando atualizações podem mudar estrutura de dados.

## Sinais de boa aplicação
- Há esquema de versionamento.
- Dados transitórios não são salvos por acidente.
- Falhas de escrita não destroem o progresso anterior.

## Conexões
- [[Estado do jogo]]
- [[Arquitetura em camadas]]
- [[Arquitetura hexagonal]]
- [[Testes automatizados]]
- [[Dívida técnica]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Desenvolvimento de Jogos 2D]].
