---
id: software.devops.tranche02.000147
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
fontes: ["https://raw.githubusercontent.com/goharbor/harbor/main/README.md", "https://goharbor.io/docs/latest/install-config/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Opções de implantação: Docker Compose, Helm Chart (harbor-helm) e Harbor Operator

## Em uma frase
As seções `Features` (`Easy deployment`) e `Install & Run` do README informam que o Harbor pode ser implantado via Docker Compose (exigindo em um host Linux `docker 20.10.10-ce+` e `docker-compose 1.18.0+`), via Helm Chart no Kubernetes usando o repositório oficial `goharbor/harbor-helm`, ou por meio do Harbor Operator.

## Por que importa
Essa flexibilidade permite instalar o Harbor tanto em uma máquina virtual Linux dedicada (para servir de registro bootstrap antes mesmo de o cluster Kubernetes existir) quanto dentro de um cluster Kubernetes produtivo com alta disponibilidade via Helm.

## Como funciona
Para hosts Linux standalone, valide os requisitos mínimos (`docker 20.10.10-ce+` e `docker-compose 1.18.0+`) e siga o guia de instalação oficial; para Kubernetes, utilize o chart oficial em `goharbor/harbor-helm`.

## Exemplo
Uma equipe implanta um Harbor inicial em VM via Docker Compose para armazenar as imagens de bootstrap dos nós e um segundo Harbor em alta disponibilidade no Kubernetes via Helm Chart.

## Limites e trade-offs
Ao implantar o Harbor dentro do próprio cluster Kubernetes que ele abastece, evite dependência circular garantindo que as imagens do próprio Harbor e do CNI (como Cilium) não dependam de o Harbor já estar saudável para subir.

## Como verificar
Conferi as seções Features e Install & Run no README oficial de `goharbor/harbor`.

## Conexões
- [[harbor-portal-auditing-and-restful-swagger-api]] — Veja também: Portal gráfico, trilha de auditoria de operações e API RESTful com Swagger UI embutido.
- [[harbor-cosign-release-signature-verification]] — Veja também: Verificação criptográfica de instaladores do Harbor com Cosign a partir da v2.15.0.

## Fontes
- [Harbor — GitHub README](https://raw.githubusercontent.com/goharbor/harbor/main/README.md) — Visão geral do Harbor como registro cloud-native na CNCF, features (RBAC, replicação, scan, LDAP/OIDC, GC, auditoria, API REST), instalação e verificação de assinatura com Cosign (v2.15.0+).; consultado em 2026-10-03.
- [Harbor Documentation — Installation & Configuration Guide](https://goharbor.io/docs/latest/install-config/) — Guia oficial de instalação, configuração e matriz de compatibilidade do Harbor referenciada no README.; consultado em 2026-10-03.
