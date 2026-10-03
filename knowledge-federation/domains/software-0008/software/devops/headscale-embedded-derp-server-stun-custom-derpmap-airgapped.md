---
id: software.devops.tranche19.001866
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

# Headscale Embedded DERP Server: operação 100% *air-gapped* com servidor relay DERP e STUN embutido

## Em uma frase
O Headscale inclui um **servidor DERP e STUN embutido** (`derp.server.enabled: true` no `config.yaml`), além de permitir customizar o **DERP Map** (`derp.urls` e `derp.paths`) para substituir ou complementar a rede global de relays públicos da Tailscale.

## Por que importa
Em ambientes *air-gapped* sem saída para a internet ou em data centers onde políticas de conformidade proíbem que pacotes criptografados transitem por servidores relay externos quando o NAT traversal direto falha, é obrigatório operar relays DERP próprios.

## Como funciona
Ao habilitar `derp.server.enabled: true` com `stun_listen_addr: "0.0.0.0:3478"` e `automatically_add_embedded_derp_region: true`, o próprio binário do Headscale passa a servir como relay DERP (sobre HTTPS) e servidor STUN (UDP `3478`), injetando automaticamente sua região no mapa DERP distribuído a todos os nós.

## Exemplo
```yaml
derp:
  server:
    enabled: true
    region_id: 999
    region_code: "corp"
    region_name: "Corporate Embedded DERP"
    stun_listen_addr: "0.0.0.0:3478"
    automatically_add_embedded_derp_region: true
  urls: []
```

## Limites e trade-offs
Se você definir `derp.urls: []` (lista vazia) e habilitar o `derp.server`, os clientes `tailscaled` usarão exclusivamente o seu servidor DERP próprio, sem nunca contactar `controlplane.tailscale.com` para baixar a lista de relays públicos.

## Como verificar
Em um nó cliente conectado ao Headscale, execute `tailscale netcheck` e confirme que a região `999 (corp)` aparece com latência medida.

## Conexões
- [[headscale-politicas-acls-grants-tags-ssh-database-vs-file]] — Veja também: Headscale Policy Engine: gerenciamento de ACLs, `Grants`, `Tags`, `Tailscale SSH` e modo `file` vs `database`.
- [[headscale-autenticacao-oidc-single-sign-on-keycloak-dex-authelia]] — Veja também: Headscale com OpenID Connect (OIDC): registro de nós via Single Sign-On com Keycloak, Dex, Authelia ou Okta.

## Fontes
- [Headscale GitHub — README.md (Open Source Self-Hosted Tailscale Control Server, Design Goal & Single Tailnet Architecture)](https://headscale.net/stable/about/features/) — README oficial do juanfont/headscale explicando o papel do servidor de controle na troca de chaves públicas WireGuard, atribuição de IPs e escopo de tailnet única; consultado em 2026-10-03.
- [Headscale Official Documentation — Features (Node Registration, MagicDNS, Extra DNS Records, Subnet Routers, Embedded DERP, ACLs/Grants & OIDC)](https://raw.githubusercontent.com/juanfont/headscale/main/README.md) — Matriz oficial de funcionalidades do Headscale cobrindo registro web/preauthkey/OIDC, extra_records, autoApprovers, Tailscale SSH e DERP embutido; consultado em 2026-10-03.
- [Headscale — Official GitHub Repository](https://github.com/juanfont/headscale) — Repositório oficial BSD-3-Clause do Headscale; consultado em 2026-10-03.
