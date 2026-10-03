---
id: software.devops.tranche15.001454
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
fontes: ["https://raw.githubusercontent.com/lxc/incus/main/doc/tutorial/first_steps.md", "https://raw.githubusercontent.com/lxc/incus/main/README.md", "https://raw.githubusercontent.com/lxc/incus/main/doc/explanation/security.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Incus: aplicação dinâmica de limites de CPU, memória (`limits.cpu`, `limits.memory`) e redimensionamento de disco

## Em uma frase
O Incus permite definir limites de CPU, memória e disco tanto na criação da instância (`--config`) quanto em tempo real com a instância em execução (`incus config set` e `incus config device override`).

## Por que importa
Por padrão, um container de sistema sem limites declarados enxerga toda a memória RAM e todos os núcleos de CPU do servidor físico (ex.: em `free -m` e `nproc`), o que pode enganar aplicações que autodimensionam pools de threads ou heap JVM com base nos recursos visíveis.

## Como funciona
Ao aplicar `incus config set <nome> limits.memory=128MiB` e `limits.cpu=1`, o Incus atualiza imediatamente os controladores de cgroup e a visão virtualizada de `/proc/meminfo` e `/proc/cpuinfo` dentro do container sem exigir reboot. Para máquinas virtuais, o disco raiz pode ser expandido via `incus config device override <vm> root size=30GiB` seguido de `incus restart`.

## Exemplo
```bash
incus launch images:debian/12 limited --config limits.cpu=1 --config limits.memory=192MiB
incus exec limited -- free -m
incus config set limited limits.memory=128MiB
incus exec limited -- free -m
```

## Limites e trade-offs
Diferentemente de containers (onde limites de memória e CPU refletem instantaneamente), expandir o tamanho do dispositivo `root` de uma máquina virtual (`--vm`) exige reiniciar a VM (`incus restart`) para que a partição seja redimensionada no boot.

## Como verificar
Compare a saída de `incus exec <nome> -- free -m` e `incus exec <nome> -- nproc` antes e depois de aplicar os limites.

## Conexões
- [[incus-containers-unprivileged-user-namespaces-idmap-isolated]] — Veja também: Incus: containers não privilegiados por padrão (`user namespaces`) e isolamento de UID/GID (`security.idmap.isolated`).
- [[incus-seguranca-rede-incusbr0-mac-ipv4-ipv6-filtering-nftables]] — Veja também: Incus: segurança de rede na bridge `incusbr0` e proteção contra spoofing via `security.mac_filtering` e `ipv4/ipv6_filtering`.

## Fontes
- [Incus GitHub — README.md (System Container & Virtual Machine Manager, Linux Containers Governance, Apache-2.0 License & Security Overview)](https://raw.githubusercontent.com/lxc/incus/main/doc/tutorial/first_steps.md) — README oficial do lxc/incus apresentando a arquitetura unificada para containers de sistema e VMs, histórico comunitário pós-LXD e diretrizes fundamentais de segurança; consultado em 2026-10-03.
- [Incus Official Documentation — doc/tutorial/first_steps.md (Initialization, Launching Containers & VMs, Resource Limits, Exec & Snapshots)](https://raw.githubusercontent.com/lxc/incus/main/README.md) — Tutorial oficial First Steps do Incus demonstrando grupos incus vs incus-admin, incus admin init, criação de containers e VMs, limites dinâmicos de CPU/memória/disco e snapshots; consultado em 2026-10-03.
- [Incus Official Documentation — doc/explanation/security.md (Unix Socket Access, Unprivileged Containers, Isolated IDMaps & Bridged NIC Filtering)](https://raw.githubusercontent.com/lxc/incus/main/doc/explanation/security.md) — Documentação oficial de segurança do Incus detalhando isolamento de user namespaces, security.idmap.isolated, proteção contra vazamento de cgroups e filtragem MAC/IPv4/IPv6 na bridge incusbr0; consultado em 2026-10-03.
