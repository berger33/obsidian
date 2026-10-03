---
id: software.devops.tranche20.001906
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://raw.githubusercontent.com/linuxkit/linuxkit/master/README.md", "https://raw.githubusercontent.com/linuxkit/linuxkit/master/docs/yaml.md", "https://github.com/linuxkit/linuxkit"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# LinuxKit `linuxkit run`: execução e teste de imagens em QEMU, macOS `Virtualization.Framework`, Hyper-V, VMware e Cloud

## Em uma frase
O subcomando **`linuxkit run`** inicializa e testa imediatamente a imagem construída por `linuxkit build`, selecionando automaticamente o hipervisor nativo da plataforma local (**QEMU** no Linux/macOS/Windows, **Virtualization.Framework** / **HyperKit** no macOS, **Hyper-V** no Windows ou **VMware**) ou provisionando em nuvem (**AWS**, **GCP**, **Azure**, **OpenStack**, **Equinix Metal**).

## Por que importa
Desenvolver alterações em pacotes de sistema (`init`, `sysctl`, `mount`, `sshd`, `kubelet`) sem poder inicializar a imagem completa em segundos no próprio laptop atrasaria o ciclo de depuração de sistemas operacionais imutáveis.

## Como funciona
Ao executar `linuxkit run qemu --cpus 2 --mem 2048 --disk size=4G linuxkit`, a ferramenta anexa um disco virtual de 4 GiB, inicializa o kernel e o initrd em uma VM QEMU com console serial conectado ao terminal atual, permitindo inspecionar o boot completo em poucos segundos.

## Exemplo
```bash
# Executando a imagem construída em uma VM QEMU com 2 vCPUs, 2 GiB de RAM e disco persistente:
linuxkit run qemu -cpus 2 -mem 2048 -disk file=state.img,size=4G linuxkit
```

## Limites e trade-offs
Em arquiteturas `arm64` no macOS moderno (Apple Silicon), o backend `Virtualization.Framework` do `linuxkit run` oferece aceleração nativa de hardware para imagens LinuxKit compiladas para `arm64`.

## Como verificar
Execute `linuxkit run --help` para inspecionar os backends de virtualização e nuvem disponíveis e as flags de rede, CPU, memória e discos.

## Conexões
- [[linuxkit-formatos-saida-build-iso-efi-raw-bios-qcow2-vhd-aws-gcp]] — Veja também: LinuxKit Formatos de Saída (`linuxkit build --format`): geração de imagens para `iso-efi`, `raw-bios`, `qcow2`, `vhd`, AWS, GCP e Raspberry Pi.
- [[linuxkit-pkg-construcao-pacotes-sistema-oci-reproducible-builds]] — Veja também: LinuxKit Packages (`linuxkit pkg`): construção reprodutível e multi-arquitetura de pacotes de sistema em containers.

## Fontes
- [LinuxKit GitHub — README.md (Toolkit for Building Secure, Portable and Lean Operating Systems for Containers)](https://raw.githubusercontent.com/linuxkit/linuxkit/master/README.md) — README oficial do linuxkit/linuxkit apresentando a arquitetura de imagens de SO imutáveis, formatos de saída, plataformas de execução e ferramentas; consultado em 2026-10-03.
- [LinuxKit Official Documentation — YAML Specification (docs/yaml.md: kernel, init, volumes, onboot, onshutdown, services & files)](https://raw.githubusercontent.com/linuxkit/linuxkit/master/docs/yaml.md) — Especificação oficial YAML do LinuxKit detalhando a ordem de inicialização, alocação simbólica de uid/gid, volumes OCI e configuração runtime; consultado em 2026-10-03.
- [LinuxKit — Official GitHub Repository](https://github.com/linuxkit/linuxkit) — Repositório oficial Apache-2.0 do LinuxKit; consultado em 2026-10-03.
