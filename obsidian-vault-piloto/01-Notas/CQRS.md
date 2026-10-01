---
tipo: ficha
status: semente
camada: arquitetura
hub: "[[MOC - Arquitetura de Software]]"
tags: [arquitetura, padroes, software]
conexoes_chave: ["[[Event-driven]]", "[[Estado do jogo]]", "[[Sistemas determinísticos]]", "[[Arquitetura hexagonal]]"]
---

# CQRS

#arquitetura #padroes #software

## Resumo
Separa comandos que mudam estado de consultas que leem estado.

## Pergunta que esta nota responde
Leitura e escrita têm necessidades tão diferentes que merecem modelos separados?

## Definição operacional
CQRS divide operações de escrita e leitura. Em jogos, a ideia aparece quando a simulação muda estado por comandos, enquanto HUD, debug e telemetria leem projeções simplificadas.

## Quando usar
- Quando leitura e escrita têm modelos conflitantes.
- Quando projeções de UI ficam complexas.
- Quando eventos alimentam visões derivadas.

## Sinais de boa aplicação
- Comandos expressam intenção.
- Consultas não mudam estado.
- A separação reduz complexidade, não aumenta por moda.

## Conexões
- [[Event-driven]]
- [[Estado do jogo]]
- [[Sistemas determinísticos]]
- [[Arquitetura hexagonal]]
- [[Telemetria em jogos]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Arquitetura de Software]].
