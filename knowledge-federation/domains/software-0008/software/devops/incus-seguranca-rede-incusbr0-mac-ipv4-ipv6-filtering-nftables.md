---
id: software.devops.tranche15.001455
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/lxc/incus/main/doc/explanation/security.md", "https://raw.githubusercontent.com/lxc/incus/main/doc/tutorial/first_steps.md", "https://raw.githubusercontent.com/lxc/incus/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Incus: segurança de rede na bridge `incusbr0` e proteção contra spoofing via `security.mac_filtering` e `ipv4/ipv6_filtering`

## Em uma frase
No modo de rede gerenciado padrão (`incusbr0`), o Incus utiliza um serviço `dnsmasq` por bridge para alocar endereços DHCPv4, anunciar rotas IPv6 (SLAAC) e criar registros DNS autoritativos, oferecendo filtros baseados em `nftables` contra falsificação de MAC e IP.

## Por que importa
Embora o `dnsmasq` impeça o spoofing de nomes DNS no DHCP, uma instância conectada a uma bridge Ethernet L2 padrão pode transmitir quadros arbitrários, realizando ARP/NDP spoofing, falsificação de IP de origem ou envio de Router Advertisements IPv6 maliciosos.

## Como funciona
Para blindar a bridge em ambientes multi-tenant, o administrador ativa nos dispositivos NIC do perfil ou da instância as chaves `security.mac_filtering=true`, `security.ipv4_filtering=true` e `security.ipv6_filtering=true`. O Incus programa regras no `nftables` do host que bloqueiam anúncios ARP/NDP e pacotes cujo MAC ou IP não correspondam exatamente à alocação registrada da instância.

## Exemplo
```bash
incus config device override app-container eth0 \
  security.mac_filtering=true \
  security.ipv4_filtering=true \
  security.ipv6_filtering=true
incus config show app-container
```

## Limites e trade-offs
Habilitar `security.mac_filtering` impede que containers aninhados dentro daquela instância utilizem a rede pai com endereços MAC próprios (como bridges internas ou interfaces `macvlan`).

## Como verificar
Inspecione a configuração efetiva do dispositivo com `incus config show <instancia>` e confirme as regras geradas no `nftables` do host.

## Conexões
- [[incus-configuracao-limites-cpu-memory-root-disk-live-updates]] — Veja também: Incus: aplicação dinâmica de limites de CPU, memória (`limits.cpu`, `limits.memory`) e redimensionamento de disco.
- [[incus-interacao-exec-file-push-pull-snapshots-stateful]] — Veja também: Incus: execução remota de comandos (`incus exec`), transferência de arquivos (`incus file`) e snapshots de estado.

## Fontes
- [Incus GitHub — README.md (System Container & Virtual Machine Manager, Linux Containers Governance, Apache-2.0 License & Security Overview)](https://raw.githubusercontent.com/lxc/incus/main/doc/explanation/security.md) — README oficial do lxc/incus apresentando a arquitetura unificada para containers de sistema e VMs, histórico comunitário pós-LXD e diretrizes fundamentais de segurança; consultado em 2026-10-03.
- [Incus Official Documentation — doc/tutorial/first_steps.md (Initialization, Launching Containers & VMs, Resource Limits, Exec & Snapshots)](https://raw.githubusercontent.com/lxc/incus/main/doc/tutorial/first_steps.md) — Tutorial oficial First Steps do Incus demonstrando grupos incus vs incus-admin, incus admin init, criação de containers e VMs, limites dinâmicos de CPU/memória/disco e snapshots; consultado em 2026-10-03.
- [Incus Official Documentation — doc/explanation/security.md (Unix Socket Access, Unprivileged Containers, Isolated IDMaps & Bridged NIC Filtering)](https://raw.githubusercontent.com/lxc/incus/main/README.md) — Documentação oficial de segurança do Incus detalhando isolamento de user namespaces, security.idmap.isolated, proteção contra vazamento de cgroups e filtragem MAC/IPv4/IPv6 na bridge incusbr0; consultado em 2026-10-03.
