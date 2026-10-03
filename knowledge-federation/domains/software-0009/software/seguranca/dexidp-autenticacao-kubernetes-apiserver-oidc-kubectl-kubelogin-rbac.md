---
id: software.seguranca.tranche03.000232
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

# Dex + Kubernetes API Server: autenticação OIDC para `kubectl` (`kubelogin`) com mapeamento de grupos para `ClusterRoleBinding`

## Em uma frase
Conforme destacado na seção *Kubernetes and Dex* do README oficial, um dos casos de uso primordiais do Dex é alimentar a autenticação de usuários humanos no **`kube-apiserver` do Kubernetes** através das flags nativas `--oidc-issuer-url`, `--oidc-client-id`, `--oidc-username-claim` e `--oidc-groups-claim=groups`.

## Por que importa
Como o Kubernetes não possui um banco de dados de usuários humanos embutido, compartilhar arquivos `kubeconfig` contendo certificados X.509 estáticos de `system:masters` que nunca podem ser revogados individualmente nem exigem login corporativo é um risco grave de segurança.

## Como funciona
Integrando o `kube-apiserver` ao Dex e utilizando o plugin de credenciais **`kubectl oidc-login` (`int128/kubelogin`)**, o engenheiro executa `kubectl get pods`, autentica-se no seu IdP corporativo via navegador, recebe um `id_token` + `refresh_token` assinado pelo Dex contendo seus grupos (`"groups": ["sre-prod", "devs"]`) e o Kubernetes aplica o RBAC (`RoleBinding` / `ClusterRoleBinding`) diretamente sobre esses grupos!

## Exemplo
```yaml
# Flags do kube-apiserver para confiar nos ID Tokens emitidos pelo Dex:
# --oidc-issuer-url=https://dex.internal.corp/dex
# --oidc-client-id=kubernetes-kubectl
# --oidc-username-claim=email
# --oidc-groups-claim=groups

# Vinculando um grupo retornado pelo Dex ao papel cluster-admin via ClusterRoleBinding:
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: dex-sre-admins
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
  - kind: Group
    name: "sre-prod"
    apiGroup: rbac.authorization.k8s.io
```

## Limites e trade-offs
Atenção à nota oficial em `dexidp.io/docs/connectors/`: clientes que dependem de acesso offline e renovação silenciosa de sessão — como o **`kubectl`** — exigem um conector que **suporte `refresh_tokens`** (como `ldap`, `oidc`, `github`, `gitlab`, `microsoft`).

## Como verificar
Inspecione as claims do JWT recebido pelo `kubelogin` para confirmar a presença do array `groups` e do `aud: "kubernetes-kubectl"`.

## Conexões
- [[dexidp-arquitetura-cncf-federated-openid-connect-provider-connectors]] — Veja também: CNCF Dex: arquitetura do provedor OpenID Connect federado (*Identity Broker*) baseado em `Connectors`.
- [[dexidp-conector-ldap-active-directory-usersearch-groupsearch-starttls]] — Veja também: Dex Conector `LDAP` (`ldap`): integração segura com Active Directory / OpenLDAP via `userSearch`, `groupSearch` e `startTLS` / `rootCA`.

## Fontes
- [CNCF Dex GitHub — README.md (Federated OpenID Connect Provider, ID Tokens, Kubernetes Authentication & Connectors Matrix)](https://raw.githubusercontent.com/dexidp/dex/master/README.md) — README oficial do dexidp/dex detalhando a emissão de ID Tokens JWT, integração com Kubernetes/AWS STS e matriz de estabilidade e recursos dos conectores; consultado em 2026-10-03.
- [CNCF Dex Official Documentation — Connectors Reference (Upstream IdP Protocol Translation, Refresh Token & Groups Support)](https://dexidp.io/docs/connectors/) — Documentação oficial de conectores do Dex cobrindo configuração de LDAP, GitHub, GitLab, OIDC e limitações de protocolo; consultado em 2026-10-03.
- [CNCF Dex — Official GitHub Repository](https://github.com/dexidp/dex) — Repositório oficial Apache-2.0 do CNCF Dex; consultado em 2026-10-03.
