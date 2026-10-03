---
id: software.devops.tranche19.001865
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

# Headscale Policy Engine: gerenciamento de ACLs, `Grants`, `Tags`, `Tailscale SSH` e modo `file` vs `database`

## Em uma frase
O motor de políticas do Headscale implementa suporte às políticas declarativas do Tailscale — incluindo **ACLs**, **Grants**, **Tags** (`tagOwners`), alguns **Autogroups**, **Auto approvers**, **Tailscale SSH**, **Node attributes** e blocos de validação **`tests`** e **`sshTests`** — podendo ler a política de um arquivo em disco (`policy.mode: file`) ou armazená-la no banco de dados (`policy.mode: database`).

## Por que importa
Sem políticas de acesso no Headscale, todos os nós registrados na *tailnet* podem comunicar-se livremente entre si em todas as portas.

## Como funciona
Quando configurado com `policy.mode: database` no `config.yaml`, o administrador gerencia a política diretamente pela CLI ou API usando `headscale policy get` e `headscale policy set -f policy.hujson`, e o Headscale valida os `tests`/`sshTests` antes de distribuir os filtros de pacotes em tempo real aos nós conectados.

## Exemplo
```bash
# Visualizando e aplicando uma nova política HuJSON no Headscale:
headscale policy get
headscale policy set --file /etc/headscale/policy.hujson
```

## Limites e trade-offs
Conforme documentado na matriz oficial de recursos do Headscale, grupos vindos do provedor OIDC (*OIDC groups*) não podem ser referenciados diretamente nas ACLs do Headscale: defina os grupos explicitamente dentro da própria política HuJSON ou utilize `tags`.

## Como verificar
Execute `headscale policy set --file policy.hujson` contendo asserções na seção `"tests"` para validar a política.

## Conexões
- [[headscale-rotas-subnet-routers-exit-nodes-auto-approvers-via]] — Veja também: Headscale Routes: aprovação manual e automática (`autoApprovers`) de Subnet Routers, Exit Nodes e filtragem com `via`.
- [[headscale-embedded-derp-server-stun-custom-derpmap-airgapped]] — Veja também: Headscale Embedded DERP Server: operação 100% *air-gapped* com servidor relay DERP e STUN embutido.

## Fontes
- [Headscale GitHub — README.md (Open Source Self-Hosted Tailscale Control Server, Design Goal & Single Tailnet Architecture)](https://headscale.net/stable/about/features/) — README oficial do juanfont/headscale explicando o papel do servidor de controle na troca de chaves públicas WireGuard, atribuição de IPs e escopo de tailnet única; consultado em 2026-10-03.
- [Headscale Official Documentation — Features (Node Registration, MagicDNS, Extra DNS Records, Subnet Routers, Embedded DERP, ACLs/Grants & OIDC)](https://raw.githubusercontent.com/juanfont/headscale/main/README.md) — Matriz oficial de funcionalidades do Headscale cobrindo registro web/preauthkey/OIDC, extra_records, autoApprovers, Tailscale SSH e DERP embutido; consultado em 2026-10-03.
- [Headscale — Official GitHub Repository](https://github.com/juanfont/headscale) — Repositório oficial BSD-3-Clause do Headscale; consultado em 2026-10-03.
