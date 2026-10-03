---
id: software.testes.tranche22.001637
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://github.com/getsentry/responses/blob/master/README.rst", "https://pypi.org/project/responses/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# responses: deixar alguns requests passarem

## Em uma frase
O add_passthru("https://percy.io") abre exceção seletiva ao bloqueio total: pedidos cuja URL casa com o prefixo atravessam o mock e chegam ao servidor real.

## Por que importa
Integrações que só precisam de um endpoint externo autêntico (upload de snapshot, webhooks) não justificam levantar um servidor de teste; o passthru delimita por prefixo o que pode falar com o mundo.

## Como funciona
O snippet do README é de duas linhas: @responses.activate + responses.add_passthru("https://percy.io"), e o resto do teste continua mockado.

## Exemplo
O migration table documenta passthru_prefixes acessível via responses.mock.passthru_prefixes — a lista é estado do mock ativo, não global solto.

## Limites e trade-offs
Passthru num teste unitário reabre o ponto de falha que o mock eliminou (rede, latency, estado do serviço externo); reserve-o para quando o par real é o contrato.

## Como verificar
Adicione um passthru para o seu host de teste local e confirme que um registro com mesma URL tem precedência sobre o prefixo (ou não, e registre a ordem).

## Conexões
- [[responses-matchers]] — Veja também: responses: match() com matchers combináveis.
- [[responses-calls-inspection]] — Veja também: responses: o histórico em responses.calls.

## Fontes
- [responses — README oficial](https://github.com/getsentry/responses/blob/master/README.rst) — activate, add, atalhos, matchers, registry e passthru; consultado em 2026-10-03.
- [responses — página no PyPI](https://pypi.org/project/responses/) — release canônica e badge do pacote; consultado em 2026-10-03.
