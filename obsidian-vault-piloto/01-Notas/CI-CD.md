---
tipo: ficha
status: semente
camada: software
hub: "[[MOC - Engenharia de Software]]"
tags: [software, automacao, entrega]
conexoes_chave: ["[[Testes automatizados]]", "[[Observabilidade]]", "[[Prototipagem jogável]]", "[[Pipeline de assets]]"]
---

# CI-CD

#software #automacao #entrega

## Resumo
Automatiza validação e entrega para reduzir risco acumulado entre mudanças e builds.

## Pergunta que esta nota responde
O que deve ser verificado automaticamente antes de uma mudança virar build jogável?

## Definição operacional
CI/CD combina integração contínua, testes, empacotamento e distribuição. Para jogos 2D, pode gerar builds por plataforma, rodar testes de lógica e publicar protótipos para playtest.

## Quando usar
- Quando builds manuais começam a falhar por esquecimento.
- Quando há mais de uma pessoa no projeto.
- Quando playtests precisam de versões frequentes.

## Sinais de boa aplicação
- Builds são reproduzíveis.
- Erros aparecem perto da mudança que os causou.
- Existe histórico claro de versões.

## Conexões
- [[Testes automatizados]]
- [[Observabilidade]]
- [[Prototipagem jogável]]
- [[Pipeline de assets]]
- [[Documentação viva]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Engenharia de Software]].
