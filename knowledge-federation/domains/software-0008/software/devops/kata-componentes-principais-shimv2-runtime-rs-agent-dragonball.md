---
id: software.devops.tranche08.000703
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

# Kata Containers: componentes principais (runtime Go, runtime-rs em Rust, agent e VMM embutido dragonball)

## Em uma frase
O núcleo do Kata Containers compreende o `runtime` (implementação `containerd shimv2` em Go), o `runtime-rs` (versão do runtime em Rust), o processo `agent` dentro da VM/Pod e o VMM embutido opcional `dragonball`.

## Por que importa
Na evolução do Kata Containers 2.0+ (e arquitetura 4.0), unificar o ciclo de vida do Pod em um único processo `shimv2` e oferecer um runtime escrito em Rust com um Virtual Machine Monitor (VMM) integrado reduziu drasticamente o consumo de memória, o número de processos por Pod e a latência de inicialização. A tabela `Main components` do README oficial do Kata Containers descreve o papel de cada um desses componentes centrais.

## Como funciona
(1) **`runtime` (`src/runtime`)**: componente principal invocado pelo gerenciador de containers (`containerd`), fornecendo a implementação `containerd shimv2` em Go; (2) **`runtime-rs` (`src/runtime-rs`)**: implementação moderna do runtime escrita em Rust, projetada para segurança de memória e menor pegada de recursos; (3) **`agent` (`src/agent`)**: processo de gerenciamento (escrito em Rust) que roda dentro da máquina virtual convidada (guest VM / Pod) e configura namespaces, cgroups e processos dos containers solicitados pelo runtime; e (4) **`dragonball` (`src/dragonball`)**: um VMM (Virtual Machine Monitor) integrado e opcional que roda na mesma memória do `runtime-rs`, proporcionando uma experiência out-of-the-box do Kata Containers com otimizações específicas para workloads de containers sem precisar lançar um processo VMM externo separado.

## Exemplo
```bash
# Inspecionar os binários instalados do runtime Kata (containerd-shim-kata-v2) no nó Linux
which containerd-shim-kata-v2 kata-runtime
containerd-shim-kata-v2 -v
```

## Limites e trade-offs
Enquanto o `runtime` tradicional em Go (`containerd-shim-kata-v2`) comunica-se com processos hipervisores externos (como QEMU, Cloud Hypervisor ou Firecracker), o uso do `dragonball` acoplado ao `runtime-rs` elimina a fronteira de processo entre o shim e o VMM para máxima eficiência, mas restringe as opções de dispositivos virtuais às funcionalidades suportadas pelo motor `dragonball`.

## Como verificar
Verifique a versão e os caminhos configurados do `containerd-shim-kata-v2` (ou `runtime-rs`) e confirme nos processos do host durante a execução de um Pod que um único shim gerencia a VM inteira do Pod.

## Conexões
- [[kata-requisitos-hardware-arquiteturas-kata-runtime-check]] — Veja também: Kata Containers: suporte multi-arquitetura de virtualização e diagnóstico com kata-runtime check.
- [[kata-hipervisores-configuracao-runtime-agent]] — Veja também: Kata Containers: arquivo único de configuração (configuration.toml) e seleção de hipervisores.
- [[kata-containers-isolamento-vms-leves-arquitetura]] — Referência cruzada direta com kata-containers-isolamento-vms-leves-arquitetura.
- [[kata-kernel-guest-osbuilder-mini-os-rootfs-initrd]] — Referência cruzada direta com kata-kernel-guest-osbuilder-mini-os-rootfs-initrd.

## Fontes
- [Kata Containers GitHub — README.md (Lightweight VMs, Hardware Requirements, Main & Additional Components)](https://raw.githubusercontent.com/kata-containers/kata-containers/main/README.md) — README oficial do Kata Containers (Apache-2.0) detalhando suporte a arquiteturas de 64 bits (x86_64, aarch64, ppc64le, s390x), kata-runtime check e componentes runtime, runtime-rs, agent, dragonball, osbuilder, kata-ctl e kata-deploy; consultado em 2026-10-03.
- [Kata Containers Design Documentation — Architecture & Configuration](https://github.com/kata-containers/kata-containers/blob/main/docs/design/architecture_4.0/architecture.md) — Documentação oficial de arquitetura do Kata Containers (incluindo evolução 4.0 em Rust, containerd shimv2 e configuração de hipervisores); consultado em 2026-10-03.
- [Kata Containers — Official GitHub Repository](https://github.com/kata-containers/kata-containers) — Repositório oficial Apache-2.0 do Kata Containers; consultado em 2026-10-03.
