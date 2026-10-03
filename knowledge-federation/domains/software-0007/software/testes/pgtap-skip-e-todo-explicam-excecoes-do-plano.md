---
id: software.testes.tranche15.000945
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
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://pgtap.org/documentation.html", "https://pgtap.org/pg_prove.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pgTAP: representar temporariamente testes ignorados ou conhecidos como TODO

## Em uma frase
Diretivas TAP `skip` e `todo` registram exceções explícitas no plano de teste, permitindo que uma verificação condicional ou uma falha conhecida continue visível no output.

## Por que importa
Pular não equivale a passar: o resultado documenta que uma assertion não foi exercitada.

## Como funciona
TODO sinaliza um resultado previsto como ainda não resolvido, útil para tornar a dívida observável sem fingir que o comportamento está correto.

## Exemplo
Use `skip(reason, how_many)` sob uma condição que realmente torna o recurso indisponível e use `todo(reason, how_many)` para um caso reconhecido como trabalho futuro.

## Limites e trade-offs
Skip amplo pode esconder perda permanente de cobertura e TODO pode permanecer indefinidamente; inclua motivo, escopo e condição de remoção em cada diretiva.

## Como verificar
Rode com a feature ativa e inativa, examine output TAP em ambos e confirme que a quantidade de casos ignorados não muda silenciosamente em CI.

## Conexões
- [[pgtap-throws-ok-contrato-de-excecao]] — Veja também: pgTAP: validar SQLSTATE e mensagem de operações que devem falhar.
- [[pgtap-sql-script-em-transacao-com-rollback]] — Veja também: pgTAP: isolar efeitos de script com transação e rollback.

## Fontes
- [pgTAP — Documentation](https://pgtap.org/documentation.html) — assertions TAP, schema, comparações, diretivas e funções de teste; consultado em 2026-10-02.
- [pgTAP — pg_prove](https://pgtap.org/pg_prove.html) — execução de scripts SQL e funções xUnit pelo TAP::Harness; consultado em 2026-10-02.
