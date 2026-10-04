---
id: software.testes.tranche19.001332
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

# ReportPortal: manter histórico por identificador de caso

## Em uma frase
A plataforma liga execuções históricas do mesmo caso por identificador derivado da localização no código e dos parâmetros, que pode ser definido explicitamente.

## Por que importa
O histórico por identificador estável revela se o caso falha de forma recorrente e se a correção surtiu efeito.

## Como funciona
Mantenha o identificador derivado enquanto a estrutura permitir e defina explicitamente quando houver vínculo com sistema externo de casos.

## Exemplo
Um caso pode ser acompanhado ao longo de várias execuções, mostrando alternância entre aprovado e falho.

## Limites e trade-offs
Alterar o identificador desvincula o histórico anterior, e identificadores que mudam a cada execução fazem cada resultado parecer inédito.

## Como verificar
Consulte o histórico de um caso antes e depois de mudar o identificador e observe a perda de continuidade.

## Conexões
- [[reportportal-defect-classification]] — Veja também: ReportPortal: classificar causas com análise automática.
- [[reportportal-attachments-and-logs]] — Veja também: ReportPortal: registrar evidências no item.

## Fontes
- [ReportPortal — Guia de desenvolvedores](https://reportportal.io/docs/developers-guides/ReportingDevelopersGuide/) — lançamentos, itens, identificadores e histórico; consultado em 2026-10-03.
- [ReportPortal — Documentação](https://reportportal.io/docs/) — execuções, lançamentos, defeitos, painéis e integrações; consultado em 2026-10-03.
