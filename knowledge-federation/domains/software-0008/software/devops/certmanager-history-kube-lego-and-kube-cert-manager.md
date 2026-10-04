---
id: software.devops.tranche03.000210
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
fontes: ["https://raw.githubusercontent.com/cert-manager/cert-manager/master/README.md", "https://github.com/cert-manager/cert-manager"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Origem histórica do projeto: evolução a partir do kube-lego e do kube-cert-manager

## Em uma frase
A seção History no final do README oficial registra que o cert-manager é baseado no trabalho do projeto kube-lego (github.com/jetstack/kube-lego) e incorporou aprendizados de outros projetos similares da época, como o kube-cert-manager (github.com/PalmStoneGames/kube-cert-manager), consolidando a gestão de certificados na CNCF (com monitoramento no CLOMonitor, Artifact Hub, OpenSSF Scorecard e Best Practices).

## Por que importa
Compreender essa evolução histórica explica por que o cert-manager substituiu controladores limitados apenas ao Let's Encrypt em Ingresses (como o antigo kube-lego) por uma arquitetura extensível de CRDs capaz de atender qualquer tipo de emissor e carga de trabalho no Kubernetes.

## Como funciona
Em clusters legados ou documentações antigas que ainda mencionem anotações do kube-lego, migre integralmente para os recursos e anotações atuais do cert-manager documentados em cert-manager.io/docs/.

## Exemplo
Uma equipe que moderniza manifestos antigos de Kubernetes substitui referências obsoletas ao kube-lego por ClusterIssuers e Certificates gerenciados pelo cert-manager.

## Limites e trade-offs
Ferramentas precursoras como kube-lego e kube-cert-manager são históricas; utilize sempre versões ativamente suportadas do cert-manager.

## Como verificar
Conferi os badges de topo e a seção History no README oficial de cert-manager/cert-manager.

## Conexões
- [[certmanager-security-reporting-and-community-governance]] — Veja também: Relato de vulnerabilidades em SECURITY.md, grupo cert-manager-dev e reuniões públicas.

## Fontes
- [cert-manager — GitHub README](https://raw.githubusercontent.com/cert-manager/cert-manager/master/README.md) — Visão geral do cert-manager para certificados e emissores no Kubernetes (ACME/Let's Encrypt, HashiCorp Vault, CyberArk, in-cluster), renovação automática, política de módulo Go e histórico kube-lego.; consultado em 2026-10-03.
- [cert-manager — Repositório Oficial no GitHub](https://github.com/cert-manager/cert-manager) — Repositório oficial do cert-manager na CNCF com código-fonte, SECURITY.md e notas de release.; consultado em 2026-10-03.
