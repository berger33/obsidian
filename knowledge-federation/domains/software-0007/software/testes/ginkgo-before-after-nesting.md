---
id: software.testes.tranche13.000701
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

# Ginkgo: ordenar setup e cleanup em containers aninhados

## Em uma frase
`BeforeEach` roda para cada spec em seu escopo e hooks aninhados seguem hierarquia do container.

## Por que importa
Preparação por spec ajuda a restaurar estado inicial, enquanto limpeza precisa respeitar recursos criados nos níveis internos e externos.

## Como funciona
Crie fixture no `BeforeEach` mais próximo do consumidor e libere em `AfterEach`; quando há múltiplos níveis, verifique ordem reversa de cleanup.

## Exemplo
Um container de API abre cliente compartilhado e contexto interno cria usuário; o teardown do usuário acontece antes de fechar cliente externo.

## Limites e trade-offs
Closure variable compartilhada dentro da árvore não pode ser mutada concorrentemente sem desenho seguro quando specs paralelizam.

## Como verificar
Faça cleanup registrar ordem e provoque falha no spec; confirme que recursos já criados continuam fechados corretamente.

## Conexões
- [[ginkgo-container-tree]] — Veja também: Ginkgo: construir árvore de specs antes da execução.
- [[ginkgo-suite-synchronized-setup]] — Veja também: Ginkgo: sincronizar recurso compartilhado na suite paralela.

## Fontes
- [Ginkgo v2 — Documentation](https://onsi.github.io/ginkgo/) — spec construction, setup, filtering and execution; consultado em 2026-10-02.
- [Ginkgo v2 — API Reference](https://pkg.go.dev/github.com/onsi/ginkgo/v2) — spec nodes, decorators and reports; consultado em 2026-10-02.
