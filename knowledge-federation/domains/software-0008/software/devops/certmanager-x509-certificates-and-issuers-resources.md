---
id: software.devops.tranche03.000201
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

# Certificados e emissores de certificados como recursos nativos do Kubernetes

## Em uma frase
O README oficial no repositório cert-manager/cert-manager define o cert-manager como o projeto que adiciona certificados (certificates) e emissores de certificados (certificate issuers) como tipos de recursos nativos em clusters Kubernetes, simplificando o processo de obter, renovar e utilizar esses certificados.

## Por que importa
Sem um controlador declarativo no cluster, equipes acabam gerando certificados TLS manualmente fora do Kubernetes e colando arquivos em objetos Secret estáticos que expiram silenciosamente em produção.

## Como funciona
Declare objetos Issuer/ClusterIssuer e Certificate (ou anotações em recursos de Ingress/Gateway) para que o cert-manager gerencie o ciclo de vida completo dos segredos TLS no Kubernetes.

## Exemplo
Um serviço exposto via HTTPS declara um recurso Certificate no mesmo namespace da aplicação e consome o Secret TLS preenchido automaticamente pelo cert-manager.

## Limites e trade-offs
Adicionar os tipos de recursos exige instalar previamente as CustomResourceDefinitions (CRDs) correspondentes à versão exata dos controladores do cert-manager.

## Como verificar
Conferi o primeiro parágrafo da seção cert-manager no README oficial de cert-manager/cert-manager.

## Conexões
- [[certmanager-acme-vault-cyberark-and-in-cluster-sources]] — Veja também: Fontes de emissão suportadas: Let's Encrypt (ACME), HashiCorp Vault, CyberArk e emissão local.

## Fontes
- [cert-manager — GitHub README](https://raw.githubusercontent.com/cert-manager/cert-manager/master/README.md) — Visão geral do cert-manager para certificados e emissores no Kubernetes (ACME/Let's Encrypt, HashiCorp Vault, CyberArk, in-cluster), renovação automática, política de módulo Go e histórico kube-lego.; consultado em 2026-10-03.
- [cert-manager Documentation — Getting Started & Installation](https://cert-manager.io/docs/getting-started/) — Documentação oficial do cert-manager cobrindo instalação, configuração de Issuers/Certificates, nginx-ingress e troubleshooting.; consultado em 2026-10-03.
