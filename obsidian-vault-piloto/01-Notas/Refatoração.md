---
tipo: ficha
status: semente
camada: software
hub: "[[MOC - Engenharia de Software]]"
tags: [software, qualidade, evolucao]
conexoes_chave: ["[[Testes automatizados]]", "[[Coesão e acoplamento]]", "[[Dívida técnica]]", "[[SOLID com pragmatismo]]"]
---

# Refatoração

#software #qualidade #evolucao

## Resumo
Melhora a estrutura interna sem alterar o comportamento observável.

## Pergunta que esta nota responde
Como tornar a próxima mudança mais barata mantendo o jogo funcionando?

## Definição operacional
Refatoração é mudança estrutural guiada por segurança. Ela remove duplicação, explicita conceitos, melhora nomes e separa responsabilidades, idealmente apoiada por testes e pequenos commits.

## Quando usar
- Antes de adicionar uma variação complexa.
- Quando um módulo acumula exceções.
- Quando o custo de entender supera o custo de mudar.

## Sinais de boa aplicação
- O comportamento final é igual.
- Os nomes ficam mais próximos do domínio.
- A alteração reduz caminhos alternativos e casos especiais.

## Conexões
- [[Testes automatizados]]
- [[Coesão e acoplamento]]
- [[Dívida técnica]]
- [[SOLID com pragmatismo]]
- [[Documentação viva]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Engenharia de Software]].
