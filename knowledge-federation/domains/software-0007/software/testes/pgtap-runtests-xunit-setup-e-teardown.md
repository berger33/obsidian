---
id: software.testes.tranche15.000948
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
fontes: ["https://pgtap.org/pg_prove.html", "https://pgtap.org/documentation.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pgTAP: organizar funções xUnit com runtests e lifecycle explícito

## Em uma frase
A função `runtests()` encontra e executa funções de teste, gera plano TAP e oferece suporte a startup, shutdown, setup, teardown e rollback entre testes.

## Por que importa
O estilo xUnit é útil quando a equipe prefere funções persistentes no banco; a ferramenta pode executar grupos por schema e regex de nome através do pg_prove.

## Como funciona
O lifecycle separa preparação comum da verificação de cada função.

## Exemplo
Crie funções que retornam `SETOF TEXT` no schema de teste e rode `pg_prove --dbname testdb --schema tests --match '^test'`; use setup/teardown para fixtures que devam ser isoladas.

## Limites e trade-offs
Funções xUnit dependem de objetos já carregados no banco e regex incorreta pode selecionar nenhum teste; não assuma que scripts de instalação sejam executados pelo comando de harness.

## Como verificar
Invente uma função `test_` que passa, outra que falha e uma fixture de setup, depois confirme que ambas entram no TAP e que rollback deixa o schema no estado esperado.

## Conexões
- [[pgtap-pg-prove-e-tap-harness]] — Veja também: pg_prove: usar TAP::Harness para agregar scripts de teste.
- [[pgtap-runtests-schema-e-match-filtros]] — Veja também: pgTAP: revisar schema e regex antes de executar funções xUnit.

## Fontes
- [pgTAP — pg_prove](https://pgtap.org/pg_prove.html) — execução de scripts SQL e funções xUnit pelo TAP::Harness; consultado em 2026-10-02.
- [pgTAP — Documentation](https://pgtap.org/documentation.html) — assertions TAP, schema, comparações, diretivas e funções de teste; consultado em 2026-10-02.
