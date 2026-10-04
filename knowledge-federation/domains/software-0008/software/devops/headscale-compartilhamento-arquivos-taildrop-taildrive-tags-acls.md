---
id: software.devops.tranche19.001870
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

# Headscale File Sharing e Tags: uso de `Taildrop`, `Taildrive` e gerenciamento de `tags` em máquinas de infraestrutura

## Em uma frase
O Headscale suporta os recursos nativos de compartilhamento de arquivos do cliente Tailscale — **Taildrop** (envio direto de arquivos entre dispositivos do mesmo usuário via `tailscale file cp`) e **Taildrive** (compartilhamento de diretórios via WebDAV na *tailnet*) — além do gerenciamento de **Tags** de infraestrutura (`headscale nodes tag`).

## Por que importa
Diferenciar dispositivos pessoais de um usuário (que podem trocar arquivos via Taildrop entre o celular e o laptop do mesmo dono) de servidores de infraestrutura compartilhados (que pertencem à organização via `tag:server`) é fundamental para a governança da *tailnet*.

## Como funciona
O administrador pode atribuir tags a um nó tanto no momento do registro (vinculando `--tags tag:k8s,tag:prod` na criação da `preauthkey`) quanto posteriormente pela CLI com `headscale nodes tag --identifier <node-id> --tags tag:prod-db`.

## Exemplo
```bash
# Atribuindo tags de infraestrutura a um nó existente no Headscale:
headscale nodes tag --identifier 2 --tags "tag:prod-server,tag:ssh-enabled"
headscale nodes list -t
```

## Limites e trade-offs
Assim que um nó recebe tags no Headscale, ele passa a ser um nó "tagged" (sua identidade deixa de ser a do usuário humano original para fins de avaliação de ACLs e passa a responder pelas tags atribuídas).

## Como verificar
Execute `headscale nodes list --tags` (`-t`) para inspecionar as tags aplicadas a cada máquina da *tailnet*.

## Conexões
- [[headscale-armazenamento-sqlite-wal-postgresql-requisitos-producao]] — Veja também: Headscale Persistência e Operação: banco de dados SQLite (WAL) vs PostgreSQL e recomendações de deploy.

## Fontes
- [Headscale GitHub — README.md (Open Source Self-Hosted Tailscale Control Server, Design Goal & Single Tailnet Architecture)](https://headscale.net/stable/about/features/) — README oficial do juanfont/headscale explicando o papel do servidor de controle na troca de chaves públicas WireGuard, atribuição de IPs e escopo de tailnet única; consultado em 2026-10-03.
- [Headscale Official Documentation — Features (Node Registration, MagicDNS, Extra DNS Records, Subnet Routers, Embedded DERP, ACLs/Grants & OIDC)](https://raw.githubusercontent.com/juanfont/headscale/main/README.md) — Matriz oficial de funcionalidades do Headscale cobrindo registro web/preauthkey/OIDC, extra_records, autoApprovers, Tailscale SSH e DERP embutido; consultado em 2026-10-03.
- [Headscale — Official GitHub Repository](https://github.com/juanfont/headscale) — Repositório oficial BSD-3-Clause do Headscale; consultado em 2026-10-03.
