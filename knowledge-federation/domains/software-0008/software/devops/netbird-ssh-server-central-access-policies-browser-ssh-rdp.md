---
id: software.devops.tranche19.001879
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

# NetBird SSH e Browser Client: acesso SSH governado por políticas centrais e terminal SSH/RDP no navegador

## Em uma frase
O NetBird inclui um **servidor SSH integrado** no cliente (`--allow-server-ssh`) governado pelas políticas centrais de controle de acesso do Management Service, além de suporte a **Browser SSH & RDP** diretamente pelo painel web.

## Por que importa
Gerenciar acesso SSH separadamente da política de rede Zero-Trust obriga a manter duas fontes da verdade; com o NetBird SSH, as mesmas regras de grupos e usuários que liberam a conectividade também controlam quem pode abrir sessão SSH na máquina.

## Como funciona
Quando habilitado no peer de destino com `netbird up --allow-server-ssh` e autorizado por uma política de acesso SSH no Management, um engenheiro autorizado conecta-se usando `netbird ssh <user>@<peer-ip-or-fqdn>` (ou pelo cliente no navegador) sem distribuir chaves SSH estáticas manualmente.

## Exemplo
```bash
# No servidor de destino, habilitando o servidor SSH gerenciado pelo NetBird:
netbird up --allow-server-ssh

# Na estação do engenheiro autorizado pela política:
netbird ssh root@100.64.0.25
```

## Limites e trade-offs
Por segurança, o servidor SSH embutido do NetBird vem desabilitado por padrão no agente cliente e precisa ser explicitamente habilitado com `--allow-server-ssh` nos hosts que devem aceitá-lo.

## Como verificar
Verifique em `netbird status --detail` se `SSH Server: Enabled` consta na saída do host.

## Conexões
- [[netbird-self-hosted-deployment-docker-compose-idp-oidc-coturn]] — Veja também: NetBird Self-Hosted: arquitetura de implantação própria com Management, Dashboard, Signal, Relay/Coturn e IdP OIDC.
- [[netbird-automacao-terraform-provider-ansible-multi-account-profiles]] — Veja também: NetBird Automação e Perfis: Terraform Provider (`netbirdio/netbird`), Ansible Collection e `netbird profile` multi-conta.

## Fontes
- [NetBird GitHub — README.md (Zero-Trust Peer-to-Peer Private Network, Feature Matrix, Rosenpass PQC, Self-Hosted Quickstart & Internals)](https://raw.githubusercontent.com/netbirdio/netbird/main/README.md) — README oficial do netbirdio/netbird detalhando conectividade Kernel WireGuard, controle de acesso, rotas DNS, resistência quântica Rosenpass e self-hosting; consultado em 2026-10-03.
- [NetBird Official Documentation — How NetBird Works (Management, Client, Signal with NaCl Box E2E Encryption & TURN Relay Architecture)](https://docs.netbird.io/about-netbird/how-netbird-works) — Documentação oficial de arquitetura do NetBird explicando o funcionamento do Management, Client, Signal (Pion ICE + NaCl box) e Relay; consultado em 2026-10-03.
- [NetBird — Official GitHub Repository](https://github.com/netbirdio/netbird) — Repositório oficial BSD-3-Clause do NetBird; consultado em 2026-10-03.
