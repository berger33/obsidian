---
tipo: ficha
status: semente
camada: software
hub: "[[MOC - Engenharia de Software]]"
tags: [software, design, qualidade]
conexoes_chave: ["[[Coesão e acoplamento]]", "[[Refatoração]]", "[[Testes automatizados]]", "[[Arquitetura hexagonal]]"]
---

# SOLID com pragmatismo

#software #design #qualidade

## Resumo
Usa princípios de design como heurísticas, não como religião arquitetural.

## Pergunta que esta nota responde
Qual princípio reduz mudança dolorosa sem adicionar abstração prematura?

## Definição operacional
SOLID é um conjunto de princípios para orientar responsabilidade, extensão, substituição, interfaces e dependências. Em projetos pequenos ou jogos, o valor está em perceber tensão de mudança, não em criar camadas para tudo.

## Quando usar
- Quando uma classe tem motivos demais para mudar.
- Quando uma interface cresce sem necessidade.
- Quando testes ficam difíceis por dependências concretas.

## Sinais de boa aplicação
- Abstrações aparecem depois de repetição real.
- A leitura do código melhora.
- O princípio escolhido resolve uma dor específica.

## Conexões
- [[Coesão e acoplamento]]
- [[Refatoração]]
- [[Testes automatizados]]
- [[Arquitetura hexagonal]]
- [[Monólito modular]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Engenharia de Software]].
