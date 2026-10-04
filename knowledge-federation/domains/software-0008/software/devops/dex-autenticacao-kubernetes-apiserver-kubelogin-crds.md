---
id: software.devops.tranche11.001013
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

# Dex e Kubernetes: autenticação do API Server via plugin OIDC, armazenamento em CRDs e integração com kubelogin / kubectl

## Em uma frase
O Dex roda nativamente sobre clusters Kubernetes utilizando **Custom Resource Definitions (CRDs)** como backend de armazenamento sem necessidade de banco externo e impulsiona a autenticação de usuários no `kube-apiserver` por meio do plugin OpenID Connect integrado a clientes como `kubectl` e `kubelogin`.

## Por que importa
Certificados X.509 de cliente no Kubernetes não possuem mecanismo nativo de revogação nem integração automática com grupos corporativos. Ao conectar o `kube-apiserver` ao Dex via OIDC, engenheiros fazem login no cluster com suas contas do LDAP/GitHub/Google e recebem permissões RBAC mapeadas diretamente a partir da claim `groups` do ID Token.

## Como funciona
Conforme descreve a seção *Kubernetes and Dex* do README oficial, o Dex pode armazenar todo o seu estado interno (chaves de assinatura rotacionadas, sessões de login, refresh tokens e clientes dinâmicos) diretamente em CRDs na API do Kubernetes. Do lado do cluster, o `kube-apiserver` é configurado com as flags `--oidc-issuer-url`, `--oidc-client-id`, `--oidc-username-claim=email` e `--oidc-groups-claim=groups` apontando para o Dex. Na estação do desenvolvedor, o plugin `kubelogin` (`kubectl oidc-login`) abre o navegador, executa o fluxo OIDC com o Dex, armazena o ID Token e o refresh token (quando o conector suporta `offline_access`) e injeta o Bearer Token nas chamadas do `kubectl`.

## Exemplo
```yaml
# Trecho de configuração do Dex usando CRDs do Kubernetes como storage nativo
issuer: https://dex.exemplo.com/dex
storage:
  type: kubernetes
  config:
    inCluster: true
web:
  https: 0.0.0.0:5556
  tlsCert: /etc/dex/tls/tls.crt
  tlsKey: /etc/dex/tls/tls.key
```

## Limites e trade-offs
Para que ferramentas de linha de comando como o `kubectl` / `kubelogin` renovem tokens silenciosamente sem exigir login interativo no navegador a cada expiração, o conector upstream configurado no Dex precisa suportar **refresh tokens** (`offline_access`) — algo suportado por conectores como LDAP, GitHub, GitLab e OIDC, mas não pelo conector SAML 2.0.

## Como verificar
Após autenticar via `kubectl oidc-login`, execute `kubectl auth whoami` para confirmar que o Kubernetes API Server reconheceu seu `Username` e a lista de `Groups` emitidos pelo Dex.

## Conexões
- [[dex-id-tokens-jwt-claims-padrao-consumidores-sts]] — Veja também: ID Tokens no Dex: estrutura do JWT assinado, claims padrão (iss, sub, aud, email, groups) e consumo por Kubernetes e AWS STS.
- [[dex-conectores-upstream-ldap-github-oidc-matriz-suporte]] — Veja também: Conectores do Dex: matriz de capacidades (refresh tokens, groups, preferred_username) e níveis de maturidade (stable, beta, alpha).
- [[dex-provedor-identidade-federado-openid-connect-cncf]] — Referência cruzada direta com dex-provedor-identidade-federado-openid-connect-cncf.

## Fontes
- [Dex GitHub — README.md (ID Tokens, Kubernetes Authentication & Connectors Matrix)](https://raw.githubusercontent.com/dexidp/dex/master/README.md) — README oficial do dexidp/dex detalhando ID Tokens JWT, integração OIDC com Kubernetes e AWS STS, matriz de suporte de conectores (stable/beta/alpha) e alerta de segurança do conector SAML 2.0; consultado em 2026-10-03.
- [Dex Official Documentation — Getting Started (Container Images, Gomplate, DEX_EXPAND_ENV & Example App)](https://dexidp.io/docs/getting-started/) — Guia oficial Getting Started do Dex documentando imagens alpine e distroless, chart Helm, pré-processamento gomplate, expansão de variáveis de ambiente e validação com example-app; consultado em 2026-10-03.
- [Dex — Official GitHub Repository](https://github.com/dexidp/dex) — Repositório oficial do Dex; consultado em 2026-10-03.
