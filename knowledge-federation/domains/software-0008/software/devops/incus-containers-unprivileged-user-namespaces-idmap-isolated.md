---
id: software.devops.tranche15.001453
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

# Incus: containers não privilegiados por padrão (`user namespaces`) e isolamento de UID/GID (`security.idmap.isolated`)

## Em uma frase
Por padrão, todos os containers criados pelo Incus são *unprivileged* (não privilegiados), operando dentro de um *user namespace* do kernel Linux onde o `UID 0` (`root`) do container é mapeado para um UID alto sem privilégios no host.

## Por que importa
Se um atacante comprometer um processo `root` dentro de um container privilegiado clássico e escapar do namespace, ele terá poderes de `root` no kernel do host; com containers não privilegiados, ele terá apenas as permissões de um usuário comum sem privilégios sobre dispositivos do host.

## Como funciona
Além do comportamento não privilegiado padrão, quando não há necessidade de compartilhamento de arquivos entre containers distintos, o administrador pode ativar `security.idmap.isolated=true` na instância para alocar faixas de UID/GID não sobrepostas exclusivas para cada container, prevenindo ataques de negação de serviço (DoS) de processos/limites entre containers.

## Exemplo
```bash
incus launch images:debian/12 secure-ct --config security.idmap.isolated=true
incus config show secure-ct
```

## Limites e trade-offs
O Incus também suporta containers privilegiados (`security.privileged=true`), mas a documentação oficial adverte que eles não são *root-safe* e nunca devem ser usados para cargas não confiáveis.

## Como verificar
Verifique o mapeamento de UID do processo init do container no host inspecionando `/proc/<pid>/uid_map` ou `incus config show <instancia>`.

## Conexões
- [[incus-grupos-acesso-incus-vs-incus-admin-seguranca-socket]] — Veja também: Incus: controle de acesso local pelos grupos `incus` vs `incus-admin` e implicações de segurança do socket Unix.
- [[incus-configuracao-limites-cpu-memory-root-disk-live-updates]] — Veja também: Incus: aplicação dinâmica de limites de CPU, memória (`limits.cpu`, `limits.memory`) e redimensionamento de disco.

## Fontes
- [Incus GitHub — README.md (System Container & Virtual Machine Manager, Linux Containers Governance, Apache-2.0 License & Security Overview)](https://raw.githubusercontent.com/lxc/incus/main/doc/explanation/security.md) — README oficial do lxc/incus apresentando a arquitetura unificada para containers de sistema e VMs, histórico comunitário pós-LXD e diretrizes fundamentais de segurança; consultado em 2026-10-03.
- [Incus Official Documentation — doc/tutorial/first_steps.md (Initialization, Launching Containers & VMs, Resource Limits, Exec & Snapshots)](https://raw.githubusercontent.com/lxc/incus/main/README.md) — Tutorial oficial First Steps do Incus demonstrando grupos incus vs incus-admin, incus admin init, criação de containers e VMs, limites dinâmicos de CPU/memória/disco e snapshots; consultado em 2026-10-03.
- [Incus Official Documentation — doc/explanation/security.md (Unix Socket Access, Unprivileged Containers, Isolated IDMaps & Bridged NIC Filtering)](https://raw.githubusercontent.com/lxc/incus/main/doc/tutorial/first_steps.md) — Documentação oficial de segurança do Incus detalhando isolamento de user namespaces, security.idmap.isolated, proteção contra vazamento de cgroups e filtragem MAC/IPv4/IPv6 na bridge incusbr0; consultado em 2026-10-03.
