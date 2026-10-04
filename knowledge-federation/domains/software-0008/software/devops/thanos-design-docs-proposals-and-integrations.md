---
id: software.devops.tranche02.000159
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/thanos-io/thanos/main/README.md", "https://thanos.io/tip/thanos/getting-started.md/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Documentação de partida: Getting Started, Design, Proposals e Integrations

## Em uma frase
A seção `Getting Started` do README reúne os pontos de entrada oficiais da documentação técnica do projeto: `Getting Started` (`thanos.io/tip/thanos/getting-started.md/`), `Design` (`thanos.io/tip/thanos/design.md/`), `Blog posts` e `Talks` (`docs/getting-started.md`), `Proposals` (`docs/proposals-done`) e `Integrations` (`docs/integrations.md`), além da referência de código Go em `pkg.go.dev/github.com/thanos-io/thanos`.

## Por que importa
Antes de desenhar a topologia de métricas de longa duração de uma empresa, ler o documento de `Design`, as propostas concluídas em `docs/proposals-done` e o catálogo `docs/integrations.md` evita reinventar padrões já resolvidos pela comunidade.

## Como funciona
Consulte `thanos.io/tip/thanos/design.md/` para entender as garantias de consistência e falha de cada componente e `docs/integrations.md` para integrar o Thanos com ferramentas de alerta, visualização e armazenamento.

## Exemplo
Um arquiteto revisa `thanos.io/tip/thanos/design.md/` e `docs/proposals-done` para dimensionar o armazenamento de objetos e a camada de consulta do Thanos.

## Limites e trade-offs
Verifique sempre se a documentação consultada (`tip` vs versão específica) corresponde às flags da versão do binário `thanos` implantada no seu cluster.

## Como verificar
Conferi os badges de topo e a seção Getting Started no README oficial de `thanos-io/thanos`.

## Conexões
- [[thanos-release-cadence-six-weeks-and-container-registries]] — Veja também: Cadência de releases menores a cada seis semanas e imagens em Quay.io e Docker Hub.
- [[thanos-community-adopters-and-maintainers-governance]] — Veja também: Comunidade no CNCF Slack, lista de adotantes em adopters.yml e MAINTAINERS.md.

## Fontes
- [Thanos — GitHub README](https://raw.githubusercontent.com/thanos-io/thanos/main/README.md) — Visão geral do Thanos (CNCF Incubating), objetivos sobre o formato Prometheus 2.0, deduplicação HA, Store API gRPC, arquiteturas Sidecar vs Receive, filosofia UNIX/Go e releases a cada 6 semanas.; consultado em 2026-10-03.
- [Thanos Documentation — Getting Started & Design](https://thanos.io/tip/thanos/getting-started.md/) — Documentação oficial de introdução e design arquitetural do Thanos referenciada no README.; consultado em 2026-10-03.
