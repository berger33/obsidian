---
id: software.testes.tranche19.001336
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
fontes: ["https://reportportal.io/docs/test-executions/", "https://reportportal.io/docs/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ReportPortal: acompanhar com filtros e painéis

## Em uma frase
A plataforma permite filtrar execuções e itens por período, nome, atributos e estado, além de montar colunas personalizadas e visões salvas.

## Por que importa
Filtros estáveis transformam os dados coletados em acompanhamento útil para o time e para quem decide prioridades.

## Como funciona
Salve filtros por componente e por tipo de execução, personalize colunas com os atributos relevantes e compartilhe as visões com o time.

## Exemplo
Uma visão pode mostrar apenas os casos do componente de pagamentos nas últimas duas semanas, com o histórico de cada um.

## Limites e trade-offs
Filtros que dependem de nomes de lançamento mudam a cada alteração do pipeline e deixam as visões vazias.

## Como verificar
Aplique um filtro salvo após uma renomeação de lançamento e verifique se a visão continua retornando os dados esperados.

## Conexões
- [[reportportal-modes-and-projects]] — Veja também: ReportPortal: separar modos de execução e projetos.
- [[reportportal-limits-and-practices]] — Veja também: ReportPortal: reconhecer limites da plataforma.

## Fontes
- [ReportPortal — Execuções de teste](https://reportportal.io/docs/test-executions/) — filtros, colunas personalizadas e visões de acompanhamento; consultado em 2026-10-03.
- [ReportPortal — Documentação](https://reportportal.io/docs/) — execuções, lançamentos, defeitos, painéis e integrações; consultado em 2026-10-03.
