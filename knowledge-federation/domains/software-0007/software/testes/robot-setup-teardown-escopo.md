---
id: software.testes.tranche11.000471
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
fontes: ["https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-setup-and-teardown", "https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Robot Framework: escolher setup e teardown pelo escopo do recurso

## Em uma frase
Setups e teardowns podem ser definidos no nível de caso ou suite e executam keywords antes/depois da unidade configurada.

## Por que importa
Robot Framework interpreta arquivos de teste por seções e executa keywords de bibliotecas ou recursos; a legibilidade da suíte depende de escopo de variáveis, setup e teardown bem delimitados. Colocar criação compartilhada em cada caso custa tempo; colocar estado específico de um caso em setup de suite pode gerar contaminação.

## Como funciona
Modele cada caso pelo comportamento observável, mantenha preparações e limpeza no nível apropriado, use tags e templates para organização explícita e prefira keywords de domínio em vez de fluxo condicional espalhado. Use setup por teste para dados isolados, setup de suite para recursos realmente compartilhados e teardown para limpeza que precisa rodar mesmo após falha do caso.

## Exemplo
Cada caso cria seu registro temporário; a suite inicia um servidor descartável e encerra ao final.

## Limites e trade-offs
Keywords e bibliotecas externas têm ciclo de vida e estado próprios; um teardown não desfaz efeitos fora do ambiente de teste. O formato de dados não torna automaticamente um teste independente ou determinístico. Teardown não garante rollback de serviço externo que falhou; limpeza precisa tratar parcialmente criado e falhas de infraestrutura.

## Como verificar
Force falha depois da criação e confirme que teardown remove dados e encerra recursos sem ocultar o erro original.

## Conexões
- [[robot-test-case-keywords-observáveis]] — Veja também: Robot Framework: manter caso centrado em comportamento observável.
- [[robot-tags-selecao-sem-substituir-assertions]] — Veja também: Robot Framework: usar tags para selecionar casos, não para definir seu resultado.

## Fontes
- [Robot Framework 7.5 — Test setup and teardown](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-setup-and-teardown) — ordem e escopo do setup e teardown de testes; consultado em 2026-10-02.
- [Robot Framework 7.5 — User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html) — formato de testes, setups, teardowns, tags, templates, variáveis, libraries e arquivos de saída; consultado em 2026-10-02.
