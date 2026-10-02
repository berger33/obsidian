---
id: software.testes.tranche11.000472
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#tagging-test-cases", "https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Robot Framework: usar tags para selecionar casos, não para definir seu resultado

## Em uma frase
Tags podem classificar casos e orientar a seleção de testes durante a execução.

## Por que importa
Uma tag como slow, smoke ou quarantine organiza a execução, mas não comprova que a assertion do caso seja relevante ou esteja funcionando.

## Como funciona
Aplique tags com vocabulário estável e teste inclusões/exclusões do comando de execução em uma matriz de CI.

## Exemplo
O job smoke seleciona tags smoke e outra etapa roda regressão completa, verificando que ambos reportam casos esperados.

## Limites e trade-offs
Regras de seleção podem combinar tags e opções do runner; uma tag incorreta pode excluir cobertura importante silenciosamente.

## Como verificar
Compare casos descobertos e executados com a lista esperada para push, merge request e execução noturna.

## Conexões
- [[robot-setup-teardown-escopo]] — Veja também: Robot Framework: escolher setup e teardown pelo escopo do recurso.
- [[robot-template-data-driven]] — Veja também: Robot Framework: usar Test Template para repetir keyword com dados.

## Fontes
- [Robot Framework 7.5 — Tagging test cases](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#tagging-test-cases) — tags como metadados de casos e seleção por execução; consultado em 2026-10-02.
- [Robot Framework 7.5 — User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html) — formato de testes, setups, teardowns, tags, templates, variáveis, libraries e arquivos de saída; consultado em 2026-10-02.
