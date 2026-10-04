---
id: software.devops.tranche03.000209
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

# Relato de vulnerabilidades em SECURITY.md, grupo cert-manager-dev e reuniões públicas

## Em uma frase
As seções Community, Security Reporting e Changelog do README destacam que a segurança é a prioridade número um do projeto — orientando seguir as instruções em SECURITY.md para reportar vulnerabilidades —, que o Google Group cert-manager-dev é usado para anúncios amplos e coordenação de desenvolvimento (dando acesso também às reuniões públicas detalhadas em cert-manager.io/docs/contributing/#meetings) e que cada release possui changelog no GitHub e notas de versão no site oficial.

## Por que importa
Como o cert-manager lida diretamente com chaves privadas TLS e credenciais de autoridades certificadoras no cluster, acompanhar as notas de release e os avisos de segurança do projeto é indispensável para a governança da plataforma.

## Como funciona
Inscreva-se no grupo cert-manager-dev para acompanhar anúncios do projeto, consulte as notas de release antes de cada atualização e reporte eventuais falhas de segurança de forma privada conforme SECURITY.md.

## Exemplo
Antes de atualizar o cert-manager em produção, a equipe de plataforma lê as release notes em cert-manager.io/docs/release-notes/ para verificar mudanças em flags ou CRDs.

## Limites e trade-offs
Nunca divulgue vulnerabilidades de segurança em issues públicas antes do processo coordenado descrito em SECURITY.md.

## Como verificar
Conferi as seções Community, Security Reporting e Changelog no README oficial de cert-manager/cert-manager.

## Conexões
- [[certmanager-troubleshooting-and-slack-channels]] — Veja também: Fluxo de troubleshooting oficial e canais #cert-manager e #cert-manager-dev no Slack.
- [[certmanager-history-kube-lego-and-kube-cert-manager]] — Veja também: Origem histórica do projeto: evolução a partir do kube-lego e do kube-cert-manager.

## Fontes
- [cert-manager — GitHub README](https://raw.githubusercontent.com/cert-manager/cert-manager/master/README.md) — Visão geral do cert-manager para certificados e emissores no Kubernetes (ACME/Let's Encrypt, HashiCorp Vault, CyberArk, in-cluster), renovação automática, política de módulo Go e histórico kube-lego.; consultado em 2026-10-03.
- [cert-manager — Repositório Oficial no GitHub](https://github.com/cert-manager/cert-manager) — Repositório oficial do cert-manager na CNCF com código-fonte, SECURITY.md e notas de release.; consultado em 2026-10-03.
