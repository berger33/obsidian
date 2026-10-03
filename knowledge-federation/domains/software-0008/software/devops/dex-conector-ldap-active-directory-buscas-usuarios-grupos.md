---
id: software.devops.tranche11.001019
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

# Conector LDAP no Dex: autenticação e resolução de grupos em diretórios OpenLDAP e Active Directory

## Em uma frase
O conector **LDAP** do Dex (classificado como `stable`) autentica usuários realizando bind contra diretórios OpenLDAP ou Microsoft Active Directory e executa buscas configuráveis (`userSearch` e `groupSearch`) para popular as claims `email`, `preferred_username` e `groups` no ID Token.

## Por que importa
Muitas empresas mantêm toda a hierarquia de permissões de engenharia em grupos LDAP/Active Directory (`cn=k8s-admins,ou=Groups,dc=exemplo,dc=com`), mas aplicações cloud-native exigem tokens JWT OpenID Connect. O conector LDAP do Dex faz essa ponte mantendo suporte completo a *refresh tokens*, `groups` e `preferred_username`.

## Como funciona
Conforme documentado no README e no guia de conectores LDAP do Dex, o conector conecta-se ao servidor LDAP (usando TLS ou `startTLS` com `rootCA`), utiliza uma conta de serviço (`bindDN` e `bindPW`) para localizar o Distinguished Name (DN) do usuário com base no filtro configurado em `userSearch` (ex.: `attr: mail` ou `sAMAccountName`), valida a senha do usuário realizando um bind com o DN encontrado e, em seguida, executa `groupSearch` para descobrir todos os grupos aos quais o usuário pertence, injetando os nomes dos grupos na claim `groups` do JWT emitido.

## Exemplo
```yaml
# Exemplo de configuração do conector LDAP (stable) no Dex com busca de usuários e grupos
connectors:
  - type: ldap
    name: OpenLDAP Corporativo
    id: ldap
    config:
      host: ldap.exemplo.com:636
      rootCA: /etc/dex/ldap-ca.crt
      bindDN: cn=dex-readonly,dc=exemplo,dc=com
      bindPW: "${LDAP_BIND_PASSWORD}"
      userSearch:
        baseDN: ou=People,dc=exemplo,dc=com
        filter: "(objectClass=person)"
        username: mail
        idAttr: DN
        emailAttr: mail
        nameAttr: cn
      groupSearch:
        baseDN: ou=Groups,dc=exemplo,dc=com
        filter: "(objectClass=groupOfNames)"
        userMatchers:
          - userAttr: DN
            groupAttr: member
        nameAttr: cn
```

## Limites e trade-offs
Se o atributo configurado em `userMatchers` não corresponder exatamente ao formato armazenado nos objetos de grupo do diretório (por exemplo, usar `uid` quando o grupo armazena o `DN` completo no atributo `member`), o login do usuário funcionará, mas a claim `groups` retornará vazia no ID Token.

## Como verificar
Realize um login solicitando o escopo `groups` no Dex e inspecione os logs do servidor Dex (que informam a query LDAP executada e a lista de grupos encontrados para o usuário).

## Conexões
- [[dex-fluxo-descoberta-oidc-example-app-static-clients]] — Veja também: Teste local e descoberta OIDC no Dex: staticClients, enablePasswordDB e validação com example-app.
- [[dex-arquitetura-ecossistema-argocd-oauth2proxy-clientes]] — Veja também: Arquitetura de integração do Dex como bloco de construção para OAuth2 Proxy, Argo CD e plataformas internas.
- [[dex-conectores-upstream-ldap-github-oidc-matriz-suporte]] — Referência cruzada direta com dex-conectores-upstream-ldap-github-oidc-matriz-suporte.
- [[dex-id-tokens-jwt-claims-padrao-consumidores-sts]] — Referência cruzada direta com dex-id-tokens-jwt-claims-padrao-consumidores-sts.
- [[dex-autenticacao-kubernetes-apiserver-kubelogin-crds]] — Referência cruzada direta com dex-autenticacao-kubernetes-apiserver-kubelogin-crds.

## Fontes
- [Dex GitHub — README.md (ID Tokens, Kubernetes Authentication & Connectors Matrix)](https://raw.githubusercontent.com/dexidp/dex/master/README.md) — README oficial do dexidp/dex detalhando ID Tokens JWT, integração OIDC com Kubernetes e AWS STS, matriz de suporte de conectores (stable/beta/alpha) e alerta de segurança do conector SAML 2.0; consultado em 2026-10-03.
- [Dex Official Documentation — Getting Started (Container Images, Gomplate, DEX_EXPAND_ENV & Example App)](https://dexidp.io/docs/getting-started/) — Guia oficial Getting Started do Dex documentando imagens alpine e distroless, chart Helm, pré-processamento gomplate, expansão de variáveis de ambiente e validação com example-app; consultado em 2026-10-03.
- [Dex — Official GitHub Repository](https://github.com/dexidp/dex) — Repositório oficial do Dex; consultado em 2026-10-03.
