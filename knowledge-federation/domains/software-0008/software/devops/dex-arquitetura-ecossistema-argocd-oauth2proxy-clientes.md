---
id: software.devops.tranche11.001020
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

# Arquitetura de integração do Dex como bloco de construção para OAuth2 Proxy, Argo CD e plataformas internas

## Em uma frase
Conforme destaca a documentação oficial, o Dex é projetado como um bloco de construção (*building block*) para impulsionar a autenticação de outras ferramentas cloud-native — sendo amplamente emparelhado com o **OAuth2 Proxy**, o **Argo CD** e o **Kubernetes API Server** para unificar o Single Sign-On da plataforma.

## Por que importa
Em vez de configurar credenciais de cliente no GitHub, Google ou Active Directory separadamente para cada uma das 20 ferramentas internas do cluster (Prometheus, Alertmanager, Dashboards, Argo CD), a equipe de plataforma registra apenas o Dex no provedor corporativo upstream e conecta todas as ferramentas internas ao Dex via OIDC.

## Como funciona
No arquivo de configuração do Dex, cada ferramenta interna da plataforma é registrada em `staticClients` (ou via API gRPC do Dex) e pode compartilhar identidade por meio de `trustedPeers`. Por exemplo, o **OAuth2 Proxy** (atuando como middleware de Ingress Nginx/Envoy) aponta seu `--oidc-issuer-url` para o Dex para proteger dashboards que não possuem autenticação própria, enquanto o **Argo CD** (que inclusive embarca o Dex em sua instalação padrão) delega o login SSO e o mapeamento de grupos RBAC ao Dex.

## Exemplo
```yaml
# Definição de múltiplos clientes internos de plataforma (OAuth2 Proxy e Grafana) autenticando contra a mesma instância do Dex
staticClients:
  - id: oauth2-proxy
    redirectURIs:
      - https://auth-proxy.exemplo.com/oauth2/callback
    name: OAuth2 Proxy Ingress Gatekeeper
    secret: "${OAUTH2_PROXY_CLIENT_SECRET}"
  - id: grafana
    redirectURIs:
      - https://grafana.exemplo.com/login/generic_oauth
    name: Grafana Observability
    secret: "${GRAFANA_CLIENT_SECRET}"
```

## Limites e trade-offs
Como o Dex passa a ser a dependência central do caminho de login de todos os painéis operacionais e do `kubectl`, sua implantação em produção deve contar com múltiplas réplicas, storage persistente compartilhado (como CRDs do Kubernetes ou PostgreSQL) e monitoramento contínuo de disponibilidade.

## Como verificar
Verifique a conectividade entre os clientes internos e o Dex consultando `https://dex.exemplo.com/dex/.well-known/openid-configuration` a partir do namespace onde rodam o OAuth2 Proxy e o Grafana.

## Conexões
- [[dex-conector-ldap-active-directory-buscas-usuarios-grupos]] — Veja também: Conector LDAP no Dex: autenticação e resolução de grupos em diretórios OpenLDAP e Active Directory.
- [[dex-provedor-identidade-federado-openid-connect-cncf]] — Referência cruzada direta com dex-provedor-identidade-federado-openid-connect-cncf.
- [[oauth2proxy-proxy-reverso-middleware-autenticacao-oidc-oauth2]] — Referência cruzada direta com oauth2proxy-proxy-reverso-middleware-autenticacao-oidc-oauth2.

## Fontes
- [Dex GitHub — README.md (ID Tokens, Kubernetes Authentication & Connectors Matrix)](https://raw.githubusercontent.com/dexidp/dex/master/README.md) — README oficial do dexidp/dex detalhando ID Tokens JWT, integração OIDC com Kubernetes e AWS STS, matriz de suporte de conectores (stable/beta/alpha) e alerta de segurança do conector SAML 2.0; consultado em 2026-10-03.
- [Dex Official Documentation — Getting Started (Container Images, Gomplate, DEX_EXPAND_ENV & Example App)](https://dexidp.io/docs/getting-started/) — Guia oficial Getting Started do Dex documentando imagens alpine e distroless, chart Helm, pré-processamento gomplate, expansão de variáveis de ambiente e validação com example-app; consultado em 2026-10-03.
- [Dex — Official GitHub Repository](https://github.com/dexidp/dex) — Repositório oficial do Dex; consultado em 2026-10-03.
