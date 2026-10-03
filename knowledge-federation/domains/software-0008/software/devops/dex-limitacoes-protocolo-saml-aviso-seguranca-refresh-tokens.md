---
id: software.devops.tranche11.001015
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

# Limitações de protocolo e alerta de segurança do conector SAML 2.0 no Dex

## Em uma frase
No Dex, limitações inerentes ao protocolo upstream impedem o conector **SAML 2.0** de emitir *refresh tokens*, e a documentação oficial exibe um alerta explícito de que o conector SAML 2.0 encontra-se sem manutenção ativa e provavelmente vulnerável a contornos de autenticação (*auth bypasses*).

## Por que importa
Muitas organizações que possuem provedores de identidade corporativos legados cogitam conectar o Dex via SAML 2.0. Conhecer tanto a limitação estrutural de renovação não interativa do SAML quanto o alerta oficial de segurança da biblioteca XML/SAML evita expor o cluster a vulnerabilidades críticas de falsificação de asserções.

## Como funciona
Conforme explica o README oficial do Dex em dois pontos distintos: primeiro, como o protocolo SAML 2.0 não fornece um mecanismo não interativo para renovar asserções em background, quando um usuário faz login pelo conector SAML o Dex **não emite um refresh token** para o cliente (`supports refresh tokens: no`), o que inviabiliza clientes que dependem de acesso offline como o `kubectl`. Segundo, na tabela oficial de conectores, a linha do SAML 2.0 traz a nota explícita: **`WARNING: Unmaintained and likely vulnerable to auth bypasses`**, recomendando evitar seu uso em favor de conectores mantidos como OpenID Connect ou LDAP.

## Exemplo
```yaml
# Recomendação arquitetural: quando o IdP corporativo suportar ambos, prefira sempre o conector OIDC em vez de SAML no Dex
connectors:
  - type: oidc
    id: idp-corporativo
    name: IdP Corporativo OIDC
    config:
      issuer: https://idp.exemplo.com/oauth2/default
      clientID: $OIDC_CLIENT_ID
      clientSecret: $OIDC_CLIENT_SECRET
      redirectURI: https://dex.exemplo.com/dex/callback
      getUserInfo: true
```

## Limites e trade-offs
Caso um sistema legado suporte exclusivamente SAML 2.0 e não possa expor OIDC ou LDAP diretamente ao Dex, utilize um broker intermediário com suporte SAML ativamente mantido (como o Keycloak) que exponha um endpoint OpenID Connect padrão para o Dex ou diretamente para os clientes.

## Como verificar
Audite os arquivos `config.yaml` de todas as instâncias do Dex na sua infraestrutura com `grep -n "type: saml" config.yaml` para garantir que nenhum ambiente produtivo dependa do conector SAML descontinuado.

## Conexões
- [[dex-conectores-upstream-ldap-github-oidc-matriz-suporte]] — Veja também: Conectores do Dex: matriz de capacidades (refresh tokens, groups, preferred_username) e níveis de maturidade (stable, beta, alpha).
- [[dex-distribuicao-imagens-alpine-distroless-helm-build]] — Veja também: Distribuição e implantação do Dex: imagens oficiais Alpine e Distroless, Helm chart e compilação com Go.
- [[keycloak-gerenciamento-identidade-acesso-oidc-saml-cncf]] — Referência cruzada direta com keycloak-gerenciamento-identidade-acesso-oidc-saml-cncf.
- [[dex-provedor-identidade-federado-openid-connect-cncf]] — Referência cruzada direta com dex-provedor-identidade-federado-openid-connect-cncf.

## Fontes
- [Dex GitHub — README.md (ID Tokens, Kubernetes Authentication & Connectors Matrix)](https://raw.githubusercontent.com/dexidp/dex/master/README.md) — README oficial do dexidp/dex detalhando ID Tokens JWT, integração OIDC com Kubernetes e AWS STS, matriz de suporte de conectores (stable/beta/alpha) e alerta de segurança do conector SAML 2.0; consultado em 2026-10-03.
- [Dex Official Documentation — Getting Started (Container Images, Gomplate, DEX_EXPAND_ENV & Example App)](https://dexidp.io/docs/getting-started/) — Guia oficial Getting Started do Dex documentando imagens alpine e distroless, chart Helm, pré-processamento gomplate, expansão de variáveis de ambiente e validação com example-app; consultado em 2026-10-03.
- [Dex — Official GitHub Repository](https://github.com/dexidp/dex) — Repositório oficial do Dex; consultado em 2026-10-03.
