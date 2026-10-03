---
id: software.devops.tranche19.001878
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

# NetBird Self-Hosted: arquitetura de implantação própria com Management, Dashboard, Signal, Relay/Coturn e IdP OIDC

## Em uma frase
Todo o conjunto de servidores do NetBird (**Management**, **Dashboard Web UI**, **Signal**, **Relay** e **Coturn STUN/TURN**) é 100% open-source e pode ser auto-hospedado (*self-hosted*) em minutos via Docker Compose ou Kubernetes integrado a qualquer provedor OIDC (Zitadel embutido, Keycloak, Authentik, Okta, Entra ID).

## Por que importa
Organizações sujeitas a requisitos estritos de residência de dados ou que desejam operar sua malha Zero-Trust sem limites de usuários ou dependência de nuvem de terceiros precisam de uma pilha self-hosted completa com UI administrativa.

## Como funciona
Conforme documentado no repositório oficial, os requisitos mínimos para o quickstart self-hosted em uma VM Linux são **1 CPU**, **2 GB de RAM**, um domínio público e as portas **TCP 80/443** e **UDP 3478** abertas.

## Exemplo
```bash
# Quickstart oficial para implantação self-hosted do NetBird com Docker Compose:
export NETBIRD_DOMAIN=netbird.example.com
curl -fsSL https://github.com/netbirdio/netbird/releases/latest/download/getting-started.sh | bash
```

## Limites e trade-offs
Em instalações self-hosted em produção, configure backups regulares do banco de dados do Management Service (SQLite ou PostgreSQL) e do provedor de identidade (como Zitadel/Keycloak), além de monitorar a renovação dos certificados TLS.

## Como verificar
Verifique os containers da pilha self-hosted com `docker compose ps` e valide o acesso HTTPS ao Dashboard e à API do Management.

## Conexões
- [[netbird-rosenpass-post-quantum-cryptography-wireguard-preshared-keys]] — Veja também: NetBird com Rosenpass (`--enable-rosenpass`): resistência pós-quântica (PQC) para túneis WireGuard.
- [[netbird-ssh-server-central-access-policies-browser-ssh-rdp]] — Veja também: NetBird SSH e Browser Client: acesso SSH governado por políticas centrais e terminal SSH/RDP no navegador.

## Fontes
- [NetBird GitHub — README.md (Zero-Trust Peer-to-Peer Private Network, Feature Matrix, Rosenpass PQC, Self-Hosted Quickstart & Internals)](https://raw.githubusercontent.com/netbirdio/netbird/main/README.md) — README oficial do netbirdio/netbird detalhando conectividade Kernel WireGuard, controle de acesso, rotas DNS, resistência quântica Rosenpass e self-hosting; consultado em 2026-10-03.
- [NetBird Official Documentation — How NetBird Works (Management, Client, Signal with NaCl Box E2E Encryption & TURN Relay Architecture)](https://docs.netbird.io/about-netbird/how-netbird-works) — Documentação oficial de arquitetura do NetBird explicando o funcionamento do Management, Client, Signal (Pion ICE + NaCl box) e Relay; consultado em 2026-10-03.
- [NetBird — Official GitHub Repository](https://github.com/netbirdio/netbird) — Repositório oficial BSD-3-Clause do NetBird; consultado em 2026-10-03.
