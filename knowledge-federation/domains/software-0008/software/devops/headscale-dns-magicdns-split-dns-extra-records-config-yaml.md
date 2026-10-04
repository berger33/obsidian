---
id: software.devops.tranche19.001863
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

# Headscale DNS: configuração de `MagicDNS`, `Split DNS` (nameservers restritos) e `extra_records` exclusivos do Headscale

## Em uma frase
A seção `dns:` do arquivo `config.yaml` do Headscale suporta **MagicDNS** (`magic_dns: true` com `base_domain` customizável, ex.: `tailnet.corp.internal`), **Split DNS** (nameservers globais e restritos por domínio), `search_domains` e o recurso exclusivo **`extra_records`** para injetar registros DNS `A`/`AAAA` arbitrários em todos os clientes da *tailnet*.

## Por que importa
Em redes corporativas ou homelabs, você frequentemente possui serviços rodando atrás de um reverse proxy ou IP de sub-rede (ex.: `git.corp.internal` -> `100.64.0.15`) e quer que todos os nós conectados à VPN resolvam esses nomes sem precisar subir um servidor BIND/CoreDNS separado.

## Como funciona
No `config.yaml` (ou via `extra_records_path` apontando para um arquivo JSON monitorado dinamicamente), basta listar entradas `{ name: "git.corp.internal", type: "A", value: "100.64.0.15" }`. O Headscale distribui esses registros pelo protocolo de controle para o resolvedor `100.100.100.100` de todos os clientes `tailscaled`.

## Exemplo
```yaml
dns:
  magic_dns: true
  base_domain: mesh.corp.internal
  nameservers:
    global:
      - 1.1.1.1
    split:
      k8s.corp.internal:
        - 10.96.0.10
  extra_records:
    - name: "grafana.corp.internal"
      type: "A"
      value: "100.64.0.10"
```

## Limites e trade-offs
Usar `extra_records_path: /var/lib/headscale/extra-records.json` permite adicionar ou alterar registros DNS customizados sem precisar reiniciar o processo do servidor Headscale.

## Como verificar
Após atualizar `extra_records`, execute `dig @100.100.100.100 grafana.corp.internal` em qualquer nó conectado para validar a resposta imediata.

## Conexões
- [[headscale-users-nodes-registration-web-auth-preauthkeys-ephemeral]] — Veja também: Headscale: gerenciamento de `Users` e registro de `Nodes` via Web Auth, `PreAuthKeys` e nós efêmeros.
- [[headscale-rotas-subnet-routers-exit-nodes-auto-approvers-via]] — Veja também: Headscale Routes: aprovação manual e automática (`autoApprovers`) de Subnet Routers, Exit Nodes e filtragem com `via`.

## Fontes
- [Headscale GitHub — README.md (Open Source Self-Hosted Tailscale Control Server, Design Goal & Single Tailnet Architecture)](https://headscale.net/stable/about/features/) — README oficial do juanfont/headscale explicando o papel do servidor de controle na troca de chaves públicas WireGuard, atribuição de IPs e escopo de tailnet única; consultado em 2026-10-03.
- [Headscale Official Documentation — Features (Node Registration, MagicDNS, Extra DNS Records, Subnet Routers, Embedded DERP, ACLs/Grants & OIDC)](https://raw.githubusercontent.com/juanfont/headscale/main/README.md) — Matriz oficial de funcionalidades do Headscale cobrindo registro web/preauthkey/OIDC, extra_records, autoApprovers, Tailscale SSH e DERP embutido; consultado em 2026-10-03.
- [Headscale — Official GitHub Repository](https://github.com/juanfont/headscale) — Repositório oficial BSD-3-Clause do Headscale; consultado em 2026-10-03.
