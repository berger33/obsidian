---
id: software.devops.tranche08.000704
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

# Kata Containers: arquivo único de configuração (configuration.toml) e seleção de hipervisores

## Em uma frase
O Kata Containers utiliza um único arquivo de configuração TOML dividido em seções para o `runtime`, o `agent` e o `hypervisor`, permitindo alternar entre múltiplos hipervisores suportados (QEMU, Cloud Hypervisor, Firecracker, Dragonball).

## Por que importa
Diferentes cargas de trabalho em Kubernetes possuem requisitos distintos de virtualização: funções serverless efêmeras priorizam inicialização ultrarrápida e mínimo footprint (Firecracker ou Dragonball), enquanto workloads corporativos complexos podem exigir hotplug amplo de dispositivos PCI, VFIO/GPUs e múltiplos recursos de hardware (QEMU ou Cloud Hypervisor). Segundo a seção `Configuration` e `Hypervisors` do README oficial do Kata Containers, toda essa parametrização é centralizada no arquivo de configuração do runtime.

## Como funciona
Quando o `containerd` invoca o shim do Kata Containers, o runtime lê o arquivo `configuration.toml` (podendo haver múltiplos arquivos `configuration-<hypervisor>.toml` no nó, cada um mapeado para uma `RuntimeClass` diferente no Kubernetes, como `kata-qemu`, `kata-clh`, `kata-fc` ou `kata-dragonball`). O arquivo contém seções específicas para: (1) o **`hypervisor`** (caminho do binário VMM, caminho do kernel guest, imagem `image` ou `initrd`, número padrão de vCPUs, memória inicial em MiB, compartilhamento de filesystem via `virtio-fs`); (2) o **`agent`** (opções de log, debug e timeouts do `kata-agent` dentro da VM); e (3) o **`runtime`** (flags de rastreamento, intercepção e cgroups no host).

## Exemplo
```bash
# Exibir o caminho do arquivo configuration.toml ativo e os diretórios padrão buscados pelo kata-runtime
kata-runtime --show-default-config-paths
kata-runtime env
```

## Limites e trade-offs
Habilitar opções de console de depuração ou logs verbosos na seção do `agent` e do `hypervisor` dentro do `configuration.toml` é valioso para troubleshooting de inicialização da VM guest, porém aumenta o tempo de boot e pode expor acesso de shell dentro da máquina virtual se `debug_console_enabled` for esquecido ativo em produção.

## Como verificar
Execute `kata-runtime env` para inspecionar o JSON/TOML resolvido com todas as configurações ativas de `[hypervisor]`, `[runtime]`, `[agent]` e `[kernel]` antes de criar um container.

## Conexões
- [[kata-componentes-principais-shimv2-runtime-rs-agent-dragonball]] — Veja também: Kata Containers: componentes principais (runtime Go, runtime-rs em Rust, agent e VMM embutido dragonball).
- [[kata-kernel-guest-osbuilder-mini-os-rootfs-initrd]] — Veja também: Kata Containers: construção de kernel guest e imagens mini-OS (rootfs e initrd) com osbuilder.
- [[kata-containers-isolamento-vms-leves-arquitetura]] — Referência cruzada direta com kata-containers-isolamento-vms-leves-arquitetura.
- [[firecracker-microvms-kvm-isolamento-serverless-multitenant]] — Referência cruzada direta com firecracker-microvms-kvm-isolamento-serverless-multitenant.

## Fontes
- [Kata Containers GitHub — README.md (Lightweight VMs, Hardware Requirements, Main & Additional Components)](https://raw.githubusercontent.com/kata-containers/kata-containers/main/README.md) — README oficial do Kata Containers (Apache-2.0) detalhando suporte a arquiteturas de 64 bits (x86_64, aarch64, ppc64le, s390x), kata-runtime check e componentes runtime, runtime-rs, agent, dragonball, osbuilder, kata-ctl e kata-deploy; consultado em 2026-10-03.
- [Kata Containers Design Documentation — Architecture & Configuration](https://github.com/kata-containers/kata-containers/blob/main/docs/design/architecture_4.0/architecture.md) — Documentação oficial de arquitetura do Kata Containers (incluindo evolução 4.0 em Rust, containerd shimv2 e configuração de hipervisores); consultado em 2026-10-03.
- [Kata Containers — Official GitHub Repository](https://github.com/kata-containers/kata-containers) — Repositório oficial Apache-2.0 do Kata Containers; consultado em 2026-10-03.
