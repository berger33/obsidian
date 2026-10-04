---
id: software.devops.tranche11.001017
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

# Configuração do Dex: pré-processamento com gomplate no entrypoint do container e expansão nativa de variáveis ($VAR / DEX_EXPAND_ENV)

## Em uma frase
O Dex lê suas opções exclusivamente de um arquivo de configuração YAML (`dex serve config.yaml`), suportando tanto o pré-processamento de templates via **gomplate** no entrypoint padrão das imagens de container quanto a expansão nativa de variáveis de ambiente (`$VAR` e `${VAR}`) controlada por `DEX_EXPAND_ENV`.

## Por que importa
Arquivos de configuração do Dex contêm segredos sensíveis — como `clientSecret` de clientes OAuth2, senhas de bind LDAP (`bindPW`) e credenciais de provedores upstream. Injetar esses valores a partir de variáveis de ambiente originadas de Kubernetes Secrets permite versionar o template `config.yaml` em Git sem expor credenciais.

## Como funciona
Conforme documentado na seção *Configuration / Templated configuration* do guia oficial (`dexidp.io/docs/getting-started/`), existem dois mecanismos complementares: (1) **Gomplate no entrypoint do container**: o entrypoint padrão das imagens distribuídas utiliza o `gomplate` para pré-processar arquivos `.tpl`, `.tmpl` ou `.yaml` passados como argumento, permitindo sintaxe como `secret: "{{ .Env.MY_SECRET_ENV }}"`. Contudo, se o Deployment sobrescrever o `command` do container para invocar o binário `dex` diretamente (ex.: `dex serve /etc/dex/config.yaml`), o entrypoint é ignorado e os templates gomplate não são renderizados; e (2) **Expansão nativa de ambiente**: o próprio binário do Dex expande referências `$VAR` e `${VAR}` nos valores YAML antes de fazer o parse da configuração (comportamento que pode ser desativado definindo `DEX_EXPAND_ENV=false`).

## Exemplo
```yaml
# Exemplo de uso de expansão nativa de variáveis de ambiente ($VAR / ${VAR}) e sintaxe gomplate no config do Dex
issuer: https://dex.exemplo.com/dex
storage:
  type: sqlite3
  config:
    file: /var/dex/dex.db
staticClients:
  - id: argo-cd
    redirectURIs:
      - https://argocd.exemplo.com/auth/callback
    name: Argo CD
    secret: "${ARGOCD_DEX_CLIENT_SECRET}"
```

## Limites e trade-offs
Se uma senha de bind LDAP ou segredo contiver o caractere literal `$` e a expansão nativa estiver ativa (padrão), o Dex tentará interpretá-lo como nome de variável de ambiente; nesses casos, escape adequadamente ou defina `DEX_EXPAND_ENV=false` caso utilize apenas renderização controlada via gomplate ou montagem direta do arquivo.

## Como verificar
Inicie o container do Dex passando variáveis de ambiente de teste e valide nos logs de inicialização que os clientes e conectores foram carregados sem erros de parse YAML.

## Conexões
- [[dex-distribuicao-imagens-alpine-distroless-helm-build]] — Veja também: Distribuição e implantação do Dex: imagens oficiais Alpine e Distroless, Helm chart e compilação com Go.
- [[dex-fluxo-descoberta-oidc-example-app-static-clients]] — Veja também: Teste local e descoberta OIDC no Dex: staticClients, enablePasswordDB e validação com example-app.
- [[dex-provedor-identidade-federado-openid-connect-cncf]] — Referência cruzada direta com dex-provedor-identidade-federado-openid-connect-cncf.
- [[externalsecrets-operador-kubernetes-sincronizacao-segredos-externos]] — Referência cruzada direta com externalsecrets-operador-kubernetes-sincronizacao-segredos-externos.

## Fontes
- [Dex GitHub — README.md (ID Tokens, Kubernetes Authentication & Connectors Matrix)](https://dexidp.io/docs/getting-started/) — README oficial do dexidp/dex detalhando ID Tokens JWT, integração OIDC com Kubernetes e AWS STS, matriz de suporte de conectores (stable/beta/alpha) e alerta de segurança do conector SAML 2.0; consultado em 2026-10-03.
- [Dex Official Documentation — Getting Started (Container Images, Gomplate, DEX_EXPAND_ENV & Example App)](https://raw.githubusercontent.com/dexidp/dex/master/README.md) — Guia oficial Getting Started do Dex documentando imagens alpine e distroless, chart Helm, pré-processamento gomplate, expansão de variáveis de ambiente e validação com example-app; consultado em 2026-10-03.
- [Dex — Official GitHub Repository](https://github.com/dexidp/dex) — Repositório oficial do Dex; consultado em 2026-10-03.
