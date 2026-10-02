---
id: software.testes.tranche11.000474
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
fontes: ["https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html", "https://robotframework.org/robotframework/latest/libraries/BuiltIn.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Robot Framework: controlar escopo e precedência de variáveis

## Em uma frase
Robot Framework oferece variáveis de diferentes origens e escopos, e sua resolução depende da origem e do momento da definição.

## Por que importa
Variável global ou de suite alterada durante teste pode afetar outros casos que usam o mesmo processo.

## Como funciona
Prefira variáveis locais ao caso; use suite/global apenas para configuração imutável ou recurso cuja partilha seja explícita.

## Exemplo
Um teste altera ${TOKEN} localmente e confirma que outro caso não herda o token nem modifica configurações do pipeline.

## Limites e trade-offs
Os mecanismos de configuração por CLI, arquivo de variáveis e keywords têm precedências documentadas que variam por tipo de variável.

## Como verificar
Execute a suíte com overrides de CLI e verifique quais valores chegaram a cada nível sem imprimir segredos no log.

## Conexões
- [[robot-template-data-driven]] — Veja também: Robot Framework: usar Test Template para repetir keyword com dados.
- [[robot-resource-vs-library-import]] — Veja também: Robot Framework: distinguir resource file de test library.

## Fontes
- [Robot Framework 7.5 — User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html) — formato de testes, setups, teardowns, tags, templates, variáveis, libraries e arquivos de saída; consultado em 2026-10-02.
- [Robot Framework 7.5 — BuiltIn library](https://robotframework.org/robotframework/latest/libraries/BuiltIn.html) — keywords incorporadas de fluxo, logging, execução, variáveis e assertions; consultado em 2026-10-02.
