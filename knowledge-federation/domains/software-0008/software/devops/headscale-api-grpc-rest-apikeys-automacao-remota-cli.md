---
id: software.devops.tranche19.001868
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://raw.githubusercontent.com/juanfont/headscale/main/README.md", "https://headscale.net/stable/about/features/", "https://github.com/juanfont/headscale"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Headscale API (gRPC/REST) e `apikeys`: administração remota segura e integração com automação externa

## Em uma frase
Todo o controle do Headscale é exposto por uma API **gRPC** e um gateway **REST/HTTP** autenticado por chaves de API gerenciadas via **`headscale apikeys`** (`create`, `list`, `expire`, `delete`), permitindo operar a CLI `headscale` remotamente ou integrar provedores Terraform e painéis web.

## Por que importa
Em servidores de produção onde o acesso SSH direto ao host do Headscale é restrito, sistemas de provisionamento e pipelines de CI precisam criar `preauthkeys`, aprovar rotas ou atualizar políticas via API HTTPS autenticada.

## Como funciona
O administrador gera uma chave de API no servidor com `headscale apikeys create --expiration 90d`. A partir de qualquer máquina remota, a própria CLI `headscale` pode controlar o servidor definindo as variáveis `HEADSCALE_CLI_ADDRESS` e `HEADSCALE_CLI_API_KEY` (ou chamadas HTTP com `Authorization: Bearer <api-key>` em `/api/v1/...`).

## Exemplo
```bash
# No servidor Headscale:
headscale apikeys create --expiration 90d
headscale apikeys list

# De uma máquina remota via REST API:
curl -sS -H "Authorization: Bearer ${HS_API_KEY}" \
  https://headscale.corp.example.com/api/v1/node
```

## Limites e trade-offs
O Headscale armazena apenas o hash bcrypt do segredo da API key no banco de dados; se a chave for perdida, expire-a pelo seu prefixo com `headscale apikeys expire --prefix <prefix>` e crie uma nova.

## Como verificar
Execute `headscale apikeys list` para auditar todas as chaves de API emitidas, seus prefixos e datas de expiração.

## Conexões
- [[headscale-autenticacao-oidc-single-sign-on-keycloak-dex-authelia]] — Veja também: Headscale com OpenID Connect (OIDC): registro de nós via Single Sign-On com Keycloak, Dex, Authelia ou Okta.
- [[headscale-armazenamento-sqlite-wal-postgresql-requisitos-producao]] — Veja também: Headscale Persistência e Operação: banco de dados SQLite (WAL) vs PostgreSQL e recomendações de deploy.

## Fontes
- [Headscale GitHub — README.md (Open Source Self-Hosted Tailscale Control Server, Design Goal & Single Tailnet Architecture)](https://raw.githubusercontent.com/juanfont/headscale/main/README.md) — README oficial do juanfont/headscale explicando o papel do servidor de controle na troca de chaves públicas WireGuard, atribuição de IPs e escopo de tailnet única; consultado em 2026-10-03.
- [Headscale Official Documentation — Features (Node Registration, MagicDNS, Extra DNS Records, Subnet Routers, Embedded DERP, ACLs/Grants & OIDC)](https://headscale.net/stable/about/features/) — Matriz oficial de funcionalidades do Headscale cobrindo registro web/preauthkey/OIDC, extra_records, autoApprovers, Tailscale SSH e DERP embutido; consultado em 2026-10-03.
- [Headscale — Official GitHub Repository](https://github.com/juanfont/headscale) — Repositório oficial BSD-3-Clause do Headscale; consultado em 2026-10-03.
