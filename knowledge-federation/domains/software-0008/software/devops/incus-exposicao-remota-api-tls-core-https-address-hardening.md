---
id: software.devops.tranche15.001457
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
fontes: ["https://raw.githubusercontent.com/lxc/incus/main/doc/explanation/security.md", "https://raw.githubusercontent.com/lxc/incus/main/README.md", "https://raw.githubusercontent.com/lxc/incus/main/doc/tutorial/first_steps.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Incus: exposição segura da API REST remota sobre TLS (`core.https_address`) e prevenção de vazamento de cgroups

## Em uma frase
Por padrão, o daemon do Incus escuta exclusivamente no socket Unix local; para gerenciamento remoto ou formação de clusters, a API HTTPS é habilitada configurando `core.https_address` com autenticação mTLS/OIDC e regras de firewall.

## Por que importa
Expor a API do Incus em `0.0.0.0:8443` sem restringir a interface de rede e sem firewall expõe o plano de controle de virtualização e imagens marcadas como públicas para redes externas.

## Como funciona
A documentação de segurança recomenda vincular `core.https_address` apenas ao endereço IP específico da interface de gerenciamento (nunca a todas as interfaces indiscriminadamente), restringir a porta via firewall apenas a sub-redes autorizadas e aplicar `chmod 400 /proc/sched_debug` e `chmod 700 /sys/kernel/slab/` no host antes de iniciar containers para evitar vazamento de nomes de cgroups entre containers.

## Exemplo
```bash
sudo chmod 400 /proc/sched_debug
sudo chmod 700 /sys/kernel/slab/
incus config set core.https_address 192.168.10.5:8443
incus config show
```

## Limites e trade-offs
Sem a restrição de permissões em `/proc/sched_debug` e `/sys/kernel/slab/`, um usuário dentro de um container pode listar todos os caminhos de cgroups do kernel do host e descobrir os nomes de todos os outros containers vizinhos no servidor.

## Como verificar
Verifique o endereço de bind com `ss -tulpn | grep incus` e as permissões de `/proc/sched_debug` com `stat -c "%a %n" /proc/sched_debug`.

## Conexões
- [[incus-interacao-exec-file-push-pull-snapshots-stateful]] — Veja também: Incus: execução remota de comandos (`incus exec`), transferência de arquivos (`incus file`) e snapshots de estado.
- [[incus-ciclo-vida-instancias-copy-stop-delete-force-profiles]] — Veja também: Incus: clonagem rápida de instâncias (`incus copy`), perfis reutilizáveis e gerenciamento de ciclo de vida.

## Fontes
- [Incus GitHub — README.md (System Container & Virtual Machine Manager, Linux Containers Governance, Apache-2.0 License & Security Overview)](https://raw.githubusercontent.com/lxc/incus/main/doc/explanation/security.md) — README oficial do lxc/incus apresentando a arquitetura unificada para containers de sistema e VMs, histórico comunitário pós-LXD e diretrizes fundamentais de segurança; consultado em 2026-10-03.
- [Incus Official Documentation — doc/tutorial/first_steps.md (Initialization, Launching Containers & VMs, Resource Limits, Exec & Snapshots)](https://raw.githubusercontent.com/lxc/incus/main/README.md) — Tutorial oficial First Steps do Incus demonstrando grupos incus vs incus-admin, incus admin init, criação de containers e VMs, limites dinâmicos de CPU/memória/disco e snapshots; consultado em 2026-10-03.
- [Incus Official Documentation — doc/explanation/security.md (Unix Socket Access, Unprivileged Containers, Isolated IDMaps & Bridged NIC Filtering)](https://raw.githubusercontent.com/lxc/incus/main/doc/tutorial/first_steps.md) — Documentação oficial de segurança do Incus detalhando isolamento de user namespaces, security.idmap.isolated, proteção contra vazamento de cgroups e filtragem MAC/IPv4/IPv6 na bridge incusbr0; consultado em 2026-10-03.
