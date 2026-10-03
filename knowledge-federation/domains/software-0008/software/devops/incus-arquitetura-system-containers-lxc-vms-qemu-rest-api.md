---
id: software.devops.tranche15.001451
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
fontes: ["https://raw.githubusercontent.com/lxc/incus/main/README.md", "https://raw.githubusercontent.com/lxc/incus/main/doc/tutorial/first_steps.md", "https://raw.githubusercontent.com/lxc/incus/main/doc/explanation/security.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Linux Containers Incus: gerenciador unificado de containers de sistema (LXC) e máquinas virtuais (QEMU)

## Em uma frase
O Incus (mantido pela comunidade Linux Containers sob licença Apache-2.0, sem CLA) é um gerenciador moderno de containers de sistema e máquinas virtuais construído em torno de uma API REST unificada e da CLI `incus`.

## Por que importa
Diferentemente de containers de aplicação (como Docker/OCI, desenhados para rodar um único processo efêmero), os containers de sistema do Incus executam um sistema operacional Linux completo (com `systemd`/init, múltiplos serviços, cron e SSH) com a densidade e leveza de namespaces do kernel, lado a lado com VMs completas baseadas em QEMU/KVM.

## Como funciona
Originado como o fork comunitário do LXD liderado pela equipe original que criou o projeto, o Incus escala desde uma única estação de trabalho ou homelab até clusters inteiros de datacenter, consumindo imagens oficiais de dezenas de distribuições a partir do servidor `images:` (`https://images.linuxcontainers.org/`).

## Exemplo
```bash
incus admin init --minimal
incus image list images: debian/12
incus launch images:debian/12 app-container
incus launch images:debian/12 app-vm --vm
incus list
```

## Limites e trade-offs
Mesmo usando exatamente o mesmo identificador de imagem (`images:debian/12`), quando a flag `--vm` é passada em `incus launch`, o Incus baixa uma variante específica da imagem contendo kernel próprio e partição EFI/disco compatível com máquina virtual.

## Como verificar
Execute `incus list` e verifique a coluna `TYPE` distinguindo `CONTAINER` de `VIRTUAL-MACHINE`.

## Conexões
- [[incus-grupos-acesso-incus-vs-incus-admin-seguranca-socket]] — Veja também: Incus: controle de acesso local pelos grupos `incus` vs `incus-admin` e implicações de segurança do socket Unix.

## Fontes
- [Incus GitHub — README.md (System Container & Virtual Machine Manager, Linux Containers Governance, Apache-2.0 License & Security Overview)](https://raw.githubusercontent.com/lxc/incus/main/README.md) — README oficial do lxc/incus apresentando a arquitetura unificada para containers de sistema e VMs, histórico comunitário pós-LXD e diretrizes fundamentais de segurança; consultado em 2026-10-03.
- [Incus Official Documentation — doc/tutorial/first_steps.md (Initialization, Launching Containers & VMs, Resource Limits, Exec & Snapshots)](https://raw.githubusercontent.com/lxc/incus/main/doc/tutorial/first_steps.md) — Tutorial oficial First Steps do Incus demonstrando grupos incus vs incus-admin, incus admin init, criação de containers e VMs, limites dinâmicos de CPU/memória/disco e snapshots; consultado em 2026-10-03.
- [Incus Official Documentation — doc/explanation/security.md (Unix Socket Access, Unprivileged Containers, Isolated IDMaps & Bridged NIC Filtering)](https://raw.githubusercontent.com/lxc/incus/main/doc/explanation/security.md) — Documentação oficial de segurança do Incus detalhando isolamento de user namespaces, security.idmap.isolated, proteção contra vazamento de cgroups e filtragem MAC/IPv4/IPv6 na bridge incusbr0; consultado em 2026-10-03.
