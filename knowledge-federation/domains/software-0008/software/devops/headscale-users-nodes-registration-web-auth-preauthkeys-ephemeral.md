---
id: software.devops.tranche19.001862
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

# Headscale: gerenciamento de `Users` e registro de `Nodes` via Web Auth, `PreAuthKeys` e nós efêmeros

## Em uma frase
No Headscale, toda máquina registrada (*Node*) pertence a um **`User`** (antigamente chamado *namespace*) dentro da *tailnet* única do servidor, podendo ser registrada por **Web Authentication** (onde o administrador aprova a chave exibida na URL de registro) ou de forma totalmente automatizada via **Pre-Authenticated Keys (`preauthkeys`)**.

## Por que importa
Ao provisionar 50 worker nodes Kubernetes ou containers efêmeros de CI/CD via Terraform/Cloud-Init, aprovar cada máquina manualmente copiando comandos no terminal é inviável.

## Como funciona
O administrador cria um usuário com `headscale users create infra` e gera uma chave pré-autenticada com `headscale preauthkeys create --user <id> --reusable --expiration 24h --ephemeral`. Quando o container ou VM executa `tailscale up --login-server https://... --authkey <key>`, o Headscale registra o nó instantaneamente e, se a chave for `--ephemeral`, remove o nó automaticamente quando ele fica offline.

## Exemplo
```bash
headscale users create prod-infra
headscale users list
headscale preauthkeys create --user 1 --reusable --ephemeral --expiration 24h
headscale nodes list
```

## Limites e trade-offs
No fluxo interativo sem chave (`tailscale up --login-server ...`), o cliente exibe uma URL contendo a `nodekey` pública; o administrador do Headscale aprova o nó rodando `headscale nodes register --user <user> --key nodekey:<hex>`.

## Como verificar
Liste todas as máquinas registradas, seus IPs e status online/offline com `headscale nodes list`.

## Conexões
- [[headscale-arquitetura-control-server-open-source-self-hosted-tailscale]] — Veja também: Headscale: arquitetura do servidor de controle open-source e *self-hosted* compatível com clientes oficiais Tailscale.
- [[headscale-dns-magicdns-split-dns-extra-records-config-yaml]] — Veja também: Headscale DNS: configuração de `MagicDNS`, `Split DNS` (nameservers restritos) e `extra_records` exclusivos do Headscale.

## Fontes
- [Headscale GitHub — README.md (Open Source Self-Hosted Tailscale Control Server, Design Goal & Single Tailnet Architecture)](https://headscale.net/stable/about/features/) — README oficial do juanfont/headscale explicando o papel do servidor de controle na troca de chaves públicas WireGuard, atribuição de IPs e escopo de tailnet única; consultado em 2026-10-03.
- [Headscale Official Documentation — Features (Node Registration, MagicDNS, Extra DNS Records, Subnet Routers, Embedded DERP, ACLs/Grants & OIDC)](https://raw.githubusercontent.com/juanfont/headscale/main/README.md) — Matriz oficial de funcionalidades do Headscale cobrindo registro web/preauthkey/OIDC, extra_records, autoApprovers, Tailscale SSH e DERP embutido; consultado em 2026-10-03.
- [Headscale — Official GitHub Repository](https://github.com/juanfont/headscale) — Repositório oficial BSD-3-Clause do Headscale; consultado em 2026-10-03.
