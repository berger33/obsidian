---
id: software.devops.tranche15.001434
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
fontes: ["https://lima-vm.io/docs/config/", "https://raw.githubusercontent.com/lima-vm/lima/master/README.md", "https://github.com/lima-vm/lima"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Lima: montagem de sistemas de arquivos (`virtiofs`, `reverse-sshfs`, `9p`) e controle de escrita em diretórios do host

## Em uma frase
O Lima compartilha diretórios entre o host e a máquina virtual Linux por meio da seção `mounts` do arquivo YAML da instância, suportando os drivers `virtiofs`, `reverse-sshfs` e `9p`.

## Por que importa
Para que containers com bind mounts (`-v $(pwd):/app`) editem arquivos de código-fonte gerados dentro da VM e reflitam as alterações na IDE do host, é preciso configurar explicitamente quais diretórios possuem `writable: true`.

## Como funciona
Por padrão, o Lima monta `~` em modo somente leitura (`writable: false`). O desenvolvedor pode liberar escrita apenas na pasta de projetos (`~/projects`) via flag `--mount-writable` ou declarando entradas em `mounts:` no YAML da instância, utilizando `virtiofs` (padrão de alta performance no `vz`) ou `reverse-sshfs`/`9p`.

## Exemplo
```yaml
mounts:
  - location: "~"
    writable: false
  - location: "~/workspace"
    writable: true
```

## Limites e trade-offs
O ponto de montagem gravável legado `/tmp/lima` foi removido a partir do Lima `v2.0`; projetos que dependem de escrita compartilhada devem declarar explicitamente os diretórios de trabalho com `writable: true`.

## Como verificar
Dentro da VM (`lima`), execute `mount | grep -E "virtiofs|fuse|9p"` para inspecionar os diretórios montados e suas flags `ro`/`rw`.

## Conexões
- [[lima-vm-types-vz-virtualization-framework-vs-qemu-rosetta]] — Veja também: Lima: backends de virtualização (`vz` Virtualization.framework vs `qemu`) e aceleração Rosetta 2 em Apple Silicon.
- [[lima-port-forwarding-automatico-guest-agent-regras-portforwards]] — Veja também: Lima: encaminhamento automático de portas (`portForwards`) entre a VM Linux e o localhost da máquina host.

## Fontes
- [Lima GitHub — README.md (Linux Virtual Machines, Automatic File Sharing & Port Forwarding, containerd/nerdctl/Docker/K8s Templates & CycloneDX SBOM)](https://lima-vm.io/docs/config/) — README oficial do lima-vm/lima (CNCF Incubating) apresentando o fluxo limactl, templates de Docker e Kubernetes, geração de SBOM CycloneDX (app vs mod) e ecossistema de adotantes; consultado em 2026-10-03.
- [Lima Official Documentation — Configuration Guide (Default Spec, VM Types VZ/QEMU, Multi-Arch, Port Forwarding, Mounts & Plain Mode)](https://raw.githubusercontent.com/lima-vm/lima/master/README.md) — Guia oficial de configuração do Lima detalhando a especificação padrão (4 vCPUs, 4 GiB RAM, 100 GiB disk), tipos de VM, montagens, redes, discos e modo plain; consultado em 2026-10-03.
- [Lima — Official GitHub Repository](https://github.com/lima-vm/lima) — Repositório oficial Apache-2.0 do Lima na CNCF; consultado em 2026-10-03.
