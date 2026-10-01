---
tipo: ficha
status: semente
camada: software
hub: "[[MOC - Engenharia de Software]]"
tags: [software, qualidade, automacao]
conexoes_chave: ["[[CI-CD]]", "[[Refatoração]]", "[[Requisitos jogáveis]]", "[[Sistemas determinísticos]]"]
---

# Testes automatizados

#software #qualidade #automacao

## Resumo
Protegem comportamento importante e permitem mudar o sistema com menos medo.

## Pergunta que esta nota responde
Que comportamento precisa continuar verdadeiro quando a implementação mudar?

## Definição operacional
Testes automatizados executam verificações repetíveis sobre unidades, integrações, regras de domínio, cenas ou simulações. Em jogos, testes podem validar dano, colisão, inventário, carregamento de fase e estados do personagem.

## Quando usar
- Quando uma regra é crítica.
- Quando bugs voltam após correções.
- Antes de refatorar sistemas centrais.

## Sinais de boa aplicação
- O teste descreve comportamento, não implementação acidental.
- Falhas apontam para uma regra quebrada.
- A suíte roda rápido o bastante para ser usada diariamente.

## Conexões
- [[CI-CD]]
- [[Refatoração]]
- [[Requisitos jogáveis]]
- [[Sistemas determinísticos]]
- [[Estado do jogo]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Engenharia de Software]].
