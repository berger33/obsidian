---
id: software.devops.tranche02.000158
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
fontes: ["https://raw.githubusercontent.com/thanos-io/thanos/main/README.md", "https://github.com/thanos-io/thanos"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Cadência de releases menores a cada seis semanas e imagens em Quay.io e Docker Hub

## Em uma frase
A seção `Releases` do README documenta que a branch `main` deve permanecer estável e utilizável — gerando a cada commit uma imagem Docker nomeada `main-<date>-<sha>` em `quay.io/thanos/thanos` e no espelho `thanosio/thanos` no Docker Hub — e que o projeto realiza **releases menores a cada 6 semanas** (`minor releases every 6 weeks`), produzindo tarballs para as principais plataformas e imagens Docker conforme documentado em `docs/release-process.md`.

## Por que importa
Conhecer a cadência de 6 semanas para versões menores e os registros oficiais (`quay.io/thanos/thanos` e `hub.docker.com/r/thanosio/thanos`) permite planejar espelhamento de imagens no Harbor corporativo e janelas regulares de atualização.

## Como funciona
Em produção, fixe versões semânticas estáveis lançadas no ciclo de 6 semanas (evitando imagens `main-<date>-<sha>` de commit contínuo) e consulte `docs/release-process.md` para detalhes de empacotamento.

## Exemplo
A automação de plataforma sincroniza a cada 6 semanas a nova release menor do Thanos de `quay.io/thanos/thanos` para o registro interno após validação em homologação.

## Limites e trade-offs
As builds de commit `main-<date>-<sha>` são úteis para testar correções recentes, mas ambientes produtivos devem rodar tags de release formalmente lançadas.

## Como verificar
Conferi a seção Releases no README oficial de `thanos-io/thanos`.

## Conexões
- [[thanos-unix-and-golang-design-philosophy]] — Veja também: Filosofia UNIX e Go no design do Thanos: um binário com subcomandos coesos.
- [[thanos-design-docs-proposals-and-integrations]] — Veja também: Documentação de partida: Getting Started, Design, Proposals e Integrations.

## Fontes
- [Thanos — GitHub README](https://raw.githubusercontent.com/thanos-io/thanos/main/README.md) — Visão geral do Thanos (CNCF Incubating), objetivos sobre o formato Prometheus 2.0, deduplicação HA, Store API gRPC, arquiteturas Sidecar vs Receive, filosofia UNIX/Go e releases a cada 6 semanas.; consultado em 2026-10-03.
- [Thanos — Repositório Oficial no GitHub](https://github.com/thanos-io/thanos) — Repositório oficial do Thanos com código-fonte em Go, docs/proposals-done, docs/integrations.md e website/data/adopters.yml.; consultado em 2026-10-03.
