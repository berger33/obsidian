---
id: software.devops.tranche19.001864
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

# Headscale Routes: aprovação manual e automática (`autoApprovers`) de Subnet Routers, Exit Nodes e filtragem com `via`

## Em uma frase
O Headscale suporta **Subnet Routers** (nós que anunciam sub-redes CIDR via `tailscale up --advertise-routes=10.10.0.0/16`), **Exit Nodes** (`--advertise-exit-node`) e filtragem de rotas com **`via`** em `grants`, permitindo aprovar rotas manualmente via CLI (`headscale nodes approve-routes`) ou automaticamente via política **`autoApprovers`**.

## Por que importa
Se qualquer nó comprometido na *tailnet* pudesse anunciar a rota `0.0.0.0/0` ou `10.0.0.0/8` e tê-la ativada sem autorização do controlador, ele sequestraria o tráfego de toda a rede.

## Como funciona
Por padrão, quando um nó anuncia rotas com `--advertise-routes`, elas ficam listadas como disponíveis mas desabilitadas no Headscale até que o administrador execute `headscale nodes list-routes` e `headscale nodes approve-routes --identifier <node-id> --routes "10.10.0.0/16"` — ou até que a identidade/tag do nó corresponda a uma regra em `autoApprovers.routes` ou `autoApprovers.exitNode`.

## Exemplo
```bash
# Listando e habilitando rotas anunciadas por um nó no Headscale:
headscale nodes list-routes
headscale nodes approve-routes --identifier 4 --routes "10.20.0.0/16,10.30.0.0/16"
```

## Limites e trade-offs
Ao anunciar múltiplas réplicas do mesmo CIDR como Subnet Routers em nós diferentes, o Headscale suporta alta disponibilidade e failover de rota entre os roteadores aprovados.

## Como verificar
Execute `headscale nodes list-routes` para auditar todas as rotas anunciadas e verificar quais estão efetivamente aprovadas e primárias.

## Conexões
- [[headscale-dns-magicdns-split-dns-extra-records-config-yaml]] — Veja também: Headscale DNS: configuração de `MagicDNS`, `Split DNS` (nameservers restritos) e `extra_records` exclusivos do Headscale.
- [[headscale-politicas-acls-grants-tags-ssh-database-vs-file]] — Veja também: Headscale Policy Engine: gerenciamento de ACLs, `Grants`, `Tags`, `Tailscale SSH` e modo `file` vs `database`.

## Fontes
- [Headscale GitHub — README.md (Open Source Self-Hosted Tailscale Control Server, Design Goal & Single Tailnet Architecture)](https://headscale.net/stable/about/features/) — README oficial do juanfont/headscale explicando o papel do servidor de controle na troca de chaves públicas WireGuard, atribuição de IPs e escopo de tailnet única; consultado em 2026-10-03.
- [Headscale Official Documentation — Features (Node Registration, MagicDNS, Extra DNS Records, Subnet Routers, Embedded DERP, ACLs/Grants & OIDC)](https://raw.githubusercontent.com/juanfont/headscale/main/README.md) — Matriz oficial de funcionalidades do Headscale cobrindo registro web/preauthkey/OIDC, extra_records, autoApprovers, Tailscale SSH e DERP embutido; consultado em 2026-10-03.
- [Headscale — Official GitHub Repository](https://github.com/juanfont/headscale) — Repositório oficial BSD-3-Clause do Headscale; consultado em 2026-10-03.
