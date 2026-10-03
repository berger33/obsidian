---
id: software.devops.tranche08.000717
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
fontes: ["https://raw.githubusercontent.com/firecracker-microvm/firecracker/main/README.md", "https://github.com/firecracker-microvm/firecracker/blob/main/docs/design.md", "https://github.com/firecracker-microvm/firecracker"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# AWS Firecracker: matriz de plataformas bare-metal testadas (Intel, AMD, ARM Graviton) e requisitos de kernel

## Em uma frase
O projeto Firecracker testa continuamente todas as combinações de instâncias bare-metal Intel (Cascade Lake a Granite Rapids), AMD (Milan e Genoa) e ARM (Graviton 2 a Graviton 5) com kernels host/guest Linux `5.10`, `6.1` e `6.18` e rootfs Ubuntu 24.04.

## Por que importa
Como um VMM depende diretamente do comportamento de virtualização assistida por hardware (Intel VT-x, AMD-V, ARMv8/v9 Virtualization Extensions) e da ABI do módulo KVM no kernel Linux hospedeiro, escolher uma combinação de CPU e versão de kernel host incompatível pode causar instabilidade ou degradação severa. A tabela `Tested platforms` e a seção `Known issues and Limitations` do README oficial do Firecracker documentam exatamente o que é validado em CI e suas restrições conhecidas.

## Como funciona
A matriz oficial de testes contínuos do Firecracker valida instâncias EC2 `.metal` de três famílias de arquiteturas: (1) **Intel**: `m5n.metal` (Cascade Lake), `m6i.metal` (Ice Lake), `m7i.metal-24xl/48xl` (Sapphire Rapids) e `m8i.metal-48xl/96xl` (Granite Rapids); (2) **AMD**: `m6a.metal` (Milan) e `m7a.metal-48xl` (Genoa); e (3) **ARM64 AWS Graviton**: `m6g.metal` (Graviton 2), `m7g.metal` (Graviton 3), `m8g.metal-24xl/48xl` (Graviton 4) e `m9g.metal-48xl` (Graviton 5), combinadas com Host OS Amazon Linux 2 (`linux_5.10`) e Amazon Linux 2023 (`linux_6.1` e `linux_6.18`), Guest Rootfs `ubuntu 24.04` e Guest Kernels `5.10` e `6.1`.

## Exemplo
```bash
# Verificar no servidor bare-metal o modelo da CPU, arquitetura e versão do kernel host para alinhamento com a matriz
uname -m -r
lscpu | grep -E "Architecture|Model name|Virtualization"
```

## Limites e trade-offs
O README oficial destaca duas restrições técnicas importantes: (1) instâncias Intel de 8ª geração (`*8i`, Granite Rapids, como `m8i.metal-48xl` e `m8i.metal-96xl`) são suportadas **exclusivamente** usando um kernel host `6.1` ou `6.18`, devido ao suporte deficiente a CPUs Granite Rapids no kernel `5.10`; e (2) na arquitetura `aarch64` (ARM64), o dispositivo de relógio de tempo real `pl031` RTC não suporta interrupções, de modo que programas convidados que dependem de alarme RTC (como `hwclock`) não funcionarão.

## Como verificar
Em servidores Intel Granite Rapids (`m8i.metal`) ou ARM64 (`aarch64`), valide com `uname -r` que o kernel do host é `6.1` ou `6.18` e evite depender de interrupções de alarme RTC em workloads `aarch64`.

## Conexões
- [[firecracker-demand-fault-paging-oversubscription-cpu-memoria]] — Veja também: AWS Firecracker: paginação sob demanda (demand fault paging) e oversubscription de CPU e memória.
- [[firecracker-especificacao-performance-logging-metricas]] — Veja também: AWS Firecracker: especificação de performance verificada em CI e sistema de logging e métricas via API.
- [[firecracker-microvms-kvm-isolamento-serverless-multitenant]] — Referência cruzada direta com firecracker-microvms-kvm-isolamento-serverless-multitenant.
- [[kata-requisitos-hardware-arquiteturas-kata-runtime-check]] — Referência cruzada direta com kata-requisitos-hardware-arquiteturas-kata-runtime-check.

## Fontes
- [AWS Firecracker GitHub — README.md (MicroVM VMM, OpenAPI Socket, Rate Limiters, Jailer & Tested Platforms)](https://raw.githubusercontent.com/firecracker-microvm/firecracker/main/README.md) — README oficial do AWS Firecracker (Apache-2.0) documentando capacidades da API REST sobre socket UNIX, CPU templates, rate limiters virtio, demand fault paging, processo jailer, seccomp por thread e matriz de plataformas Intel/AMD/Graviton; consultado em 2026-10-03.
- [AWS Firecracker Documentation — Design, Specification & Production Host Setup](https://github.com/firecracker-microvm/firecracker/blob/main/docs/design.md) — Documentação oficial de design, compromissos de performance (SPECIFICATION.md) e endurecimento de host Linux (prod-host-setup.md) do Firecracker; consultado em 2026-10-03.
- [AWS Firecracker — Official GitHub Repository](https://github.com/firecracker-microvm/firecracker) — Repositório oficial do VMM Firecracker mantido pela AWS; consultado em 2026-10-03.
