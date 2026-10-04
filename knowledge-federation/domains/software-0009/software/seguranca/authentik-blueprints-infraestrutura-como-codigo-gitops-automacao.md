---
id: software.seguranca.tranche14.001306
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/goauthentik/authentik/main/README.md", "https://docs.goauthentik.io/docs/core/architecture"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Identidade como Código (**Identity-as-Code**) no authentik com **Blueprints YAML**: Versionando Fluxos, Políticas, Provedores e RBAC via GitOps

## Em uma frase
Configurar fluxos de autenticação, políticas de MFA, escopos OIDC e aplicações clicando manualmente em dezenas de telas na interface web torna impossível reproduzir o ambiente de homologação em produção, auditar mudanças via *Pull Request* ou recuperar a configuração de identidade em caso de desastre.

## Por que importa
Para trazer a disciplina de **Infraestrutura como Código (IaC) e GitOps** para o gerenciamento de identidades, o authentik criou o sistema declarativo de **Blueprints (`.yaml`)**!

## Como funciona
Um **Blueprint** é um documento YAML idempotente que pode declarar e reconciliar **qualquer modelo de banco de dados do authentik** (`authentik_flows.flow`, `authentik_providers_oauth2.oauth2provider`, `authentik_core.application`, `authentik_policies_expression.expressionpolicy`, `authentik_rbac.role`). Usando tags especiais do motor YAML do authentik — como **`!KeyOf`** (referencia o ID primário de outra entrada declarada no mesmo Blueprint), **`!Find`** (busca um objeto já existente no banco pelo nome/slug), **`!Env`** (lê variáveis de ambiente/Secrets do Kubernetes!) e **`!Condition`** — o Worker reconcilia continuamente os arquivos `.yaml` montados no container com o estado real no PostgreSQL!

## Exemplo
```yaml
# Exemplo de Blueprint YAML do authentik criando uma Application e vinculando-a a um Provider OIDC usando !KeyOf e !Env
version: 1
metadata:
  name: Provisionamento GitOps - Portal Grafana
entries:
  - model: authentik_core.application
    id: app-grafana
    identifiers:
      slug: grafana
    attrs:
      name: Grafana Observability
      meta_launch_url: !Env [GRAFANA_URL, "https://grafana.exemplo.br"]
```

## Limites e trade-offs
Você pode exportar recursos existentes da sua instância do authentik ou validar a sintaxe e aplicação de um Blueprint pela CLI dentro do container executando **`ak apply_blueprint /blueprints/custom/meu-app.yaml`**!

## Como verificar
Armazene seus Blueprints customizados em um repositório Git privado, monte-os via `ConfigMap` / `Secret` no Helm Chart do authentik e nunca coloque `client_secret` em texto claro no YAML (use sempre a tag **`!Env [NOME_DA_VARIAVEL_SECRET]`**)!

## Conexões
- [[authentik-outposts-proxy-forwardauth-ldap-radius-arquitetura-distribuida]] — Veja também: Arquitetura de **Outposts** no authentik: Protegendo Aplicações Sem SSO via **Proxy / ForwardAuth (Traefik, Nginx, Envoy)** e Gateways **LDAP / RADIUS**.
- [[authentik-autenticacao-webauthn-passkeys-totp-duo-mfa-obrigatorio]] — Veja também: Autenticação Resistente a Phishing no authentik: **WebAuthn / Passkeys (FIDO2)**, Restrição de **MDS Attestation (`AAUID`)**, TOTP e Códigos de Recuperação.
- [[authentik-arquitetura-idp-core-embedded-outpost-worker-postgresql]] — Referência cruzada direta com authentik-arquitetura-idp-core-embedded-outpost-worker-postgresql.
- [[authentik-motor-flows-stages-bindings-autenticacao-contextual]] — Referência cruzada direta com authentik-motor-flows-stages-bindings-autenticacao-contextual.
- [[kanidm-operacao-cli-kanidmd-certificados-backups-migracoes-json]] — Referência cruzada direta com kanidm-operacao-cli-kanidmd-certificados-backups-migracoes-json.

## Fontes
- [authentik Official GitHub Repository (`goauthentik/authentik`)](https://raw.githubusercontent.com/goauthentik/authentik/main/README.md) — repositório oficial do provedor de identidade open-source authentik cobrindo OAuth2/OIDC, SAML, LDAP, RADIUS, SCIM e Flows; consultado em 2026-10-03.
- [authentik Official Architecture Documentation (`docs.goauthentik.io/docs/core/architecture`)](https://docs.goauthentik.io/docs/core/architecture) — documentação arquitetural oficial do authentik detalhando Server (Go Router + Python/Django API), Workers, PostgreSQL, Outposts e Blueprints declarativos; consultado em 2026-10-03.
