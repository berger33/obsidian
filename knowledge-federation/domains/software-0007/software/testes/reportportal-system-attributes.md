---
id: software.testes.tranche19.001330
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
fontes: ["https://reportportal.io/docs/log-data-in-reportportal/HowToReportAttributesToReportPortal/", "https://reportportal.io/docs/developers-guides/ReportingDevelopersGuide/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ReportPortal: controlar o processamento com atributos de sistema

## Em uma frase
Atributos de sistema alteram o comportamento da plataforma, disparando análise imediata, tratando itens ignorados ou marcando reversões.

## Por que importa
Esses atributos evitam esperar o fim do lançamento para obter análise e ajustam a classificação de itens que não representam defeito.

## Como funciona
Declare apenas os atributos de sistema necessários, com valor explícito, e documente o efeito pretendido no projeto.

## Exemplo
Um lançamento pode pedir análise imediata dos itens, recebendo a classificação de causa assim que cada teste termina.

## Limites e trade-offs
Sem documentação, os atributos de sistema viram configuração oculta, e o efeito se perde quando alguém altera a integração.

## Como verificar
Ative a análise imediata e confirme que itens concluídos já aparecem analisados antes do fim do lançamento.

## Conexões
- [[reportportal-attributes]] — Veja também: ReportPortal: classificar com atributos.
- [[reportportal-defect-classification]] — Veja também: ReportPortal: classificar causas com análise automática.

## Fontes
- [ReportPortal — Atributos](https://reportportal.io/docs/log-data-in-reportportal/HowToReportAttributesToReportPortal/) — atributos de lançamento e de item, filtros e atributos de sistema; consultado em 2026-10-03.
- [ReportPortal — Guia de desenvolvedores](https://reportportal.io/docs/developers-guides/ReportingDevelopersGuide/) — lançamentos, itens, identificadores e histórico; consultado em 2026-10-03.
