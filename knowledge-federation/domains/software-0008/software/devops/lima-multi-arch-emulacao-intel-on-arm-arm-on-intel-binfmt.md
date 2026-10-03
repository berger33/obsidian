---
id: software.devops.tranche15.001436
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

# Lima: execução multi-arquitetura (Intel-on-ARM, ARM-on-Intel) e emulação transparente via QEMU/binfmt

## Em uma frase
O Lima suporta tanto a criação de máquinas virtuais completas de arquitetura cruzada (`arch: "x86_64"` em host ARM64 ou `arch: "aarch64"` em host x86_64) quanto a emulação de binários e containers estrangeiros via `binfmt_misc` dentro de uma VM nativa.

## Por que importa
Equipes que desenvolvem em laptops Apple Silicon (`aarch64`) mas implantam em servidores `x86_64` (ou vice-versa) precisam testar imagens e pacotes de ambas as arquiteturas sem manter duas máquinas físicas.

## Como funciona
Para máxima performance, recomenda-se rodar uma VM com a arquitetura nativa da CPU do host e usar Rosetta 2 (em Apple Silicon com `vz`) ou QEMU user-mode (`binfmt_misc`) para containers de outra arquitetura; quando é necessário testar um kernel ou sistema inteiro de outra arquitetura, `limactl start --arch=x86_64` instancia a VM via emulação de sistema do QEMU.

## Exemplo
```bash
lima nerdctl run --rm --platform=linux/amd64 alpine uname -m
lima nerdctl run --rm --platform=linux/arm64 alpine uname -m
```

## Limites e trade-offs
Rodar uma VM inteira emulada com `arch` diferente da CPU física do host via QEMU system emulation é substancialmente mais lento do que rodar uma VM nativa com Rosetta 2 ou QEMU user-mode para containers individuais.

## Como verificar
Verifique a arquitetura da VM com `lima uname -m` e a capacidade de executar containers de outra plataforma com `lima nerdctl run --rm --platform=linux/amd64 alpine arch`.

## Conexões
- [[lima-port-forwarding-automatico-guest-agent-regras-portforwards]] — Veja também: Lima: encaminhamento automático de portas (`portForwards`) entre a VM Linux e o localhost da máquina host.
- [[lima-redes-user-v2-socket-vmnet-bridged-comunicacao-vms]] — Veja também: Lima: modos de rede (`user-v2`, `socket_vmnet`, `vzNAT`) e comunicação direta entre múltiplas VMs.

## Fontes
- [Lima GitHub — README.md (Linux Virtual Machines, Automatic File Sharing & Port Forwarding, containerd/nerdctl/Docker/K8s Templates & CycloneDX SBOM)](https://lima-vm.io/docs/config/) — README oficial do lima-vm/lima (CNCF Incubating) apresentando o fluxo limactl, templates de Docker e Kubernetes, geração de SBOM CycloneDX (app vs mod) e ecossistema de adotantes; consultado em 2026-10-03.
- [Lima Official Documentation — Configuration Guide (Default Spec, VM Types VZ/QEMU, Multi-Arch, Port Forwarding, Mounts & Plain Mode)](https://raw.githubusercontent.com/lima-vm/lima/master/README.md) — Guia oficial de configuração do Lima detalhando a especificação padrão (4 vCPUs, 4 GiB RAM, 100 GiB disk), tipos de VM, montagens, redes, discos e modo plain; consultado em 2026-10-03.
- [Lima — Official GitHub Repository](https://github.com/lima-vm/lima) — Repositório oficial Apache-2.0 do Lima na CNCF; consultado em 2026-10-03.
