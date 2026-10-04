---
id: software.devops.tranche15.001460
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

# Incus: escolha arquitetural entre containers de sistema (Incus) e containers de aplicação (Docker/Kubernetes)

## Em uma frase
Enquanto Docker e Kubernetes empacotam processos únicos a partir de camadas OCI imutáveis, o Incus gerencia máquinas completas (containers de sistema LXC ou VMs QEMU) com estado persistente, init completo e administração tradicional de SO.

## Por que importa
Muitas cargas de trabalho — como laboratórios de infraestrutura, nós de clusters Kubernetes/Nomad de teste, sistemas legados multi-processo com systemd ou rodar o próprio Docker/Podman de forma aninhada (`security.nesting=true`) — encaixam-se muito melhor em um container de sistema ou VM do Incus do que em um container OCI.

## Como funciona
Em vez de reconstruir a imagem a cada mudança como em um `Dockerfile`, uma instância Incus é tratada como uma máquina virtual leve gerenciada por configuração declarativa, Ansible, cloud-init ou snapshots, podendo inclusive ser usada via Colima (`colima start --runtime incus`) em estações macOS.

## Exemplo
```bash
incus launch images:ubuntu/24.04 docker-host \
  --config security.nesting=true \
  --config security.syscalls.intercept.mknod=true
incus exec docker-host -- systemctl status
```

## Limites e trade-offs
Habilitar aninhamento (`security.nesting=true`) para rodar Docker ou Kubernetes dentro de um container Incus expõe interfaces adicionais de procfs/sysfs dentro do user namespace do container; para isolamento máximo entre tenants hostis, prefira instâncias `--vm` (QEMU/KVM).

## Como verificar
Execute `incus exec <instancia> -- systemctl is-system-running` para confirmar que o sistema init completo está operacional dentro do container de sistema.

## Conexões
- [[incus-governanca-comunitaria-migracao-lxd-apache2-sem-cla]] — Veja também: Incus: governança comunitária Linux Containers, licença Apache-2.0 sem CLA e pacotes Zabbly.

## Fontes
- [Incus GitHub — README.md (System Container & Virtual Machine Manager, Linux Containers Governance, Apache-2.0 License & Security Overview)](https://raw.githubusercontent.com/lxc/incus/main/README.md) — README oficial do lxc/incus apresentando a arquitetura unificada para containers de sistema e VMs, histórico comunitário pós-LXD e diretrizes fundamentais de segurança; consultado em 2026-10-03.
- [Incus Official Documentation — doc/tutorial/first_steps.md (Initialization, Launching Containers & VMs, Resource Limits, Exec & Snapshots)](https://raw.githubusercontent.com/lxc/incus/main/doc/tutorial/first_steps.md) — Tutorial oficial First Steps do Incus demonstrando grupos incus vs incus-admin, incus admin init, criação de containers e VMs, limites dinâmicos de CPU/memória/disco e snapshots; consultado em 2026-10-03.
- [Incus Official Documentation — doc/explanation/security.md (Unix Socket Access, Unprivileged Containers, Isolated IDMaps & Bridged NIC Filtering)](https://raw.githubusercontent.com/lxc/incus/main/doc/explanation/security.md) — Documentação oficial de segurança do Incus detalhando isolamento de user namespaces, security.idmap.isolated, proteção contra vazamento de cgroups e filtragem MAC/IPv4/IPv6 na bridge incusbr0; consultado em 2026-10-03.
