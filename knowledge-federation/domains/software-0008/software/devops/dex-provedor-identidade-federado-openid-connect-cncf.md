---
id: software.devops.tranche11.001011
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

# Dex: provedor de identidade federado OpenID Connect (CNCF) baseado em conectores upstream

## Em uma frase
O Dex (`dexidp/dex`) é um serviço de identidade open-source da CNCF que utiliza **OpenID Connect (OIDC)** para fornecer autenticação padronizada a aplicações clientes, atuando como um portal (*shim*) que delega a verificação de credenciais a provedores upstream — como servidores LDAP, Active Directory, SAML, GitHub, GitLab, Google e Microsoft — por meio de **conectores**.

## Por que importa
Em engenharia de plataforma, ferramentas como o Kubernetes API Server, Argo CD, Grafana e OAuth2 Proxy entendem OpenID Connect, mas o diretório corporativo da empresa frequentemente é um servidor LDAP legado, Active Directory ou GitHub Organization que não expõe OIDC nativamente ou não emite as claims de grupos necessárias. Com o Dex, os clientes escrevem sua lógica de autenticação uma única vez falando OIDC com o Dex, e o Dex traduz os protocolos específicos de cada backend.

## Como funciona
Conforme documenta o README oficial (`dexidp/dex`), quando um usuário tenta autenticar-se em uma aplicação cliente (como `kubectl` via `kubelogin` ou uma aplicação web): (1) o cliente redireciona o navegador para o endpoint OAuth2/OIDC do Dex; (2) o Dex consulta seu conector configurado (ex.: realizando um bind e busca de usuário/grupos no LDAP ou autenticando via API do GitHub); e (3) após validar a identidade upstream, o Dex assina criptograficamente e retorna um **ID Token** (JSON Web Token — JWT) padronizado ao cliente, além de expor suas chaves públicas de verificação no endpoint `.well-known/openid-configuration` / JWKS.

## Exemplo
```bash
# Iniciar o servidor Dex localmente usando o arquivo de configuração de exemplo com datastore SQLite3
git clone https://github.com/dexidp/dex.git
cd dex && make build
./bin/dex serve examples/config-dev.yaml
```

## Limites e trade-offs
Diferentemente do Keycloak, o Dex não é um sistema completo de gerenciamento de ciclo de vida de usuários (ele não oferece telas para auto-cadastro de usuários, redefinição de senha nem edição de grupos próprios); ele é projetado especificamente como um intermediário federado leve que reflete identidades mantidas em um sistema upstream.

## Como verificar
Com o Dex em execução na porta `5556`, consulte `curl -s http://127.0.0.1:5556/dex/.well-known/openid-configuration | jq .` para inspecionar os endpoints `authorization_endpoint`, `token_endpoint` e `jwks_uri`.

## Conexões
- [[dex-id-tokens-jwt-claims-padrao-consumidores-sts]] — Veja também: ID Tokens no Dex: estrutura do JWT assinado, claims padrão (iss, sub, aud, email, groups) e consumo por Kubernetes e AWS STS.
- [[dex-conectores-upstream-ldap-github-oidc-matriz-suporte]] — Referência cruzada direta com dex-conectores-upstream-ldap-github-oidc-matriz-suporte.
- [[keycloak-gerenciamento-identidade-acesso-oidc-saml-cncf]] — Referência cruzada direta com keycloak-gerenciamento-identidade-acesso-oidc-saml-cncf.

## Fontes
- [Dex GitHub — README.md (ID Tokens, Kubernetes Authentication & Connectors Matrix)](https://raw.githubusercontent.com/dexidp/dex/master/README.md) — README oficial do dexidp/dex detalhando ID Tokens JWT, integração OIDC com Kubernetes e AWS STS, matriz de suporte de conectores (stable/beta/alpha) e alerta de segurança do conector SAML 2.0; consultado em 2026-10-03.
- [Dex Official Documentation — Getting Started (Container Images, Gomplate, DEX_EXPAND_ENV & Example App)](https://dexidp.io/docs/getting-started/) — Guia oficial Getting Started do Dex documentando imagens alpine e distroless, chart Helm, pré-processamento gomplate, expansão de variáveis de ambiente e validação com example-app; consultado em 2026-10-03.
- [Dex — Official GitHub Repository](https://github.com/dexidp/dex) — Repositório oficial do Dex; consultado em 2026-10-03.
