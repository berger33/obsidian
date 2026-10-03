---
id: software.seguranca.tranche05.000444
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/paralus/paralus/main/README.md", "https://www.paralus.io/docs/", "https://www.paralus.io/docs/usage/audit-logs"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CNCF Paralus: Federação SSO com Provedores OIDC (Okta, Microsoft Entra ID, Google, Keycloak e GitHub) e Mapeamento de Grupos

## Em uma frase
O Paralus integra-se nativamente a provedores de identidade externos compatíveis com **OpenID Connect (OIDC)** — incluindo Okta, Microsoft Entra ID (Azure AD), Google Workspace, Keycloak, Dex e GitHub — sincronizando usuários e grupos automaticamente no momento do login.

## Por que importa
Garante que o desligamento de um funcionário ou a remoção de um engenheiro de um grupo no IdP corporativo revogue o seu acesso a todos os clusters Kubernetes sem necessidade de intervenção manual em cada cluster.

## Como funciona
Ao configurar um *Identity Provider* no Paralus (informando `Client ID`, `Client Secret`, `Issuer URL` e escopos `openid`, `profile`, `email`, `groups`), os claims de grupo retornados pelo IdP são mapeados diretamente para **Groups** do Paralus, que já possuem os projetos, clusters, namespaces e roles pré-associados.

## Exemplo
```yaml
# Exemplo de configuração de provedor OIDC corporativo no Paralus
name: "corp-okta-oidc"
idpType: "generic-oidc"
domain: "corp.example.com"
clientId: "0oa9x8y7z6sigstore"
issuerUrl: "https://sso.corp.example.com/oauth2/default"
scopes:
  - openid
  - profile
  - email
  - groups
groupAttributeName: "groups"
```

## Limites e trade-offs
Se o IdP OIDC não incluir a claim `groups` no ID Token (ou se o nome do atributo configurado em `groupAttributeName` divergir do emitido pelo IdP), o usuário fará login via SSO mas cairá sem permissões de grupo atribuídas.

## Como verificar
Realize login via SSO com um usuário de teste e verifique na seção *Users* do Paralus que os grupos provenientes do IdP foram associados automaticamente.

## Conexões
- [[paralus-organizacao-projects-groups-custom-roles-namespace-rbac]] — Veja também: CNCF Paralus: Modelo Multi-Tenant com `Projects`, `Groups`, Papéis Pré-Configurados e `Custom Roles` por Namespace.
- [[paralus-kubeconfig-dinamico-just-in-time-serviceaccounts-revogacao]] — Veja também: CNCF Paralus: Provisionamento *Just-in-Time* de ServiceAccounts, `kubeconfig` Auditado e Revogação Instantânea.

## Fontes
- [CNCF Paralus Official GitHub — Zero-Trust Kubernetes Access Manager](https://raw.githubusercontent.com/paralus/paralus/main/README.md) — documentação oficial do Paralus cobrindo RBAC multi-cluster, SSO/OIDC, JIT ServiceAccounts e pctl; consultado em 2026-10-03.
- [Paralus Official Documentation — Zero Trust & Architecture](https://www.paralus.io/docs/) — guia oficial de arquitetura, Relay Agent, Projects, Roles e operação do Paralus; consultado em 2026-10-03.
- [Paralus Documentation — Audit Logs](https://www.paralus.io/docs/usage/audit-logs) — documentação oficial de System Audit Logs e Kubectl/Relay Audit Logs; consultado em 2026-10-03.
