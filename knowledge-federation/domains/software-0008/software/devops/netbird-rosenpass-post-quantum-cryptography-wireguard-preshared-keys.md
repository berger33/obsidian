---
id: software.devops.tranche19.001877
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

# NetBird com Rosenpass (`--enable-rosenpass`): resistência pós-quântica (PQC) para túneis WireGuard

## Em uma frase
O NetBird é pioneiro na integração nativa com o **Rosenpass**, adicionando **criptografia resistente a computadores quânticos (*Post-Quantum Cryptography — PQC*)** aos túneis WireGuard por meio da rotação contínua de chaves pré-compartilhadas (`PresharedKey`) negociadas com algoritmos pós-quânticos (Classic McEliece + Kyber).

## Por que importa
O handshake clássico do WireGuard usa `Curve25519` (ECDH), que é vulnerável ao ataque "*harvest now, decrypt later*" caso um adversário capture pacotes criptografados hoje para quebrá-los futuramente com um computador quântico suficientemente potente.

## Como funciona
Quando iniciado com `netbird up --enable-rosenpass` (e opcionalmente `--rosenpass-permissive`), o agente NetBird executa o protocolo Rosenpass em paralelo ao WireGuard e injeta periodicamente a chave simétrica derivada pós-quântica no campo `preshared-key` da sessão WireGuard de cada peer.

## Exemplo
```bash
# Habilitando proteção pós-quântica Rosenpass no cliente NetBird:
netbird down
netbird up --enable-rosenpass
netbird status --detail | grep -i rosenpass
```

## Limites e trade-offs
Se `--enable-rosenpass` for usado **sem** `--rosenpass-permissive`, o peer exigirá obrigatoriamente Rosenpass e recusará estabelecer túneis com peers antigos que não tenham Rosenpass habilitado; use `--rosenpass-permissive` durante migrações graduais da frota.

## Como verificar
Ative `--enable-rosenpass` em dois peers e confirme em `netbird status --detail` que `Rosenpass enabled: true` está ativo na conexão.

## Conexões
- [[netbird-private-dns-custom-zones-ebpf-xdp-port-sharing]] — Veja também: NetBird Private DNS: resolução de FQDNs de peers, `Custom DNS Zones` e compartilhamento de porta DNS com XDP/eBPF.
- [[netbird-self-hosted-deployment-docker-compose-idp-oidc-coturn]] — Veja também: NetBird Self-Hosted: arquitetura de implantação própria com Management, Dashboard, Signal, Relay/Coturn e IdP OIDC.

## Fontes
- [NetBird GitHub — README.md (Zero-Trust Peer-to-Peer Private Network, Feature Matrix, Rosenpass PQC, Self-Hosted Quickstart & Internals)](https://raw.githubusercontent.com/netbirdio/netbird/main/README.md) — README oficial do netbirdio/netbird detalhando conectividade Kernel WireGuard, controle de acesso, rotas DNS, resistência quântica Rosenpass e self-hosting; consultado em 2026-10-03.
- [NetBird Official Documentation — How NetBird Works (Management, Client, Signal with NaCl Box E2E Encryption & TURN Relay Architecture)](https://docs.netbird.io/about-netbird/how-netbird-works) — Documentação oficial de arquitetura do NetBird explicando o funcionamento do Management, Client, Signal (Pion ICE + NaCl box) e Relay; consultado em 2026-10-03.
- [NetBird — Official GitHub Repository](https://github.com/netbirdio/netbird) — Repositório oficial BSD-3-Clause do NetBird; consultado em 2026-10-03.
