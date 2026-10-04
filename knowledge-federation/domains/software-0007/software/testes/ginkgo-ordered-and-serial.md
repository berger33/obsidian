---
id: software.testes.tranche18.001211
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://onsi.github.io/ginkgo/", "https://pkg.go.dev/github.com/onsi/ginkgo/v2"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Ginkgo: declarar ordem e serialidade

## Em uma frase
Contêineres podem ser marcados como ordenados, e especificações ou contêineres podem ser declarados seriais para nunca rodarem simultaneamente.

## Por que importa
Alguns fluxos só fazem sentido em sequência, e declarar isso explicitamente preserva o paralelismo do restante da suíte.

## Como funciona
Use contêiner ordenado quando a sequência importa, marque como serial o que não pode coincidir com outras especificações e documente a razão.

## Exemplo
Um fluxo de cadastro seguido de ativação pode rodar em contêiner ordenado, aproveitando o mesmo estado entre as etapas.

## Limites e trade-offs
Ordem declarada sem necessidade reduz o paralelismo, e estado mutável dentro do contêiner ordenado cria dependência oculta entre especificações.

## Como verificar
Execute a suíte em paralelo com o contêiner ordenado e confirme que as etapas ocorreram na ordem declarada.

## Conexões
- [[ginkgo-parallel-execution]] — Veja também: Ginkgo: executar especificações em paralelo.
- [[ginkgo-labels-and-filtering]] — Veja também: Ginkgo: selecionar especificações com etiquetas.

## Fontes
- [Ginkgo — Documentation](https://onsi.github.io/ginkgo/) — contêineres, nós de preparação, paralelismo, etiquetas e relatórios; consultado em 2026-10-03.
- [Ginkgo — pacote publicado](https://pkg.go.dev/github.com/onsi/ginkgo/v2) — API pública, decoradores e funções de execução; consultado em 2026-10-03.
