---
id: software.devops.tranche03.000203
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

# Renovação automática antes da expiração para reduzir indisponibilidades e trabalho manual

## Em uma frase
O terceiro parágrafo da abertura do README explica que o cert-manager garante que os certificados permaneçam válidos e atualizados, tentando renová-los em um momento apropriado antes do vencimento (at an appropriate time before expiry) para reduzir o risco de indisponibilidades (outages) e eliminar o trabalho operacional repetitivo (toil).

## Por que importa
Quedas de sistemas críticos causadas por certificados TLS esquecidos que venceram na madrugada estão entre os incidentes mais comuns e evitáveis em operações de infraestrutura.

## Como funciona
Deixe o controlador do cert-manager monitorar continuamente a data de expiração dos certificados emitidos e monitore as métricas e eventos de renovação para agir caso algum desafio ACME ou conexão com a CA falhe.

## Exemplo
Antes que o certificado de um Ingress público expire, o cert-manager executa automaticamente o fluxo de renovação junto à autoridade certificadora e atualiza o Secret TLS correspondente no Kubernetes.

## Limites e trade-offs
A atualização do Secret no Kubernetes é automática, mas aplicações que carregam o certificado apenas na inicialização do processo precisam recarregar o arquivo montado ou ser reiniciadas para servir o novo certificado.

## Como verificar
Conferi o terceiro parágrafo da seção cert-manager no README oficial de cert-manager/cert-manager.

## Conexões
- [[certmanager-acme-vault-cyberark-and-in-cluster-sources]] — Veja também: Fontes de emissão suportadas: Let's Encrypt (ACME), HashiCorp Vault, CyberArk e emissão local.
- [[certmanager-nginx-ingress-and-getting-started-guides]] — Veja também: Guias oficiais para emissão automática de TLS em Ingress (nginx-ingress) e primeiro certificado.

## Fontes
- [cert-manager — GitHub README](https://raw.githubusercontent.com/cert-manager/cert-manager/master/README.md) — Visão geral do cert-manager para certificados e emissores no Kubernetes (ACME/Let's Encrypt, HashiCorp Vault, CyberArk, in-cluster), renovação automática, política de módulo Go e histórico kube-lego.; consultado em 2026-10-03.
- [cert-manager Documentation — Getting Started & Installation](https://cert-manager.io/docs/getting-started/) — Documentação oficial do cert-manager cobrindo instalação, configuração de Issuers/Certificates, nginx-ingress e troubleshooting.; consultado em 2026-10-03.
