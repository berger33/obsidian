---
id: software.devops.tranche15.001459
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
fontes: ["https://raw.githubusercontent.com/lxc/incus/main/README.md", "https://raw.githubusercontent.com/lxc/incus/main/doc/explanation/security.md", "https://raw.githubusercontent.com/lxc/incus/main/doc/tutorial/first_steps.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Incus: governança comunitária Linux Containers, licença Apache-2.0 sem CLA e pacotes Zabbly

## Em uma frase
O Incus foi criado e adotado pela comunidade Linux Containers como sucessor comunitário direto do LXD após a mudança de governança e licenciamento do LXD pela Canonical, mantendo a licença Apache-2.0 livre de *Contributor License Agreement* (CLA).

## Por que importa
Para organizações que dependem de containers de sistema em infraestrutura de longo prazo, a governança aberta na organização `lxc/incus`, liderada pelos criadores originais do LXD, garante continuidade técnica, API Go estável (`github.com/lxc/incus/v7/client`) e ausência de relicenciamento proprietário.

## Como funciona
O projeto disponibiliza pacotes nativos nas principais distribuições Linux (Debian, Ubuntu, Fedora, Arch, Gentoo, NixOS, Alpine), pacotes oficiais mantidos comercialmente pela Zabbly para Debian e Ubuntu, além de ferramenta de migração direta (`lxd-to-incus`) para converter instalações existentes.

## Exemplo
```bash
incus version
incus admin os system show || incus info
```

## Limites e trade-offs
Ao operar o Incus em produção, utilize apenas versões suportadas (releases LTS ou a série estável corrente) e mantenha o kernel do sistema operacional hospedeiro atualizado com patches de segurança.

## Como verificar
Verifique a versão do cliente e do servidor daemon com `incus version` e confirme que ambos estão alinhados na mesma série suportada.

## Conexões
- [[incus-ciclo-vida-instancias-copy-stop-delete-force-profiles]] — Veja também: Incus: clonagem rápida de instâncias (`incus copy`), perfis reutilizáveis e gerenciamento de ciclo de vida.
- [[incus-diferenca-system-containers-vs-oci-docker-aninhamento]] — Veja também: Incus: escolha arquitetural entre containers de sistema (Incus) e containers de aplicação (Docker/Kubernetes).

## Fontes
- [Incus GitHub — README.md (System Container & Virtual Machine Manager, Linux Containers Governance, Apache-2.0 License & Security Overview)](https://raw.githubusercontent.com/lxc/incus/main/README.md) — README oficial do lxc/incus apresentando a arquitetura unificada para containers de sistema e VMs, histórico comunitário pós-LXD e diretrizes fundamentais de segurança; consultado em 2026-10-03.
- [Incus Official Documentation — doc/tutorial/first_steps.md (Initialization, Launching Containers & VMs, Resource Limits, Exec & Snapshots)](https://raw.githubusercontent.com/lxc/incus/main/doc/explanation/security.md) — Tutorial oficial First Steps do Incus demonstrando grupos incus vs incus-admin, incus admin init, criação de containers e VMs, limites dinâmicos de CPU/memória/disco e snapshots; consultado em 2026-10-03.
- [Incus Official Documentation — doc/explanation/security.md (Unix Socket Access, Unprivileged Containers, Isolated IDMaps & Bridged NIC Filtering)](https://raw.githubusercontent.com/lxc/incus/main/doc/tutorial/first_steps.md) — Documentação oficial de segurança do Incus detalhando isolamento de user namespaces, security.idmap.isolated, proteção contra vazamento de cgroups e filtragem MAC/IPv4/IPv6 na bridge incusbr0; consultado em 2026-10-03.
