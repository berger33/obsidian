---
id: software.devops.tranche19.001874
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
fontes: ["https://docs.netbird.io/about-netbird/how-netbird-works", "https://raw.githubusercontent.com/netbirdio/netbird/main/README.md", "https://github.com/netbirdio/netbird"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# NetBird Access Control e Posture Checks: políticas baseadas em grupos aplicadas via `nftables` e verificação de postura

## Em uma frase
Por padrão, uma rede full-mesh onde todos os pares se enxergam pode ser indesejada em ambientes corporativos; o NetBird resolve isso com **Groups**, **Access Control Policies** (regras direcionais por protocolo/porta aplicadas localmente via `nftables`/firewall do sistema) e **Device Posture Checks**.

## Por que importa
Permitir que o laptop de um prestador acesse o servidor de homologação somente na porta TCP `443` — e apenas se o laptop estiver rodando uma versão mínima do sistema operacional ou originando de determinado país/rede — exige combinar regras de firewall L3/L4 com checagens de postura do dispositivo.

## Como funciona
Quando o Management Service distribui as políticas de acesso, o próprio cliente NetBird programa o gerenciador de firewall nativo da máquina (como `nftables` no Linux ou userspace packet filter) para bloquear pacotes não autorizados. Além disso, *Posture Checks* verificam versão do cliente NetBird, sistema operacional/kernel, localização geográfica ou faixa de rede antes de liberar a regra de conexão.

## Exemplo
```bash
# Inspecionando o status do agente NetBird e as interfaces/filtros aplicados:
netbird status
sudo nft list tables
```

## Limites e trade-offs
Desative ou substitua a regra padrão inicial `Default (All -> All)` assim que estruturar seus grupos (`developers`, `sre`, `prod-dbs`, `staging-k8s`) para operar em modelo estrito de menor privilégio (*deny-by-default*).

## Como verificar
Teste a comunicação entre dois peers antes e depois de restringir a porta na política de acesso no Management Service.

## Conexões
- [[netbird-setup-keys-provisionamento-automatizado-servidores-containers-ephemeral]] — Veja também: NetBird `Setup Keys`: registro automatizado de servidores, containers e nós efêmeros em massa.
- [[netbird-network-routes-domain-routes-exit-nodes-ha-routing-peers]] — Veja também: NetBird Network Routes e Exit Nodes: roteamento para sub-redes privadas (CIDR), rotas por domínio DNS e grupos de alta disponibilidade.

## Fontes
- [NetBird GitHub — README.md (Zero-Trust Peer-to-Peer Private Network, Feature Matrix, Rosenpass PQC, Self-Hosted Quickstart & Internals)](https://docs.netbird.io/about-netbird/how-netbird-works) — README oficial do netbirdio/netbird detalhando conectividade Kernel WireGuard, controle de acesso, rotas DNS, resistência quântica Rosenpass e self-hosting; consultado em 2026-10-03.
- [NetBird Official Documentation — How NetBird Works (Management, Client, Signal with NaCl Box E2E Encryption & TURN Relay Architecture)](https://raw.githubusercontent.com/netbirdio/netbird/main/README.md) — Documentação oficial de arquitetura do NetBird explicando o funcionamento do Management, Client, Signal (Pion ICE + NaCl box) e Relay; consultado em 2026-10-03.
- [NetBird — Official GitHub Repository](https://github.com/netbirdio/netbird) — Repositório oficial BSD-3-Clause do NetBird; consultado em 2026-10-03.
