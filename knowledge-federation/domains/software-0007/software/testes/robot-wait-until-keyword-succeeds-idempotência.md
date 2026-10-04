---
id: software.testes.tranche11.000478
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
fontes: ["https://robotframework.org/robotframework/latest/libraries/BuiltIn.html", "https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Robot Framework: repetir condição observável sem repetir efeito irreversível

## Em uma frase
Wait Until Keyword Succeeds repete uma keyword em intervalo configurado até passar ou esgotar limite.

## Por que importa
Repetir um POST de compra ou migração pode produzir múltiplos efeitos quando a primeira resposta é lenta ou ambígua.

## Como funciona
Use retry apenas para leitura/assertion idempotente de condição eventualmente consistente; faça a ação única e aguarde depois por estado observável.

## Exemplo
Após iniciar processamento uma vez, o teste consulta status até aparecer complete em vez de reenviar a solicitação de processamento.

## Limites e trade-offs
Retry não garante que a operação anterior não tenha sido executada, e tempo total depende de intervalo e limite configurados.

## Como verificar
Registre número de chamadas e force timeout com efeito já aplicado para comprovar que a ação não é repetida.

## Conexões
- [[robot-ignore-error-nao-esconder-falha]] — Veja também: Robot Framework: limitar Run Keyword And Ignore Error a erro esperado.
- [[robot-output-report-sensitive-data]] — Veja também: Robot Framework: controlar artefatos de saída e dados sensíveis.

## Fontes
- [Robot Framework 7.5 — BuiltIn library](https://robotframework.org/robotframework/latest/libraries/BuiltIn.html) — keywords incorporadas de fluxo, logging, execução, variáveis e assertions; consultado em 2026-10-02.
- [Robot Framework 7.5 — User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html) — formato de testes, setups, teardowns, tags, templates, variáveis, libraries e arquivos de saída; consultado em 2026-10-02.
