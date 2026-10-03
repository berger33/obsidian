---
id: software.testes.tranche19.001328
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://reportportal.io/docs/developers-guides/ReportingDevelopersGuide/", "https://reportportal.io/docs/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ReportPortal: organizar lançamentos e itens

## Em uma frase
Cada execução é registrada como lançamento, e os resultados são itens hierárquicos de suíte, teste, cenário e passo sob esse lançamento.

## Por que importa
A hierarquia entre lançamento e itens preserva o contexto da execução e permite analisar resultados por nível.

## Como funciona
Crie o lançamento no início da execução, reporte os itens conforme acontecem e finalize com o estado calculado ou explícito.

## Exemplo
Uma execução noturna pode ser um lançamento com suítes por módulo e testes por caso, permitindo navegar da visão geral ao passo.

## Limites e trade-offs
Lançamentos abertos sem finalização distorcem a visão de execuções em andamento e atrasam a análise automática.

## Como verificar
Finalize um lançamento de teste e confirme que o estado e as contagens agregadas correspondem aos itens reportados.

## Conexões
- [[reportportal-attributes]] — Veja também: ReportPortal: classificar com atributos.

## Fontes
- [ReportPortal — Guia de desenvolvedores](https://reportportal.io/docs/developers-guides/ReportingDevelopersGuide/) — lançamentos, itens, identificadores e histórico; consultado em 2026-10-03.
- [ReportPortal — Documentação](https://reportportal.io/docs/) — execuções, lançamentos, defeitos, painéis e integrações; consultado em 2026-10-03.
