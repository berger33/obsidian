---
id: software.devops.tranche20.001905
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

# LinuxKit Formatos de Saída (`linuxkit build --format`): geração de imagens para `iso-efi`, `raw-bios`, `qcow2`, `vhd`, AWS, GCP e Raspberry Pi

## Em uma frase
A partir do mesmo arquivo declarativo `linuxkit.yml`, a flag **`--format`** do comando `linuxkit build` compila artefatos de boot específicos para hipervisores locais, nuvens públicas e servidores bare-metal (incluindo `kernel+initrd`, `iso-bios`, `iso-efi`, `raw-bios`, `raw-efi`, `qcow2-bios`, `qcow2-efi`, `vhd`, `vmdk`, `aws`, `gcp` e `rpi3`).

## Por que importa
Manter pipelines de Packer separadas com scripts Kickstart/Preseed distintos para VMware on-premises, QEMU/KVM, AWS EC2, Google Compute Engine, Microsoft Azure e bare-metal Equinix Metal gera divergência entre os sistemas operacionais homologados e os de produção.

## Como funciona
No LinuxKit, a definição lógica dos containers de sistema no YAML permanece a mesma; basta variar `--format` na linha de comando para empacotar a árvore raiz e o kernel no formato exigido pelo bootloader (Syslinux/GRUB/EFI) ou hipervisor de destino.

## Exemplo
```bash
# Gerando uma ISO inicializável via UEFI e uma imagem de disco raw BIOS a partir do mesmo YAML:
linuxkit build --format iso-efi linuxkit.yml
linuxkit build --format raw-bios linuxkit.yml
```

## Limites e trade-offs
Ao compilar para bare-metal (`x86_64` ou `arm64`), lembre-se de incluir na seção `kernel:` o arquivo de microcódigo da CPU (`ucode: intel-ucode.cpio` ou equivalente AMD) para que ele seja concatenado no início do `initrd`.

## Como verificar
Execute `linuxkit build --help` para listar todos os formatos de imagem suportados pela sua versão instalada do `linuxkit`.

## Conexões
- [[linuxkit-volumes-blank-filesystem-oci-layout-readonly-mounts]] — Veja também: LinuxKit Seção `volumes`: criação em tempo de build de volumes em branco, `filesystem` populado por imagem e `format: oci`.
- [[linuxkit-run-hipervisores-locais-qemu-hyperkit-virtualization-framework-cloud]] — Veja também: LinuxKit `linuxkit run`: execução e teste de imagens em QEMU, macOS `Virtualization.Framework`, Hyper-V, VMware e Cloud.

## Fontes
- [LinuxKit GitHub — README.md (Toolkit for Building Secure, Portable and Lean Operating Systems for Containers)](https://raw.githubusercontent.com/linuxkit/linuxkit/master/README.md) — README oficial do linuxkit/linuxkit apresentando a arquitetura de imagens de SO imutáveis, formatos de saída, plataformas de execução e ferramentas; consultado em 2026-10-03.
- [LinuxKit Official Documentation — YAML Specification (docs/yaml.md: kernel, init, volumes, onboot, onshutdown, services & files)](https://raw.githubusercontent.com/linuxkit/linuxkit/master/docs/yaml.md) — Especificação oficial YAML do LinuxKit detalhando a ordem de inicialização, alocação simbólica de uid/gid, volumes OCI e configuração runtime; consultado em 2026-10-03.
- [LinuxKit — Official GitHub Repository](https://github.com/linuxkit/linuxkit) — Repositório oficial Apache-2.0 do LinuxKit; consultado em 2026-10-03.
