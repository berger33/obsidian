---
id: software.devops.tranche02.000128
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
fontes: ["https://raw.githubusercontent.com/cilium/cilium/main/README.rst", "https://docs.cilium.io/en/stable/overview/component-overview/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Política de manutenção das três últimas versões menores estáveis do Cilium

## Em uma frase
A seção `Stable Releases` do `README.rst` estabelece que a comunidade Cilium mantém releases estáveis menores para as **três últimas versões menores** do Cilium (`last three minor Cilium versions`), considerando versões anteriores como fim de vida (EOL), listando na tabela de branches ativas as séries `v1.20` (`quay.io/cilium/cilium:v1.20.2`), `v1.19` (`quay.io/cilium/cilium:v1.19.8`) e `v1.18` (`quay.io/cilium/cilium:v1.18.14`), além de apontar para o `Cilium Upgrade Guide` (`docs.cilium.io/en/stable/operations/upgrade/`).

## Por que importa
Como o CNI é um componente crítico de infraestrutura de todos os nós do cluster, permanecer em uma série fora das três últimas versões menores deixa o dataplane sem patches de segurança e correções de bugs.

## Como funciona
Planeje atualizações regulares do Cilium seguindo o `Cilium Upgrade Guide` oficial para manter toda a frota dentro das três séries menores suportadas (`v1.18`, `v1.19` ou `v1.20`) e utilize sempre tags de versão explícitas em produção.

## Exemplo
Uma equipe operando Cilium `v1.18` programa o upgrade para `v1.19` e `v1.20` antes do lançamento da série `v1.21` estável.

## Limites e trade-offs
As imagens de desenvolvimento (`quay.io/cilium/cilium-ci:latest` e snapshots `pre`) listadas na seção `Development` destinam-se apenas a testes e nunca devem ser usadas em produção.

## Como verificar
Conferi as seções Stable Releases e Development em `README.rst` de `cilium/cilium`.

## Conexões
- [[cilium-hubble-observability-and-drop-reasons]] — Veja também: Observabilidade integrada com Hubble, métricas Prometheus e motivos de descarte.
- [[cilium-multi-arch-images-and-spdx-sbom]] — Veja também: Distribuição de imagens AMD64/AArch64 e SBOM em formato SPDX desde a v1.13.0.

## Fontes
- [Cilium — GitHub README.rst](https://raw.githubusercontent.com/cilium/cilium/main/README.rst) — Visão geral do Cilium (dataplane eBPF, CNI overlay/native/BGP, substituição do kube-proxy, Cluster Mesh, Network Policy L3-L7/DNS, Service Mesh, Hubble, releases estáveis, SBOM SPDX e licenças).; consultado em 2026-10-03.
- [Cilium Documentation — Architecture and Component Overview](https://docs.cilium.io/en/stable/overview/component-overview/) — Documentação oficial de arquitetura, requisitos de sistema e operação do Cilium referenciada no README.; consultado em 2026-10-03.
