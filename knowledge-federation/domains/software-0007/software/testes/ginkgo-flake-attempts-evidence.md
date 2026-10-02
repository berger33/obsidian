---
id: software.testes.tranche13.000709
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
fontes: ["https://onsi.github.io/ginkgo/MIGRATING_TO_V2#spec-decorators", "https://pkg.go.dev/github.com/onsi/ginkgo/v2"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Ginkgo: deixar FlakeAttempts visível no relatório

## Em uma frase
`FlakeAttempts` permite executar novamente um spec marcado como flakey até o limite definido.

## Por que importa
Retry pode fornecer evidência sobre intermitência, mas o passe final não deve apagar a tentativa que falhou inicialmente.

## Como funciona
Use decorator de forma temporária ou para caso reconhecidamente instável, preserve contagem de tentativas e abra correção da condição que torna o teste flakey.

## Exemplo
Um spec de integração pode ser repetido algumas vezes para capturar falhas por estado eventual e deixar número de tentativas no relatório de teste.

## Limites e trade-offs
Retry consome tempo e pode mascarar defeito determinístico ou duplicar operação externa; recursos de escrita precisam de idempotência.

## Como verificar
Cause uma falha na primeira tentativa e verifique no relatório que houve retry e que estado final não esconde o número de tentativas.

## Conexões
- [[ginkgo-consistently-window]] — Veja também: Gomega: usar Consistently para ausência durante janela.

## Fontes
- [Ginkgo v2 — FlakeAttempts Decorator](https://onsi.github.io/ginkgo/MIGRATING_TO_V2#spec-decorators) — decorator retry limits and CLI override behavior; consultado em 2026-10-02.
- [Ginkgo v2 — API Reference](https://pkg.go.dev/github.com/onsi/ginkgo/v2) — spec nodes, decorators and reports; consultado em 2026-10-02.
