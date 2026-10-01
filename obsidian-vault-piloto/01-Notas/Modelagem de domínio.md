---
tipo: ficha
status: semente
camada: software
hub: "[[MOC - Engenharia de Software]]"
tags: [software, arquitetura, dominio]
conexoes_chave: ["[[Arquitetura hexagonal]]", "[[Estado do jogo]]", "[[Sistema de inventário]]", "[[Coesão e acoplamento]]"]
---

# Modelagem de domínio

#software #arquitetura #dominio

## Resumo
Organiza conceitos, regras e vocabulário do problema antes de escolher frameworks ou estruturas de código.

## Pergunta que esta nota responde
Quais objetos, regras e eventos existem no problema independentemente da tecnologia?

## Definição operacional
Modelagem de domínio é a prática de representar entidades, valores, eventos, políticas e invariantes do negócio ou do sistema. Em jogos 2D, o domínio pode incluir jogador, inimigo, dano, inventário, fase, checkpoint e progressão.

## Quando usar
- Quando o código começa a refletir nomes confusos.
- Antes de separar módulos.
- Ao criar sistemas de jogo com regras complexas.

## Sinais de boa aplicação
- Os nomes do código batem com os nomes usados pela equipe.
- Regras importantes ficam perto dos conceitos que protegem.
- A arquitetura fica menos dependente de detalhes de engine.

## Conexões
- [[Arquitetura hexagonal]]
- [[Estado do jogo]]
- [[Sistema de inventário]]
- [[Coesão e acoplamento]]
- [[Documentação viva]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Engenharia de Software]].
