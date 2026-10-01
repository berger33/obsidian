---
tipo: ficha
status: semente
camada: arquitetura
hub: "[[MOC - Arquitetura de Software]]"
tags: [arquitetura, software, padroes]
conexoes_chave: ["[[Modelagem de domínio]]", "[[Testes automatizados]]", "[[Arquitetura em camadas]]", "[[Sistema de save]]"]
---

# Arquitetura hexagonal

#arquitetura #software #padroes

## Resumo
Protege regras centrais de detalhes externos por portas e adaptadores.

## Pergunta que esta nota responde
Como testar regras sem depender de banco, engine, rede ou UI?

## Definição operacional
A arquitetura hexagonal coloca o domínio e os casos de uso no centro. Entradas e saídas passam por portas, e detalhes como engine, armazenamento e APIs ficam em adaptadores substituíveis.

## Quando usar
- Quando regras importantes precisam de testes rápidos.
- Quando detalhes externos mudam com frequência.
- Quando a lógica está presa demais à engine.

## Sinais de boa aplicação
- Casos de uso podem rodar fora da interface.
- Adaptadores dependem do centro, não o contrário.
- Mocks e fakes ficam naturais.

## Conexões
- [[Modelagem de domínio]]
- [[Testes automatizados]]
- [[Arquitetura em camadas]]
- [[Sistema de save]]
- [[Ferramentas internas]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Arquitetura de Software]].
