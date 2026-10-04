---
id: software.testes.tranche18.001208
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

# Ginkgo: preparar estado nos nós de preparação

## Em uma frase
Nós de preparação são executados antes e depois de cada especificação, com variantes de suíte e de contêiner ordenado.

## Por que importa
Os nós mantêm cada especificação independente e permitem que a ordem das especificações seja embaralhada com segurança.

## Como funciona
Declare a preparação no nível mais próximo do uso e inicialize os dados ali, em vez de construí-los na declaração do contêiner.

## Exemplo
Um nó pode criar o registro necessário e outro removê-lo ao final da especificação.

## Limites e trade-offs
Preparações que compartilham estado entre especificações quebram o embaralhamento, e a construção de objetos na declaração os compartilha entre todas as execuções.

## Como verificar
Embaralhe a ordem das especificações e confirme que o resultado permanece o mesmo.

## Conexões
- [[ginkgo-container-nodes]] — Veja também: Ginkgo: organizar especificações em contêineres.
- [[ginkgo-subject-and-assertions]] — Veja também: Ginkgo: verificar comportamento com asserções.

## Fontes
- [Ginkgo — Documentation](https://onsi.github.io/ginkgo/) — contêineres, nós de preparação, paralelismo, etiquetas e relatórios; consultado em 2026-10-03.
- [Ginkgo — pacote publicado](https://pkg.go.dev/github.com/onsi/ginkgo/v2) — API pública, decoradores e funções de execução; consultado em 2026-10-03.
