---
id: software.devops.tranche19.001861
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

# Headscale: arquitetura do servidor de controle open-source e *self-hosted* compatível com clientes oficiais Tailscale

## Em uma frase
O **Headscale** (escrito em Go e licenciado sob BSD-3-Clause) é uma implementação open-source e auto-hospedada (*self-hosted*) do servidor de controle do Tailscale, projetada para operar uma única rede Tailscale (*tailnet*) sob total soberania de infraestrutura usando os clientes oficiais `tailscale` em Linux, macOS, Windows, iOS, Android e FreeBSD.

## Por que importa
Embora o cliente `tailscaled` seja open-source, o servidor de controle SaaS oficial da Tailscale é proprietário; organizações, laboratórios e ambientes *air-gapped* que exigem manter 100% do plano de controle (troca de chaves, DNS, ACLs e autenticação) on-premises precisam de um servidor de controle aberto.

## Como funciona
O Headscale atua como o coordenador central de uma *tailnet*: registra nós (via autenticação web, chaves pré-autenticadas ou OIDC), atribui endereços IPv4 (`100.64.0.0/10`) e IPv6 (`fd7a:115c:a1e0::/48`) em dual-stack, distribui chaves públicas WireGuard entre pares, gerencia MagicDNS/Split DNS, rotas e políticas ACL/Grants.

## Exemplo
```bash
# Conectando o cliente oficial Tailscale a um servidor Headscale próprio:
tailscale up --login-server https://headscale.corp.example.com
```

## Limites e trade-offs
Como o Headscale implementa o protocolo de controle esperado pelo `tailscaled`, os nós continuam estabelecendo túneis WireGuard ponto-a-ponto diretos entre si; o servidor Headscale nunca roteia o tráfego de dados (a menos que o relay DERP embutido opcional seja ativado).

## Como verificar
Verifique a versão e o status do servidor executando `headscale version` e `headscale nodes list` no host do Headscale.

## Conexões
- [[headscale-users-nodes-registration-web-auth-preauthkeys-ephemeral]] — Veja também: Headscale: gerenciamento de `Users` e registro de `Nodes` via Web Auth, `PreAuthKeys` e nós efêmeros.

## Fontes
- [Headscale GitHub — README.md (Open Source Self-Hosted Tailscale Control Server, Design Goal & Single Tailnet Architecture)](https://raw.githubusercontent.com/juanfont/headscale/main/README.md) — README oficial do juanfont/headscale explicando o papel do servidor de controle na troca de chaves públicas WireGuard, atribuição de IPs e escopo de tailnet única; consultado em 2026-10-03.
- [Headscale Official Documentation — Features (Node Registration, MagicDNS, Extra DNS Records, Subnet Routers, Embedded DERP, ACLs/Grants & OIDC)](https://headscale.net/stable/about/features/) — Matriz oficial de funcionalidades do Headscale cobrindo registro web/preauthkey/OIDC, extra_records, autoApprovers, Tailscale SSH e DERP embutido; consultado em 2026-10-03.
- [Headscale — Official GitHub Repository](https://github.com/juanfont/headscale) — Repositório oficial BSD-3-Clause do Headscale; consultado em 2026-10-03.
