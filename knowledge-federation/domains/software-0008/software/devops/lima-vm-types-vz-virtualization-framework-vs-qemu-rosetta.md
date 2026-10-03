---
id: software.devops.tranche15.001433
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

# Lima: backends de virtualização (`vz` Virtualization.framework vs `qemu`) e aceleração Rosetta 2 em Apple Silicon

## Em uma frase
No macOS, o Lima suporta dois motores principais de máquina virtual configuráveis em `vmType`: o framework nativo da Apple (`vz`, `Virtualization.framework`) e o hipervisor multiplataforma `qemu`.

## Por que importa
A escolha entre `vz` e `qemu` impacta diretamente o desempenho de I/O de disco, a velocidade de boot e a capacidade de executar binários e containers `x86_64` (`linux/amd64`) com desempenho quase nativo via Rosetta 2 em Macs com Apple Silicon.

## Como funciona
O backend `vz` utiliza o hipervisor nativo do macOS com compartilhamento de arquivos via `virtiofs` e permite habilitar o suporte a Rosetta 2 dentro da VM Linux para traduzir instruções `x86_64` em hardware ARM64. Já o backend `qemu` oferece ampla compatibilidade com arquiteturas emuladas adicionais e sistemas operacionais variados.

## Exemplo
```bash
limactl start --name=vz-vm --vm-type=vz --rosetta
limactl list vz-vm
```

## Limites e trade-offs
Certas funcionalidades de baixo nível de emulação de dispositivos ou redes legadas diferem entre `vz` e `qemu`, e o tipo da VM (`vmType`) é definido na criação da instância.

## Como verificar
Execute `limactl list --format '{{.Name}}: {{.VMType}}'` para verificar qual hipervisor está sendo utilizado por cada instância do Lima.

## Conexões
- [[lima-templates-docker-kubernetes-podman-distros-linux]] — Veja também: Lima: catálogo de templates prontos (`template:docker`, `template:k8s`, Podman e múltiplas distribuições Linux).
- [[lima-filesystem-mounts-virtiofs-reverse-sshfs-9p-writable]] — Veja também: Lima: montagem de sistemas de arquivos (`virtiofs`, `reverse-sshfs`, `9p`) e controle de escrita em diretórios do host.

## Fontes
- [Lima GitHub — README.md (Linux Virtual Machines, Automatic File Sharing & Port Forwarding, containerd/nerdctl/Docker/K8s Templates & CycloneDX SBOM)](https://lima-vm.io/docs/config/) — README oficial do lima-vm/lima (CNCF Incubating) apresentando o fluxo limactl, templates de Docker e Kubernetes, geração de SBOM CycloneDX (app vs mod) e ecossistema de adotantes; consultado em 2026-10-03.
- [Lima Official Documentation — Configuration Guide (Default Spec, VM Types VZ/QEMU, Multi-Arch, Port Forwarding, Mounts & Plain Mode)](https://raw.githubusercontent.com/lima-vm/lima/master/README.md) — Guia oficial de configuração do Lima detalhando a especificação padrão (4 vCPUs, 4 GiB RAM, 100 GiB disk), tipos de VM, montagens, redes, discos e modo plain; consultado em 2026-10-03.
- [Lima — Official GitHub Repository](https://github.com/lima-vm/lima) — Repositório oficial Apache-2.0 do Lima na CNCF; consultado em 2026-10-03.
