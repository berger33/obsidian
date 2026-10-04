---
id: software.devops.tranche11.001014
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/dexidp/dex/master/README.md", "https://dexidp.io/docs/getting-started/", "https://github.com/dexidp/dex"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Conectores do Dex: matriz de capacidades (refresh tokens, groups, preferred_username) e níveis de maturidade (stable, beta, alpha)

## Em uma frase
Os conectores do Dex abstraem protocolos heterogêneos de autenticação upstream (como LDAP, GitHub, GitLab, OpenID Connect, Microsoft, Google, Atlassian Crowd e Gitea), mas diferem no suporte a **refresh tokens**, **groups claim**, **preferred_username claim** e no nível de estabilidade (**stable**, **beta** ou **alpha**).

## Por que importa
Escolher um conector sem verificar sua matriz de capacidades no README oficial pode quebrar requisitos essenciais da plataforma — por exemplo, escolher um conector que não retorna a claim `groups` inviabiliza `ClusterRoleBindings` por equipe no Kubernetes, enquanto um conector sem suporte a refresh tokens força logins manuais repetitivos no `kubectl`.

## Como funciona
Conforme a tabela oficial de conectores do Dex: (1) **LDAP** e **GitHub** são classificados como `stable` e suportam simultaneamente *refresh tokens*, *groups claim* e *preferred_username claim*; (2) **GitLab**, **OpenID Connect** (incluindo Salesforce, Azure etc.) e **Atlassian Crowd** são `beta` e suportam as três capacidades (no Crowd, `preferred_username` exige configuração explícita); (3) **Microsoft** (`beta`), **Google** (`alpha`), **Bitbucket Cloud** (`alpha`), **OpenShift** (`alpha`) e **OpenStack Keystone** (`alpha`) suportam *refresh tokens* e *groups claim*, mas não `preferred_username`; e (4) **LinkedIn** (`beta`) e **Gitea** (`beta`) suportam *refresh tokens*, mas não retornam `groups claim`. O projeto define `stable` como bem testado e sem quebras incompatíveis, `beta` como testado e improvável de quebrar compatibilidade, e `alpha` como sujeito a mudanças incompatíveis.

## Exemplo
```yaml
# Exemplo de conector GitHub (stable) configurado no Dex para autenticar membros de uma organização e equipes
connectors:
  - type: github
    id: github
    name: GitHub Corp
    config:
      clientID: $GITHUB_CLIENT_ID
      clientSecret: $GITHUB_CLIENT_SECRET
      redirectURI: https://dex.exemplo.com/dex/callback
      orgs:
        - name: minha-organizacao
```

## Limites e trade-offs
O conector **OAuth 2.0** genérico (`alpha`) e o conector **AuthProxy** (`alpha`) não suportam *refresh tokens* (`supports refresh tokens: no`), sendo inadequados para fluxos que exigem o escopo `offline_access`.

## Como verificar
Verifique a seção `connectors:` do seu arquivo de configuração do Dex contra a tabela oficial do README e teste o login com `scopes: ["openid", "profile", "email", "groups", "offline_access"]` para confirmar quais claims retornam.

## Conexões
- [[dex-autenticacao-kubernetes-apiserver-kubelogin-crds]] — Veja também: Dex e Kubernetes: autenticação do API Server via plugin OIDC, armazenamento em CRDs e integração com kubelogin / kubectl.
- [[dex-limitacoes-protocolo-saml-aviso-seguranca-refresh-tokens]] — Veja também: Limitações de protocolo e alerta de segurança do conector SAML 2.0 no Dex.
- [[dex-provedor-identidade-federado-openid-connect-cncf]] — Referência cruzada direta com dex-provedor-identidade-federado-openid-connect-cncf.

## Fontes
- [Dex GitHub — README.md (ID Tokens, Kubernetes Authentication & Connectors Matrix)](https://raw.githubusercontent.com/dexidp/dex/master/README.md) — README oficial do dexidp/dex detalhando ID Tokens JWT, integração OIDC com Kubernetes e AWS STS, matriz de suporte de conectores (stable/beta/alpha) e alerta de segurança do conector SAML 2.0; consultado em 2026-10-03.
- [Dex Official Documentation — Getting Started (Container Images, Gomplate, DEX_EXPAND_ENV & Example App)](https://dexidp.io/docs/getting-started/) — Guia oficial Getting Started do Dex documentando imagens alpine e distroless, chart Helm, pré-processamento gomplate, expansão de variáveis de ambiente e validação com example-app; consultado em 2026-10-03.
- [Dex — Official GitHub Repository](https://github.com/dexidp/dex) — Repositório oficial do Dex; consultado em 2026-10-03.
