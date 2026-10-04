---
id: software.devops.tranche03.000204
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

# Guias oficiais para emissão automática de TLS em Ingress (nginx-ingress) e primeiro certificado

## Em uma frase
A seção Documentation do README aponta para a documentação geral em cert-manager.io/docs/ e destaca dois roteiros fundamentais: o guia rápido cert-manager nginx-ingress quick start guide (cert-manager.io/docs/tutorials/acme/nginx-ingress/) para o caso de uso comum de emitir certificados TLS automaticamente para recursos Ingress, e o getting started guide (cert-manager.io/docs/getting-started/) para emitir o primeiro certificado, além da página de instalação (cert-manager.io/docs/installation/).

## Por que importa
A integração direta com controladores de Ingress por meio de anotações permite que desenvolvedores protejam novas rotas HTTPS apenas anotando o manifesto do Ingress sem precisar criar manualmente cada objeto Certificate.

## Como funciona
Siga o tutorial oficial de nginx-ingress ao configurar a emissão automática de certificados ACME para rotas HTTP/HTTPS expostas pelo controlador de Ingress do cluster.

## Exemplo
Ao criar um Ingress anotado com o emissor configurado, o cert-manager detecta o hostname declarado, resolve o desafio ACME e popula o Secret referenciado em spec.tls.

## Limites e trade-offs
Verifique se o firewall e o balanceador de carga permitem o tráfego de entrada necessário para a validação do desafio ACME (como HTTP-01 na porta 80) ou utilize validação DNS-01 quando o serviço não for acessível publicamente.

## Como verificar
Conferi a seção Documentation e a subseção Installation no README oficial de cert-manager/cert-manager.

## Conexões
- [[certmanager-automated-renewal-before-expiry]] — Veja também: Renovação automática antes da expiração para reduzir indisponibilidades e trabalho manual.
- [[certmanager-linux-macos-development-and-coding-conventions]] — Veja também: Requisitos de build em Linux e macOS e convenções de código para contribuidores.

## Fontes
- [cert-manager — GitHub README](https://raw.githubusercontent.com/cert-manager/cert-manager/master/README.md) — Visão geral do cert-manager para certificados e emissores no Kubernetes (ACME/Let's Encrypt, HashiCorp Vault, CyberArk, in-cluster), renovação automática, política de módulo Go e histórico kube-lego.; consultado em 2026-10-03.
- [cert-manager Documentation — Getting Started & Installation](https://cert-manager.io/docs/getting-started/) — Documentação oficial do cert-manager cobrindo instalação, configuração de Issuers/Certificates, nginx-ingress e troubleshooting.; consultado em 2026-10-03.
