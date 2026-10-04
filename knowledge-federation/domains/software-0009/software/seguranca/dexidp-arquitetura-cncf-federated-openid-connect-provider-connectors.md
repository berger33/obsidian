---
id: software.seguranca.tranche03.000231
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/dexidp/dex/master/README.md", "https://dexidp.io/docs/connectors/", "https://github.com/dexidp/dex"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CNCF Dex: arquitetura do provedor OpenID Connect federado (*Identity Broker*) baseado em `Connectors`

## Em uma frase
Conforme documentado no README oficial (`dexidp/dex`, projeto Sandbox da CNCF escrito em Go sob licença Apache 2.0) e em `dexidp.io/docs/connectors/`, o **Dex** é um serviço de identidade federado que utiliza **OpenID Connect (OIDC)** para prover autenticação padronizada a aplicações clientes, atuando como um *shim / broker* para provedores de identidade upstream através de **Connectors**.

## Por que importa
Em ecossistemas cloud-native (como Kubernetes API Server, Argo CD, Grafana, Kubeflow, Harbor e Gangway), cada ferramenta espera autenticar usuários via OpenID Connect moderno, mas muitas empresas armazenam suas identidades em diretórios **LDAP / Active Directory**, **GitHub Organizations**, **GitLab**, **Google Workspace** ou múltiplos provedores distintos.

## Como funciona
Com o Dex, todas as suas aplicações clientes implementam **apenas um protocolo (OpenID Connect falando com o Dex)**, enquanto o Dex traduz e delega a autenticação para qualquer conector configurado (`ldap`, `oidc`, `github`, `gitlab`, `microsoft`, `google`, `atlassian-crowd`, `openshift`), emitindo `id_token` JWT assinados com as claims padronizadas (`sub`, `email`, `email_verified`, `groups`, `name`)!

## Exemplo
```yaml
# Trecho central do config.yaml do Dex definindo o issuer OIDC e o armazenamento em CRDs do Kubernetes:
issuer: https://dex.internal.corp/dex
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
Como destaca o README oficial, o Dex pode rodar de forma 100% nativa sobre qualquer cluster Kubernetes usando **Custom Resource Definitions (`storage.type: kubernetes`)**, sem exigir a manutenção de um banco de dados SQL externo!

## Como verificar
Consulte `curl -sS https://dex.internal.corp/dex/.well-known/openid-configuration | jq .` para validar os endpoints OIDC expostos pelo Dex.

## Conexões
- [[dexidp-autenticacao-kubernetes-apiserver-oidc-kubectl-kubelogin-rbac]] — Veja também: Dex + Kubernetes API Server: autenticação OIDC para `kubectl` (`kubelogin`) com mapeamento de grupos para `ClusterRoleBinding`.

## Fontes
- [CNCF Dex GitHub — README.md (Federated OpenID Connect Provider, ID Tokens, Kubernetes Authentication & Connectors Matrix)](https://raw.githubusercontent.com/dexidp/dex/master/README.md) — README oficial do dexidp/dex detalhando a emissão de ID Tokens JWT, integração com Kubernetes/AWS STS e matriz de estabilidade e recursos dos conectores; consultado em 2026-10-03.
- [CNCF Dex Official Documentation — Connectors Reference (Upstream IdP Protocol Translation, Refresh Token & Groups Support)](https://dexidp.io/docs/connectors/) — Documentação oficial de conectores do Dex cobrindo configuração de LDAP, GitHub, GitLab, OIDC e limitações de protocolo; consultado em 2026-10-03.
- [CNCF Dex — Official GitHub Repository](https://github.com/dexidp/dex) — Repositório oficial Apache-2.0 do CNCF Dex; consultado em 2026-10-03.
