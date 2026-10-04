---
id: software.testes.tranche19.001333
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
fontes: ["https://reportportal.io/docs/", "https://reportportal.io/docs/log-data-in-reportportal/HowToReportAttributesToReportPortal/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ReportPortal: registrar evidências no item

## Em uma frase
Logs e anexos podem ser enviados para o item ou passo correspondente, ficando disponíveis junto do resultado da execução.

## Por que importa
A evidência no nível do item reduz o tempo de diagnóstico e preserva o contexto exato em que o teste falhou.

## Como funciona
Anexe captura e trecho de log na falha, mantenha os anexos vinculados ao passo e evite registrar dados sensíveis.

## Exemplo
Uma falha na confirmação de pedido pode incluir a captura da tela e o corpo da resposta recebida.

## Limites e trade-offs
Anexar tudo em todas as execuções infla o armazenamento, e anexos no lançamento perdem a associação com o passo que falhou.

## Como verificar
Verifique se a captura anexada corresponde ao instante da falha e não ao estado final da execução.

## Conexões
- [[reportportal-history-and-uniqueness]] — Veja também: ReportPortal: manter histórico por identificador de caso.
- [[reportportal-framework-integration]] — Veja também: ReportPortal: integrar com o framework de testes.

## Fontes
- [ReportPortal — Documentação](https://reportportal.io/docs/) — execuções, lançamentos, defeitos, painéis e integrações; consultado em 2026-10-03.
- [ReportPortal — Atributos](https://reportportal.io/docs/log-data-in-reportportal/HowToReportAttributesToReportPortal/) — atributos de lançamento e de item, filtros e atributos de sistema; consultado em 2026-10-03.
