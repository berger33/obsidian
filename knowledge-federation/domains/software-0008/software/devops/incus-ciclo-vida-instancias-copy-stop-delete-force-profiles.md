---
id: software.devops.tranche15.001458
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

# Incus: clonagem rápida de instâncias (`incus copy`), perfis reutilizáveis e gerenciamento de ciclo de vida

## Em uma frase
O Incus permite clonar rapidamente instâncias existentes (`incus copy`), padronizar configurações em perfis compartilhados (`incus profile`) e controlar transições seguras de parada e remoção (`incus stop`, `incus delete`).

## Por que importa
Quando uma equipe prepara uma imagem base dourada com dependências instaladas em uma instância, `incus copy` permite criar dezenas de ambientes idênticos de teste em segundos aproveitando o armazenamento Copy-on-Write local.

## Como funciona
Ao executar `incus copy first third`, o Incus clona o volume raiz e a configuração da instância em estado parado (`STOPPED`), permitindo iniciá-la com `incus start third`. Por proteção contra perda acidental de dados, `incus delete` recusa-se a apagar uma instância em execução a menos que ela seja parada antes ou que a flag `--force` seja informada.

## Exemplo
```bash
incus copy app-container app-staging
incus start app-staging
incus info app-staging
incus stop app-staging
incus delete app-staging
```

## Limites e trade-offs
O perfil `default` é aplicado automaticamente a todas as instâncias que não especificam lista própria de perfis; alterações feitas em `incus profile edit default` afetam imediatamente todas as instâncias que herdam esse perfil.

## Como verificar
Execute `incus info <instancia>` para inspecionar o PID do processo init, uso de memória, tráfego de rede por interface e perfis associados.

## Conexões
- [[incus-exposicao-remota-api-tls-core-https-address-hardening]] — Veja também: Incus: exposição segura da API REST remota sobre TLS (`core.https_address`) e prevenção de vazamento de cgroups.
- [[incus-governanca-comunitaria-migracao-lxd-apache2-sem-cla]] — Veja também: Incus: governança comunitária Linux Containers, licença Apache-2.0 sem CLA e pacotes Zabbly.

## Fontes
- [Incus GitHub — README.md (System Container & Virtual Machine Manager, Linux Containers Governance, Apache-2.0 License & Security Overview)](https://raw.githubusercontent.com/lxc/incus/main/doc/tutorial/first_steps.md) — README oficial do lxc/incus apresentando a arquitetura unificada para containers de sistema e VMs, histórico comunitário pós-LXD e diretrizes fundamentais de segurança; consultado em 2026-10-03.
- [Incus Official Documentation — doc/tutorial/first_steps.md (Initialization, Launching Containers & VMs, Resource Limits, Exec & Snapshots)](https://raw.githubusercontent.com/lxc/incus/main/README.md) — Tutorial oficial First Steps do Incus demonstrando grupos incus vs incus-admin, incus admin init, criação de containers e VMs, limites dinâmicos de CPU/memória/disco e snapshots; consultado em 2026-10-03.
- [Incus Official Documentation — doc/explanation/security.md (Unix Socket Access, Unprivileged Containers, Isolated IDMaps & Bridged NIC Filtering)](https://raw.githubusercontent.com/lxc/incus/main/doc/explanation/security.md) — Documentação oficial de segurança do Incus detalhando isolamento de user namespaces, security.idmap.isolated, proteção contra vazamento de cgroups e filtragem MAC/IPv4/IPv6 na bridge incusbr0; consultado em 2026-10-03.
