---
id: software.devops.tranche17.001700
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
fontes: ["https://canonical.com/microk8s/docs/high-availability", "https://raw.githubusercontent.com/canonical/microk8s/master/README.md", "https://github.com/canonical/microk8s"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Canonical MicroK8s: execução multiplataforma (macOS/Windows via Multipass) e laboratórios HA em containers LXD/Incus

## Em uma frase
Além da instalação nativa em 42 distribuições Linux, o MicroK8s roda em macOS e Windows sobre máquinas virtuais gerenciadas automaticamente pelo Canonical **Multipass** e suporta a criação de clusters HA multi-nó dentro de containers de sistema **LXD/Incus** em uma única máquina Linux.

## Por que importa
Desenvolvedores em macOS/Windows precisam da mesma CLI `microk8s` usada nas VMs Ubuntu da nuvem, e engenheiros de plataforma precisam testar cenários de falha de 3+ nós do `dqlite` (`voters`, `standby`, `spare`) em uma única estação ou runner de CI sem provisionar 3 VMs pesadas.

## Como funciona
Em macOS e Windows, o instalador do MicroK8s cria e gerencia transparentemente uma VM `microk8s-vm` via Multipass (onde comandos como `multipass exec microk8s -- sudo snap refresh ...` também podem ser executados). Em Linux, aplicando um perfil LXD/Incus com suporte a montagem de dispositivos e AppArmor/cgroups para containers aninhados, é possível subir 3 containers de sistema e formar um cluster HA MicroK8s completo com `microk8s add-node` / `join`.

## Exemplo
```bash
# Em macOS ou Windows via Multipass:
multipass list
multipass exec microk8s-vm -- microk8s status
```

## Limites e trade-offs
Ao rodar o MicroK8s dentro de containers de sistema LXD/Incus, é necessário aplicar o perfil específico para MicroK8s (habilitando `security.nesting=true`, `security.privileged=true` e acesso a `/dev/kmsg`) para que o `kubelet` e o `containerd` iniciem sem erros de permissão.

## Como verificar
Verifique com `microk8s status` dentro das instâncias LXD ou da VM Multipass que o cluster e seus add-ons básicos (`dns`, `hostpath-storage`) estão operacionais.

## Conexões
- [[microk8s-inspect-diagnostico-troubleshooting-pacote-logs]] — Veja também: Canonical MicroK8s: diagnóstico automatizado de saúde e coleta de pacote de suporte com `microk8s inspect`.

## Fontes
- [Canonical MicroK8s GitHub — README.md (Single-Package Snap Kubernetes for Developers, CI/CD, IoT & Edge with Curated Addons)](https://canonical.com/microk8s/docs/high-availability) — README oficial do canonical/microk8s detalhando instalação via Snap, canais de versão, comandos microk8s kubectl/enable/status/inspect e add-ons embutidos; consultado em 2026-10-03.
- [Canonical MicroK8s Official Documentation — High Availability (Automatic dqlite HA, Voters/Standby/Spare Roles, Failure Domains & Node Lifecycle)](https://raw.githubusercontent.com/canonical/microk8s/master/README.md) — Documentação oficial de Alta Disponibilidade do MicroK8s cobrindo datastore dqlite na porta 19001, eleição em 5s, papéis voter/standby/spare e ha-conf; consultado em 2026-10-03.
- [Canonical MicroK8s — Official GitHub Repository](https://github.com/canonical/microk8s) — Repositório oficial Apache-2.0 do Canonical MicroK8s; consultado em 2026-10-03.
