---
id: software.seguranca.tranche19.001847
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-19.md"
fontes: ["https://cert-manager.io/docs/usage/certificate/", "https://cert-manager.io/docs/configuration/issuers/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# cert-manager: Proteger Secret da chave privada

## Em uma frase
**cert-manager — Proteger Secret da chave privada:** Private key é armazenada em Secret Kubernetes associado ao Certificate e requer RBAC restrito.

## Por que importa
O recorte de **proteger secret da chave privada** ajuda a automatizar ciclo de vida de certificados TLS com configuração declarativa e integração a workloads. A equipe registra risco, evidência e responsável.

## Como funciona
Para **proteger secret da chave privada**, Certificate referencia Issuer ou ClusterIssuer; o controller solicita certificado, grava Secret e acompanha renovação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Limite leitura do Secret ao controller de ingress e workload que realmente consome o certificado. Teste em staging autorizado.

## Limites e trade-offs
Control plane access ou backup aberto pode expor chave privada mesmo com TLS válido. Exceções exigem responsável e prazo.

## Como verificar
Revise RoleBindings, encryption at rest e permissões de cópia do Secret. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cert-manager-selecionar-solver-pelo-dominio]] — Complementa o tópico com cert-manager: selecionar solver pelo domínio.

## Fontes
- [cert-manager — Certificate usage](https://cert-manager.io/docs/usage/certificate/) — guia oficial de recursos Certificate, issuerRef, Secret e renovação; consultado em 2026-10-04.
- [cert-manager — Issuers](https://cert-manager.io/docs/configuration/issuers/) — documentação oficial de Issuer, ClusterIssuer e tipos de autoridade; consultado em 2026-10-04.
