---
id: software.devops.tranche19.001880
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
fontes: ["https://raw.githubusercontent.com/netbirdio/netbird/main/README.md", "https://docs.netbird.io/about-netbird/how-netbird-works", "https://github.com/netbirdio/netbird"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# NetBird Automação e Perfis: Terraform Provider (`netbirdio/netbird`), Ansible Collection e `netbird profile` multi-conta

## Em uma frase
O NetBird oferece automação completa via **API Pública REST**, **Terraform Provider oficial (`netbirdio/netbird`)** e **Ansible Collection (`netbirdio/ansible-netbird`)**, além do subcomando **`netbird profile`** na CLI/GUI para alternar rapidamente entre múltiplas contas ou servidores Management.

## Por que importa
Consultorias de DevOps/SRE e equipes de plataforma que gerenciam múltiplos ambientes isolados (ou clientes distintos, cada um com seu próprio Management Service) precisam alternar de rede em segundos e provisionar grupos, políticas, rotas e setup keys via código.

## Como funciona
Com `netbird profile add <nome>` e `netbird profile select <nome>`, o cliente mantém configurações e chaves separadas para diferentes contas/servidores. Já no Terraform, recursos como `netbird_group`, `netbird_policy`, `netbird_route` e `netbird_setup_key` mantêm toda a topologia Zero-Trust versionada no Git.

## Exemplo
```bash
# Gerenciando múltiplos perfis de conexão no cliente NetBird:
netbird profile list
netbird profile add staging-selfhosted
netbird profile select staging-selfhosted --management-url https://netbird.staging.corp.io
```

## Limites e trade-offs
Em conjunto com a sincronização de grupos do IdP via JWT (*IdP groups sync*) e reautenticação periódica obrigatória (*periodic re-authentication*), o Terraform Provider garante que o ciclo de vida de acesso acompanhe imediatamente o diretório corporativo.

## Como verificar
Execute `netbird profile list` para inspecionar os perfis configurados localmente.

## Conexões
- [[netbird-ssh-server-central-access-policies-browser-ssh-rdp]] — Veja também: NetBird SSH e Browser Client: acesso SSH governado por políticas centrais e terminal SSH/RDP no navegador.

## Fontes
- [NetBird GitHub — README.md (Zero-Trust Peer-to-Peer Private Network, Feature Matrix, Rosenpass PQC, Self-Hosted Quickstart & Internals)](https://raw.githubusercontent.com/netbirdio/netbird/main/README.md) — README oficial do netbirdio/netbird detalhando conectividade Kernel WireGuard, controle de acesso, rotas DNS, resistência quântica Rosenpass e self-hosting; consultado em 2026-10-03.
- [NetBird Official Documentation — How NetBird Works (Management, Client, Signal with NaCl Box E2E Encryption & TURN Relay Architecture)](https://docs.netbird.io/about-netbird/how-netbird-works) — Documentação oficial de arquitetura do NetBird explicando o funcionamento do Management, Client, Signal (Pion ICE + NaCl box) e Relay; consultado em 2026-10-03.
- [NetBird — Official GitHub Repository](https://github.com/netbirdio/netbird) — Repositório oficial BSD-3-Clause do NetBird; consultado em 2026-10-03.
