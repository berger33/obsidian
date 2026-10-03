---
id: software.testes.tranche15.000949
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

# pgTAP: revisar schema e regex antes de executar funções xUnit

## Em uma frase
Para funções de teste no banco, `pg_prove --runtests` pode usar `--schema` e `--match` para determinar quais rotinas serão encontradas e executadas.

## Por que importa
O filtro facilita particionar uma biblioteca de testes, mas uma expressão errada pode entregar zero funções e criar uma falsa impressão de sucesso.

## Como funciona
Fixar convenções de prefixo e verificar a quantidade descoberta torna o job auditável.

## Exemplo
Agrupe funções no schema `test` com prefixo `test_` e passe `--schema test --match '^test'` ao harness, ajustando a expressão aos nomes reais.

## Limites e trade-offs
Regex corresponde a nomes de função, não a texto de descrição TAP; quoting do shell e case podem mudar seleção, e scripts SQL têm caminho de execução diferente.

## Como verificar
Execute primeiro uma listagem ou dry run quando disponível, confira quantas funções aparecem e faça o job falhar se a seleção esperada ficar vazia.

## Conexões
- [[pgtap-runtests-xunit-setup-e-teardown]] — Veja também: pgTAP: organizar funções xUnit com runtests e lifecycle explícito.

## Fontes
- [pgTAP — pg_prove](https://pgtap.org/pg_prove.html) — execução de scripts SQL e funções xUnit pelo TAP::Harness; consultado em 2026-10-02.
- [pgTAP — Documentation](https://pgtap.org/documentation.html) — assertions TAP, schema, comparações, diretivas e funções de teste; consultado em 2026-10-02.
