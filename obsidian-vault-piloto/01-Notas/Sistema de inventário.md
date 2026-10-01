---
tipo: ficha
status: semente
camada: ponte
hub: "[[MOC - Desenvolvimento de Jogos 2D]]"
tags: [jogos2d, dominio, gameplay]
conexoes_chave: ["[[Modelagem de domínio]]", "[[Estado do jogo]]", "[[Sistema de save]]", "[[Testes automatizados]]"]
---

# Sistema de inventário

#jogos2d #dominio #gameplay

## Resumo
Gerencia itens, quantidades, regras de uso, coleta, descarte e efeitos no gameplay.

## Pergunta que esta nota responde
Inventário é lista de objetos, economia de recursos ou motor de decisões?

## Definição operacional
Um inventário pode ser simples como chaves coletadas ou complexo como slots, peso, crafting e equipamentos. A modelagem correta evita bugs de duplicação, perda e uso indevido.

## Quando usar
- Quando itens afetam progressão.
- Quando UI e regra começam a se misturar.
- Quando há equipamentos, consumíveis ou crafting.

## Sinais de boa aplicação
- Itens têm identidade e regras claras.
- UI não é fonte de verdade.
- Operações críticas são testáveis.

## Conexões
- [[Modelagem de domínio]]
- [[Estado do jogo]]
- [[Sistema de save]]
- [[Testes automatizados]]
- [[UX em jogos]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Desenvolvimento de Jogos 2D]].
