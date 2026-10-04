---
id: software.devops.tranche15.001456
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

# Incus: execução remota de comandos (`incus exec`), transferência de arquivos (`incus file`) e snapshots de estado

## Em uma frase
O CLI `incus` fornece operações nativas para executar comandos dentro de containers e VMs (`incus exec`), editar ou transferir arquivos entre host e instância (`incus file pull/push/edit`) e capturar snapshots instantâneos (`incus snapshot`).

## Por que importa
Permite administrar tanto containers LXC quanto máquinas virtuais QEMU usando exatamente os mesmos comandos, sem precisar configurar servidores SSH ou chaves dentro de cada instância recém-criada (nas VMs, a comunicação ocorre via `incus-agent` sobre vsock).

## Como funciona
O operador executa comandos não interativos (`incus exec first -- apt-get update`) ou abre shells interativos (`incus exec first -- bash`), transfere configurações com `incus file push app.conf first/etc/app.conf` e protege mudanças arriscadas criando pontos de restauração com `incus snapshot create first pre-upgrade` e revertendo com `incus snapshot restore first pre-upgrade`.

## Exemplo
```bash
incus snapshot create app-container clean-state
incus exec app-container -- touch /root/test-change
incus snapshot restore app-container clean-state
incus snapshot list app-container
```

## Limites e trade-offs
A velocidade e o consumo de espaço dos snapshots dependem do driver da storage pool subjacente: backends Copy-on-Write como ZFS, Btrfs e LVM criam snapshots instantâneos sem duplicar blocos, enquanto o driver `dir` realiza cópia completa dos arquivos.

## Como verificar
Crie um snapshot, modifique um arquivo dentro da instância, restaure o snapshot e confirme com `incus exec` que o arquivo retornou ao estado original.

## Conexões
- [[incus-seguranca-rede-incusbr0-mac-ipv4-ipv6-filtering-nftables]] — Veja também: Incus: segurança de rede na bridge `incusbr0` e proteção contra spoofing via `security.mac_filtering` e `ipv4/ipv6_filtering`.
- [[incus-exposicao-remota-api-tls-core-https-address-hardening]] — Veja também: Incus: exposição segura da API REST remota sobre TLS (`core.https_address`) e prevenção de vazamento de cgroups.

## Fontes
- [Incus GitHub — README.md (System Container & Virtual Machine Manager, Linux Containers Governance, Apache-2.0 License & Security Overview)](https://raw.githubusercontent.com/lxc/incus/main/doc/tutorial/first_steps.md) — README oficial do lxc/incus apresentando a arquitetura unificada para containers de sistema e VMs, histórico comunitário pós-LXD e diretrizes fundamentais de segurança; consultado em 2026-10-03.
- [Incus Official Documentation — doc/tutorial/first_steps.md (Initialization, Launching Containers & VMs, Resource Limits, Exec & Snapshots)](https://raw.githubusercontent.com/lxc/incus/main/README.md) — Tutorial oficial First Steps do Incus demonstrando grupos incus vs incus-admin, incus admin init, criação de containers e VMs, limites dinâmicos de CPU/memória/disco e snapshots; consultado em 2026-10-03.
- [Incus Official Documentation — doc/explanation/security.md (Unix Socket Access, Unprivileged Containers, Isolated IDMaps & Bridged NIC Filtering)](https://raw.githubusercontent.com/lxc/incus/main/doc/explanation/security.md) — Documentação oficial de segurança do Incus detalhando isolamento de user namespaces, security.idmap.isolated, proteção contra vazamento de cgroups e filtragem MAC/IPv4/IPv6 na bridge incusbr0; consultado em 2026-10-03.
