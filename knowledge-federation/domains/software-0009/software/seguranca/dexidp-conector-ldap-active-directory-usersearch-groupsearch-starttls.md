---
id: software.seguranca.tranche03.000233
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
fontes: ["https://dexidp.io/docs/connectors/", "https://raw.githubusercontent.com/dexidp/dex/master/README.md", "https://github.com/dexidp/dex"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Dex Conector `LDAP` (`ldap`): integração segura com Active Directory / OpenLDAP via `userSearch`, `groupSearch` e `startTLS` / `rootCA`

## Em uma frase
Na matriz oficial de conectores (`dexidp.io/docs/connectors/`), o conector **`ldap`** possui status **`stable`** e suporte completo a `refresh tokens`, `groups claim` e `preferred_username claim`, permitindo expor diretórios **OpenLDAP**, **FreeIPA** e **Microsoft Active Directory** como um provedor OpenID Connect moderno.

## Por que importa
Muitos sistemas empresariais legados ou diretórios internos falam apenas LDAPv3, enquanto plataformas modernas como Argo CD ou Kubernetes suportam apenas OIDC; o conector `ldap` do Dex faz essa ponte realizando a busca do usuário (`userSearch`), validando o bind da senha e buscando os grupos (`groupSearch`) em uma única transação.

## Como funciona
No bloco `connectors:` do Dex, configure sempre **`insecureNoSSL: false`** (com `startTLS: true` na porta `389` ou LDAPS na porta `636`) e forneça o certificado da autoridade certificadora interna em **`rootCA`** (ou `rootCAData`), garantindo que as senhas dos usuários nunca trafeguem em texto claro até o servidor LDAP.

## Exemplo
```yaml
connectors:
  - type: ldap
    name: Active Directory Corporativo
    id: ad-corp
    config:
      host: ldap.internal.corp:636
      insecureNoSSL: false
      rootCA: /etc/dex/certs/corp-ca.pem
      bindDN: cn=dex-svc,ou=svc,dc=internal,dc=corp
      bindPW: $DEX_LDAP_BIND_PASSWORD
      userSearch:
        baseDN: ou=Users,dc=internal,dc=corp
        filter: "(objectClass=person)"
        username: sAMAccountName
        idAttr: DN
        emailAttr: mail
        nameAttr: displayName
      groupSearch:
        baseDN: ou=Groups,dc=internal,dc=corp
        filter: "(objectClass=group)"
        userMatchers:
          - userAttr: DN
            groupAttr: member
        nameAttr: cn
```

## Limites e trade-offs
Referencie a senha da conta de serviço LDAP usando variável de ambiente (`$DEX_LDAP_BIND_PASSWORD`) injetada via Kubernetes Secret, nunca comitando a senha em texto plano no ConfigMap do Dex.

## Como verificar
Faça um login de teste selecionando o conector LDAP e inspecione o `id_token` emitido para confirmar o preenchimento de `email` e `groups`.

## Conexões
- [[dexidp-autenticacao-kubernetes-apiserver-oidc-kubectl-kubelogin-rbac]] — Veja também: Dex + Kubernetes API Server: autenticação OIDC para `kubectl` (`kubelogin`) com mapeamento de grupos para `ClusterRoleBinding`.
- [[dexidp-conectores-github-gitlab-orgs-teams-groups-filtragem]] — Veja também: Dex Conectores `GitHub` e `GitLab`: controle de acesso baseado em Organizações, Teams (`org:team`) e Grupos de engenharia.

## Fontes
- [CNCF Dex GitHub — README.md (Federated OpenID Connect Provider, ID Tokens, Kubernetes Authentication & Connectors Matrix)](https://dexidp.io/docs/connectors/) — README oficial do dexidp/dex detalhando a emissão de ID Tokens JWT, integração com Kubernetes/AWS STS e matriz de estabilidade e recursos dos conectores; consultado em 2026-10-03.
- [CNCF Dex Official Documentation — Connectors Reference (Upstream IdP Protocol Translation, Refresh Token & Groups Support)](https://raw.githubusercontent.com/dexidp/dex/master/README.md) — Documentação oficial de conectores do Dex cobrindo configuração de LDAP, GitHub, GitLab, OIDC e limitações de protocolo; consultado em 2026-10-03.
- [CNCF Dex — Official GitHub Repository](https://github.com/dexidp/dex) — Repositório oficial Apache-2.0 do CNCF Dex; consultado em 2026-10-03.
