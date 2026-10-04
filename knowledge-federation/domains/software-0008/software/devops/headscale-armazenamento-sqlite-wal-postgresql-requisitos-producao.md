---
id: software.devops.tranche19.001869
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

# Headscale Persistência e Operação: banco de dados SQLite (WAL) vs PostgreSQL e recomendações de deploy

## Em uma frase
O Headscale armazena o estado dos usuários, nós, chaves públicas, rotas e políticas em um banco de dados relacional, recomendando **SQLite3** (com `write_ahead_log: true` em disco local rápido) como padrão oficial para a maioria das instalações e suportando **PostgreSQL** quando um banco externo já é mantido.

## Por que importa
Como o Headscale foi projetado com escopo focado em uma única *tailnet* (tipicamente dezenas a centenas de nós) e realiza leituras/escritas intensivas em transações curtas de mapa de rede, um SQLite local em modo WAL elimina a latência de rede entre o processo Go e um servidor PostgreSQL remoto.

## Como funciona
A documentação oficial do Headscale destaca também recomendações operacionais importantes: o projeto prioriza instalação direta via pacote `.deb`/`.rpm`, binário systemd ou módulo nativo do **NixOS** (`services.headscale`), desencorajando proxies reversos mal configurados que quebram conexões long-lived HTTP/2, gRPC ou WebSockets do protocolo de controle TS2021.

## Exemplo
```yaml
database:
  type: sqlite
  sqlite:
    path: /var/lib/headscale/db.sqlite
    write_ahead_log: true
```

## Limites e trade-offs
Se houver um firewall ou balanceador na frente do Headscale, garanta suporte integral a conexões persistentes de longa duração, upgrade de protocolo (`Upgrade: tailscale-control-protocol` / WebSockets) e HTTP/2 sem timeouts agressivos de 60 segundos.

## Como verificar
Verifique o serviço ativo com `systemctl status headscale` e a integridade do banco em `/var/lib/headscale/db.sqlite`.

## Conexões
- [[headscale-api-grpc-rest-apikeys-automacao-remota-cli]] — Veja também: Headscale API (gRPC/REST) e `apikeys`: administração remota segura e integração com automação externa.
- [[headscale-compartilhamento-arquivos-taildrop-taildrive-tags-acls]] — Veja também: Headscale File Sharing e Tags: uso de `Taildrop`, `Taildrive` e gerenciamento de `tags` em máquinas de infraestrutura.

## Fontes
- [Headscale GitHub — README.md (Open Source Self-Hosted Tailscale Control Server, Design Goal & Single Tailnet Architecture)](https://raw.githubusercontent.com/juanfont/headscale/main/README.md) — README oficial do juanfont/headscale explicando o papel do servidor de controle na troca de chaves públicas WireGuard, atribuição de IPs e escopo de tailnet única; consultado em 2026-10-03.
- [Headscale Official Documentation — Features (Node Registration, MagicDNS, Extra DNS Records, Subnet Routers, Embedded DERP, ACLs/Grants & OIDC)](https://headscale.net/stable/about/features/) — Matriz oficial de funcionalidades do Headscale cobrindo registro web/preauthkey/OIDC, extra_records, autoApprovers, Tailscale SSH e DERP embutido; consultado em 2026-10-03.
- [Headscale — Official GitHub Repository](https://github.com/juanfont/headscale) — Repositório oficial BSD-3-Clause do Headscale; consultado em 2026-10-03.
