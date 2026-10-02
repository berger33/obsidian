---
id: software.testes.tranche13.000705
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
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://onsi.github.io/ginkgo/#spec-labels", "https://onsi.github.io/ginkgo/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Ginkgo: selecionar specs por labels declarados

## Em uma frase
Labels associam metadados a specs e filtros permitem selecionar conjuntos sem comentar ou editar a árvore de testes.

## Por que importa
Separar smoke, banco e integração por label permite escolher custo e dependência do job com intenção legível.

## Como funciona
Aplique `Label()` no nó que representa o grupo, use `--label-filter` no runner e defina convenção curta que continue correta quando specs são movidos.

## Exemplo
Um job rápido inclui specs `smoke`, enquanto nightly inclui `database` e `external-service` além dos casos básicos.

## Limites e trade-offs
Filtro incorreto pode excluir precisamente os casos que o job deveria proteger; ausência de label não significa automaticamente leve ou rápido.

## Como verificar
Imprima lista de specs selecionados no job e teste filtros de inclusão e exclusão com nomes de exemplo conhecidos.

## Conexões
- [[ginkgo-random-order-seed]] — Veja também: Ginkgo: reproduzir falha de ordem com seed.
- [[ginkgo-describe-table-entries]] — Veja também: Ginkgo: gerar casos de tabela no estágio de construção.

## Fontes
- [Ginkgo v2 — Spec Labels](https://onsi.github.io/ginkgo/#spec-labels) — label decorators and label-filter selection; consultado em 2026-10-02.
- [Ginkgo v2 — Documentation](https://onsi.github.io/ginkgo/) — spec construction, setup, filtering and execution; consultado em 2026-10-02.
