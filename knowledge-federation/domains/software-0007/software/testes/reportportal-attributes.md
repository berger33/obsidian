---
id: software.testes.tranche19.001329
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
fontes: ["https://reportportal.io/docs/log-data-in-reportportal/HowToReportAttributesToReportPortal/", "https://reportportal.io/docs/test-executions/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ReportPortal: classificar com atributos

## Em uma frase
Atributos são pares de chave e valor anexados ao lançamento ou ao item e usados em filtros, colunas e agrupamentos.

## Por que importa
A classificação consistente permite comparar execuções por componente, ambiente e tipo de teste sem depender do nome do caso.

## Como funciona
Defina um conjunto pequeno de chaves estáveis, aplique-as na origem da execução e use-as nos filtros em vez de codificar no nome.

## Exemplo
Um lançamento pode declarar o ambiente e o ramo, enquanto cada item indica o componente a que pertence.

## Limites e trade-offs
Chaves inconsistentes entre times inviabilizam filtros conjuntos, e atributos em excesso tornam a interface poluída e a manutenção pesada.

## Como verificar
Filtre uma execução por componente e confirme que o resultado inclui exatamente os itens marcados com aquele valor.

## Conexões
- [[reportportal-launches-and-items]] — Veja também: ReportPortal: organizar lançamentos e itens.
- [[reportportal-system-attributes]] — Veja também: ReportPortal: controlar o processamento com atributos de sistema.

## Fontes
- [ReportPortal — Atributos](https://reportportal.io/docs/log-data-in-reportportal/HowToReportAttributesToReportPortal/) — atributos de lançamento e de item, filtros e atributos de sistema; consultado em 2026-10-03.
- [ReportPortal — Execuções de teste](https://reportportal.io/docs/test-executions/) — filtros, colunas personalizadas e visões de acompanhamento; consultado em 2026-10-03.
