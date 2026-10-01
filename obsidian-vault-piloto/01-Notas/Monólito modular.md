---
tipo: ficha
status: semente
camada: arquitetura
hub: "[[MOC - Arquitetura de Software]]"
tags: [arquitetura, software, modularidade]
conexoes_chave: ["[[Coesão e acoplamento]]", "[[Arquitetura em camadas]]", "[[Arquitetura hexagonal]]", "[[Ferramentas internas]]"]
---

# Monólito modular

#arquitetura #software #modularidade

## Resumo
Mantém um deploy simples com módulos internos bem definidos e fronteiras explícitas.

## Pergunta que esta nota responde
Como ganhar modularidade sem pagar cedo o custo de distribuição?

## Definição operacional
Monólito modular é uma arquitetura em que o sistema roda como uma unidade, mas o código é dividido por módulos coesos. É uma escolha forte para produtos em evolução e jogos com ferramentas internas.

## Quando usar
- Quando microserviços seriam complexidade prematura.
- Quando o time é pequeno.
- Quando fronteiras de domínio ainda estão amadurecendo.

## Sinais de boa aplicação
- Módulos têm APIs internas claras.
- Dependências entre módulos são visíveis.
- É possível extrair partes depois, se houver necessidade real.

## Conexões
- [[Coesão e acoplamento]]
- [[Arquitetura em camadas]]
- [[Arquitetura hexagonal]]
- [[Ferramentas internas]]
- [[Dívida técnica]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Arquitetura de Software]].
