---
id: software.testes.tranche13.000700
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
fontes: ["https://onsi.github.io/ginkgo/", "https://pkg.go.dev/github.com/onsi/ginkgo/v2"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Ginkgo: construir árvore de specs antes da execução

## Em uma frase
Ginkgo usa `Describe`, `Context` e `It` para compor uma árvore de especificações que o runner constrói antes de executar os casos.

## Por que importa
O modelo de construção permite filtrar e ordenar specs, mas exige que declarações sejam determinísticas antes do código de teste começar a rodar.

## Como funciona
Declare containers e exemplos no nível de construção, mantenha setup que acessa serviço dentro de nós de execução e evite gerar árvore com resposta de rede em tempo de execução.

## Exemplo
Um pacote pode declarar fluxos de compra por contexto e adicionar `BeforeEach` para preparar usuário antes de cada spec.

## Limites e trade-offs
Código executado ao declarar a árvore roda mesmo quando um filtro depois exclui o spec; não faça efeitos destrutivos no corpo de construção.

## Como verificar
Execute com label que exclui parte da árvore e confirme que nenhum recurso externo foi criado durante simples registro dos specs.

## Conexões
- [[ginkgo-before-after-nesting]] — Veja também: Ginkgo: ordenar setup e cleanup em containers aninhados.

## Fontes
- [Ginkgo v2 — Documentation](https://onsi.github.io/ginkgo/) — spec construction, setup, filtering and execution; consultado em 2026-10-02.
- [Ginkgo v2 — API Reference](https://pkg.go.dev/github.com/onsi/ginkgo/v2) — spec nodes, decorators and reports; consultado em 2026-10-02.
