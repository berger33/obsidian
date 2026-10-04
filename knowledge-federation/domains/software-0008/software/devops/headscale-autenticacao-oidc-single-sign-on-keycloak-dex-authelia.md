---
id: software.devops.tranche19.001867
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
fontes: ["https://headscale.net/stable/about/features/", "https://raw.githubusercontent.com/juanfont/headscale/main/README.md", "https://github.com/juanfont/headscale"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Headscale com OpenID Connect (OIDC): registro de nós via Single Sign-On com Keycloak, Dex, Authelia ou Okta

## Em uma frase
A seção `oidc:` do `config.yaml` do Headscale permite integrar um provedor de identidade **OpenID Connect (OIDC)** (como Keycloak, Authentik, Authelia, Dex, Google Workspace ou Entra ID) para que usuários registrem seus dispositivos com Single Sign-On corporativo e tenham seus perfis atualizados a partir do IdP.

## Por que importa
Aprovar chaves de máquina manualmente para cada colaborador de uma equipe de engenharia não escala e impede exigir autenticação multifator (MFA/WebAuthn) no momento do ingresso na rede.

## Como funciona
Quando `oidc.issuer`, `oidc.client_id` e `oidc.client_secret` estão configurados (junto com filtros opcionais como `allowed_domains` ou `allowed_users`), ao rodar `tailscale up --login-server https://...`, a URL exibida redireciona o usuário para o fluxo de login OIDC com PKCE e registra o nó automaticamente no usuário correspondente após o callback.

## Exemplo
```yaml
oidc:
  only_start_if_oidc_is_available: true
  issuer: "https://sso.corp.internal/realms/engineering"
  client_id: "headscale-vpn"
  client_secret_path: "/var/lib/headscale/oidc_client_secret"
  pkce:
    enabled: true
  allowed_domains:
    - "corp.internal"
```

## Limites e trade-offs
Utilize `client_secret_path` apontando para um arquivo com permissão `0400` em vez de gravar o segredo OIDC diretamente em texto claro em `client_secret` dentro do `config.yaml`.

## Como verificar
Inicie o Headscale e verifique nos logs de inicialização que o endpoint `.well-known/openid-configuration` do `issuer` foi validado com sucesso.

## Conexões
- [[headscale-embedded-derp-server-stun-custom-derpmap-airgapped]] — Veja também: Headscale Embedded DERP Server: operação 100% *air-gapped* com servidor relay DERP e STUN embutido.
- [[headscale-api-grpc-rest-apikeys-automacao-remota-cli]] — Veja também: Headscale API (gRPC/REST) e `apikeys`: administração remota segura e integração com automação externa.

## Fontes
- [Headscale GitHub — README.md (Open Source Self-Hosted Tailscale Control Server, Design Goal & Single Tailnet Architecture)](https://headscale.net/stable/about/features/) — README oficial do juanfont/headscale explicando o papel do servidor de controle na troca de chaves públicas WireGuard, atribuição de IPs e escopo de tailnet única; consultado em 2026-10-03.
- [Headscale Official Documentation — Features (Node Registration, MagicDNS, Extra DNS Records, Subnet Routers, Embedded DERP, ACLs/Grants & OIDC)](https://raw.githubusercontent.com/juanfont/headscale/main/README.md) — Matriz oficial de funcionalidades do Headscale cobrindo registro web/preauthkey/OIDC, extra_records, autoApprovers, Tailscale SSH e DERP embutido; consultado em 2026-10-03.
- [Headscale — Official GitHub Repository](https://github.com/juanfont/headscale) — Repositório oficial BSD-3-Clause do Headscale; consultado em 2026-10-03.
