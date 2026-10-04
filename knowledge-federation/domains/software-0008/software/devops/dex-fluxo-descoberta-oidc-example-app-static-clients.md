---
id: software.devops.tranche11.001018
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
fontes: ["https://dexidp.io/docs/getting-started/", "https://raw.githubusercontent.com/dexidp/dex/master/README.md", "https://github.com/dexidp/dex"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Teste local e descoberta OIDC no Dex: staticClients, enablePasswordDB e validação com example-app

## Em uma frase
O Dex inclui uma aplicação cliente de referência (`./bin/example-app`, compilada com `make examples`) e suporte a clientes estáticos (`staticClients`) e banco de senhas estático (`enablePasswordDB`) em `examples/config-dev.yaml` para validar localmente o fluxo completo de descoberta OIDC e emissão de tokens.

## Por que importa
Antes de conectar o Dex a um servidor Active Directory corporativo ou alterar flags do `kube-apiserver`, engenheiros de plataforma precisam testar localmente o mapeamento de escopos (`openid`, `profile`, `email`, `groups`, `offline_access`), a assinatura de JWTs e o redirecionamento de callback OAuth2.

## Como funciona
Conforme descreve a seção *Running a client* do guia *Getting Started* (`dexidp.io/docs/getting-started/`): (1) `./bin/dex serve examples/config-dev.yaml` inicia o Dex na porta `5556` com um datastore SQLite3 e credenciais OAuth2 pré-definidas; (2) `./bin/example-app` inicia um cliente OAuth2 de teste em `http://localhost:5555/` que consulta automaticamente o **discovery endpoint** do Dex (`/.well-known/openid-configuration`) para descobrir os endpoints de autorização, token e chaves públicas; e (3) ao clicar em login no navegador, o usuário pode autenticar-se com dados simulados (*Login with Example*) ou com as credenciais estáticas de demonstração (`admin@example.com` / `password`), aprovar os escopos solicitados e inspecionar o ID Token e o Refresh Token retornados.

## Exemplo
```bash
# Compilar o Dex e a aplicação cliente de exemplo para testar o fluxo OIDC ponta a ponta localmente
make build
make examples
./bin/dex serve examples/config-dev.yaml &
./bin/example-app --issuer http://127.0.0.1:5556/dex --listen http://127.0.0.1:5555
```

## Limites e trade-offs
A opção `enablePasswordDB: true` com `staticPasswords` no arquivo `config-dev.yaml` é útil para desenvolvimento, demonstrações e testes automatizados de CI, mas em produção as identidades devem vir de conectores corporativos auditáveis (como LDAP ou OIDC) em vez de hashes bcrypt estáticos no YAML.

## Como verificar
Acesse `http://localhost:5555/`, conclua o fluxo de login com `admin@example.com` e verifique na página de callback a presença do `ID Token` decodificado e do `Refresh Token`.

## Conexões
- [[dex-configuracao-gomplate-expansao-variaveis-ambiente]] — Veja também: Configuração do Dex: pré-processamento com gomplate no entrypoint do container e expansão nativa de variáveis ($VAR / DEX_EXPAND_ENV).
- [[dex-conector-ldap-active-directory-buscas-usuarios-grupos]] — Veja também: Conector LDAP no Dex: autenticação e resolução de grupos em diretórios OpenLDAP e Active Directory.
- [[dex-provedor-identidade-federado-openid-connect-cncf]] — Referência cruzada direta com dex-provedor-identidade-federado-openid-connect-cncf.
- [[dex-id-tokens-jwt-claims-padrao-consumidores-sts]] — Referência cruzada direta com dex-id-tokens-jwt-claims-padrao-consumidores-sts.

## Fontes
- [Dex GitHub — README.md (ID Tokens, Kubernetes Authentication & Connectors Matrix)](https://dexidp.io/docs/getting-started/) — README oficial do dexidp/dex detalhando ID Tokens JWT, integração OIDC com Kubernetes e AWS STS, matriz de suporte de conectores (stable/beta/alpha) e alerta de segurança do conector SAML 2.0; consultado em 2026-10-03.
- [Dex Official Documentation — Getting Started (Container Images, Gomplate, DEX_EXPAND_ENV & Example App)](https://raw.githubusercontent.com/dexidp/dex/master/README.md) — Guia oficial Getting Started do Dex documentando imagens alpine e distroless, chart Helm, pré-processamento gomplate, expansão de variáveis de ambiente e validação com example-app; consultado em 2026-10-03.
- [Dex — Official GitHub Repository](https://github.com/dexidp/dex) — Repositório oficial do Dex; consultado em 2026-10-03.
