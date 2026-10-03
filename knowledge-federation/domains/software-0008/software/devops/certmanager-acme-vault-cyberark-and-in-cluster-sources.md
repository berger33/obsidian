---
id: software.devops.tranche03.000202
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/cert-manager/cert-manager/master/README.md", "https://cert-manager.io/docs/getting-started/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fontes de emissão suportadas: Let's Encrypt (ACME), HashiCorp Vault, CyberArk e emissão local

## Em uma frase
O segundo parágrafo do README oficial destaca que o cert-manager suporta a emissão de certificados a partir de diversas fontes, incluindo Let's Encrypt (via protocolo ACME), HashiCorp Vault e CyberArk Certificate Manager, bem como emissão local dentro do próprio cluster (local in-cluster issuance, como CA interna ou self-signed).

## Por que importa
Ambientes corporativos frequentemente combinam certificados públicos válidos em navegadores (ACME/Let's Encrypt) na borda com autoridades certificadoras privadas (HashiCorp Vault, CyberArk ou CA interna do cluster) para tráfego leste-oeste e mTLS entre microsserviços.

## Como funciona
Configure emissores distintos para cada fronteira de confiança: ACME (Let's Encrypt) para endpoints públicos de entrada e HashiCorp Vault, CyberArk ou CA in-cluster para serviços internos e webhooks.

## Exemplo
Uma plataforma usa um ClusterIssuer ACME para os Ingresses públicos e um Issuer conectado ao HashiCorp Vault para emitir certificados de curta duração para comunicação interna.

## Limites e trade-offs
Emissores públicos baseados em Let's Encrypt possuem limites estritos de taxa (rate limits); utilize o ambiente de staging do ACME ao testar configurações novas antes de apontar para o endpoint de produção.

## Como verificar
Conferi o segundo parágrafo da abertura do README oficial de cert-manager/cert-manager.

## Conexões
- [[certmanager-x509-certificates-and-issuers-resources]] — Veja também: Certificados e emissores de certificados como recursos nativos do Kubernetes.
- [[certmanager-automated-renewal-before-expiry]] — Veja também: Renovação automática antes da expiração para reduzir indisponibilidades e trabalho manual.

## Fontes
- [cert-manager — GitHub README](https://raw.githubusercontent.com/cert-manager/cert-manager/master/README.md) — Visão geral do cert-manager para certificados e emissores no Kubernetes (ACME/Let's Encrypt, HashiCorp Vault, CyberArk, in-cluster), renovação automática, política de módulo Go e histórico kube-lego.; consultado em 2026-10-03.
- [cert-manager Documentation — Getting Started & Installation](https://cert-manager.io/docs/getting-started/) — Documentação oficial do cert-manager cobrindo instalação, configuração de Issuers/Certificates, nginx-ingress e troubleshooting.; consultado em 2026-10-03.
