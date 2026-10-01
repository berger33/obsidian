---
tipo: ficha
status: semente
camada: arquitetura
hub: "[[MOC - Arquitetura de Software]]"
tags: [arquitetura, software, padroes]
conexoes_chave: ["[[Arquitetura hexagonal]]", "[[Monólito modular]]", "[[Coesão e acoplamento]]", "[[Estado do jogo]]"]
---

# Arquitetura em camadas

#arquitetura #software #padroes

## Resumo
Organiza responsabilidades em níveis, normalmente interface, aplicação, domínio e infraestrutura.

## Pergunta que esta nota responde
Quais dependências devem apontar para dentro e quais detalhes podem ficar nas bordas?

## Definição operacional
Arquitetura em camadas separa apresentação, orquestração, regras e infraestrutura. Ela é simples de explicar, mas pode virar rigidez se cada mudança pequena atravessar camadas sem valor claro.

## Quando usar
- Quando o sistema precisa separar UI, regras e persistência.
- Quando há muita lógica misturada com interface.
- Quando o time precisa de uma convenção inicial.

## Sinais de boa aplicação
- Cada camada tem motivo de mudança distinto.
- O domínio não depende de frameworks.
- A regra não fica escondida em callbacks de UI.

## Conexões
- [[Arquitetura hexagonal]]
- [[Monólito modular]]
- [[Coesão e acoplamento]]
- [[Estado do jogo]]
- [[Sistema de save]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Arquitetura de Software]].
