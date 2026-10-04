---
id: software.devops.tranche08.000705
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/kata-containers/kata-containers/main/README.md", "https://github.com/kata-containers/kata-containers/blob/main/docs/design/architecture_4.0/architecture.md", "https://github.com/kata-containers/kata-containers"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kata Containers: construção de kernel guest e imagens mini-OS (rootfs e initrd) com osbuilder

## Em uma frase
O Kata Containers inclui a ferramenta de infraestrutura `osbuilder` (`tools/osbuilder`) e patches dedicados de kernel (`tools/packaging/kernel`) para construir o kernel Linux guest e imagens enxutas de `rootfs` ou `initrd` que inicializam a VM do Pod.

## Por que importa
Usar uma imagem de sistema operacional de servidor Linux genérica (com centenas de megabytes de pacotes, serviços systemd desnecessários e drivers legados) para dar boot na máquina virtual de cada Pod inviabilizaria a velocidade e a densidade de memória dos Kata Containers. Conforme a tabela `Additional components` do README oficial do Kata Containers, o `osbuilder` e a árvore de kernel otimizada geram um ambiente guest mínimo contendo apenas o necessário para rodar o `kata-agent`.

## Como funciona
O componente **`kernel`** (`tools/packaging/kernel`) mantém as configurações enxutas e patches aplicados ao kernel Linux oficial para acelerar o boot dentro do hipervisor e habilitar recursos como `virtio-fs`, `vsock` e hotplug de memória/CPU. Já a ferramenta **`osbuilder`** (`tools/osbuilder`) constrói uma imagem de "mini O/S" contendo o binário `kata-agent` (frequentemente configurado como o próprio processo `init` da VM para eliminar sobrecarga de inicialização), podendo empacotá-la em dois formatos: (1) uma imagem **`rootfs`** (sistema de arquivos bruto mapeado na VM via `pmem`/`nvdimm` ou dispositivo de bloco Com DAX para economizar RAM compartilhando páginas); ou (2) um arquivo **`initrd`** (initial ramdisk comprimido carregado diretamente em memória pelo hipervisor).

## Exemplo
```bash
# Verificar na saída de kata-runtime env qual kernel guest e qual imagem (rootfs ou initrd) estão configurados
kata-runtime env | grep -A 6 -E "^\[(Kernel|Image|Initrd)\]"
```

## Limites e trade-offs
O uso de uma imagem `initrd` simplifica o boot em hipervisores ou arquiteturas que não suportam mapeamento DAX/NVDIMM, mas consome memória RAM adicional em cada VM guest porque o ramdisk é descompactado na memória da VM; já o uso de imagem `rootfs` com DAX permite mapear o sistema de arquivos convidado diretamente da memória do host sem duplicar cache de páginas.

## Como verificar
Inspecione os arquivos de kernel (`vmlinux*` ou `vmlinuz*`) e de imagem (`kata-containers.img` ou `kata-containers-initrd.img`) instalados em `/opt/kata/share/kata-containers/` (ou caminho listado em `kata-runtime env`).

## Conexões
- [[kata-hipervisores-configuracao-runtime-agent]] — Veja também: Kata Containers: arquivo único de configuração (configuration.toml) e seleção de hipervisores.
- [[kata-packaging-kata-deploy-helm-kubernetes-runtimeclass]] — Veja também: Kata Containers: empacotamento de binários e implantação em Kubernetes com o Helm chart kata-deploy e RuntimeClass.
- [[kata-containers-isolamento-vms-leves-arquitetura]] — Referência cruzada direta com kata-containers-isolamento-vms-leves-arquitetura.
- [[kata-componentes-principais-shimv2-runtime-rs-agent-dragonball]] — Referência cruzada direta com kata-componentes-principais-shimv2-runtime-rs-agent-dragonball.

## Fontes
- [Kata Containers GitHub — README.md (Lightweight VMs, Hardware Requirements, Main & Additional Components)](https://raw.githubusercontent.com/kata-containers/kata-containers/main/README.md) — README oficial do Kata Containers (Apache-2.0) detalhando suporte a arquiteturas de 64 bits (x86_64, aarch64, ppc64le, s390x), kata-runtime check e componentes runtime, runtime-rs, agent, dragonball, osbuilder, kata-ctl e kata-deploy; consultado em 2026-10-03.
- [Kata Containers Design Documentation — Architecture & Configuration](https://github.com/kata-containers/kata-containers/blob/main/docs/design/architecture_4.0/architecture.md) — Documentação oficial de arquitetura do Kata Containers (incluindo evolução 4.0 em Rust, containerd shimv2 e configuração de hipervisores); consultado em 2026-10-03.
- [Kata Containers — Official GitHub Repository](https://github.com/kata-containers/kata-containers) — Repositório oficial Apache-2.0 do Kata Containers; consultado em 2026-10-03.
