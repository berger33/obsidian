---
id: software.devops.tranche01.000051
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/fluxcd/flux2/main/README.md", "https://fluxcd.io/flux/get-started/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Flux v2: sincronização contínua de clusters Kubernetes com fontes Git e artefatos OCI

## Em uma frase
O README oficial no repositório fluxcd/flux2 explica que o Flux é uma ferramenta para manter clusters Kubernetes sincronizados com fontes de configuração (como repositórios Git e artefatos OCI) e automatizar atualizações na configuração quando há novo código a implantar; na versão 2 ("v2"), o Flux foi construído do zero para usar o sistema de extensão de API do Kubernetes, integrar-se com o Prometheus e suportar multi-tenancy e a sincronização de um número arbitrário de repositórios Git.

## Por que importa
Enquanto primeiras gerações de operadores GitOps sincronizavam um único repositório de forma monolítica, o Flux v2 divide a responsabilidade em CRDs nativos do Kubernetes, aceita tanto Git quanto artefatos OCI como fonte, expõe métricas para o Prometheus e permite isolar múltiplos locatários (multi-tenancy) e múltiplos repositórios no mesmo cluster.

## Como funciona
Faça o bootstrap do Flux v2 no cluster seguindo o guia oficial `https://fluxcd.io/flux/get-started/` e declare suas fontes de configuração (Git ou OCI) como Custom Resources do Kubernetes.

## Exemplo
O Flux é um projeto graduado da Cloud Native Computing Foundation (CNCF) e exibe certificação SLSA Level 3 (`fluxcd.io/flux/security/slsa-assessment`) no cabeçalho do repositório.

## Limites e trade-offs
Como o Flux v2 opera inteiramente por meio do sistema de extensão de API do Kubernetes (CRDs e controladores), o estado e os eventos de sincronização são inspecionados diretamente na API do cluster e via métricas do Prometheus.

## Como verificar
Conferi os parágrafos de abertura e os badges no README oficial de `fluxcd/flux2`.

## Conexões
- [[fluxcd-gitops-toolkit-composable-apis]] — Veja também: O GitOps Toolkit: conjunto de APIs componíveis e controladores especializados em Kubernetes.

## Fontes
- [Flux v2 — README oficial](https://raw.githubusercontent.com/fluxcd/flux2/main/README.md) — README oficial do Flux v2 com sincronização Git/OCI, integração Prometheus, multi-tenancy, GitOps Toolkit, as cinco famílias de controladores e todos os seus CRDs, quatro guias práticos e diretrizes de suporte.; consultado em 2026-10-03.
- [Flux — Get Started e documentação oficial](https://fluxcd.io/flux/get-started/) — Guia oficial Get Started do Flux v2 para bootstrap em clusters Kubernetes e entrega contínua GitOps.; consultado em 2026-10-03.
