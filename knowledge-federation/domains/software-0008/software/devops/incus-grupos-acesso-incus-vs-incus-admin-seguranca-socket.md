---
id: software.devops.tranche15.001452
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

# Incus: controle de acesso local pelos grupos `incus` vs `incus-admin` e implicações de segurança do socket Unix

## Em uma frase
O daemon do Incus executa como `root` e controla o acesso local ao seu socket Unix por meio de dois grupos distintos do sistema operacional: o grupo restrito `incus` e o grupo administrativo completo `incus-admin`.

## Por que importa
Compreender a fronteira de segurança entre esses dois grupos é vital: qualquer usuário com acesso irrestrito ao socket administrativo do Incus (`incus-admin`) pode montar diretórios arbitrários do host (`/` ou `/etc`) dentro de uma instância e obter privilégio equivalente a `root` na máquina física.

## Como funciona
Usuários adicionados ao grupo `incus` recebem acesso básico isolado em um projeto individual por usuário, sem permissão para alterar configurações globais do daemon ou anexar recursos sensíveis do host. Já membros de `incus-admin` possuem controle total sobre todas as instâncias, redes e pools de armazenamento do servidor.

## Exemplo
```bash
sudo adduser "$USER" incus-admin
id
incus project list
```

## Limites e trade-offs
Nunca adicione usuários não confiáveis ao grupo `incus-admin`: a documentação oficial de segurança alerta explicitamente que o acesso completo ao socket Unix do Incus equivale a conceder acesso `root` direto ao sistema hospedeiro.

## Como verificar
Audite os membros do grupo administrativo no servidor Linux executando `getent group incus-admin` e `getent group incus`.

## Conexões
- [[incus-arquitetura-system-containers-lxc-vms-qemu-rest-api]] — Veja também: Linux Containers Incus: gerenciador unificado de containers de sistema (LXC) e máquinas virtuais (QEMU).
- [[incus-containers-unprivileged-user-namespaces-idmap-isolated]] — Veja também: Incus: containers não privilegiados por padrão (`user namespaces`) e isolamento de UID/GID (`security.idmap.isolated`).

## Fontes
- [Incus GitHub — README.md (System Container & Virtual Machine Manager, Linux Containers Governance, Apache-2.0 License & Security Overview)](https://raw.githubusercontent.com/lxc/incus/main/doc/explanation/security.md) — README oficial do lxc/incus apresentando a arquitetura unificada para containers de sistema e VMs, histórico comunitário pós-LXD e diretrizes fundamentais de segurança; consultado em 2026-10-03.
- [Incus Official Documentation — doc/tutorial/first_steps.md (Initialization, Launching Containers & VMs, Resource Limits, Exec & Snapshots)](https://raw.githubusercontent.com/lxc/incus/main/doc/tutorial/first_steps.md) — Tutorial oficial First Steps do Incus demonstrando grupos incus vs incus-admin, incus admin init, criação de containers e VMs, limites dinâmicos de CPU/memória/disco e snapshots; consultado em 2026-10-03.
- [Incus Official Documentation — doc/explanation/security.md (Unix Socket Access, Unprivileged Containers, Isolated IDMaps & Bridged NIC Filtering)](https://raw.githubusercontent.com/lxc/incus/main/README.md) — Documentação oficial de segurança do Incus detalhando isolamento de user namespaces, security.idmap.isolated, proteção contra vazamento de cgroups e filtragem MAC/IPv4/IPv6 na bridge incusbr0; consultado em 2026-10-03.
