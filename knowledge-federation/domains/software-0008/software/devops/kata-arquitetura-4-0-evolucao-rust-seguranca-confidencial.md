---
id: software.devops.tranche08.000709
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

# Kata Containers: evolução para a Arquitetura 4.0, unificação em Rust e isolamento de workloads

## Em uma frase
A documentação de design do Kata Containers (incluindo a visão geral da Arquitetura 4.0 em `docs/design/architecture_4.0/architecture.md`) consolida a transição dos componentes críticos (`runtime-rs`, `kata-agent`, `dragonball`) para Rust com foco em segurança de memória, baixo overhead e suporte a computação confidencial.

## Por que importa
Em ambientes multi-tenant hostis e nuvens públicas, o próprio software que gerencia a máquina virtual no host (o shim e o hipervisor) faz parte da base computacional confiável (TCB); reescrever esses componentes em Rust e otimizar a comunicação host-guest reduz vulnerabilidades de corrupção de memória e prepara o caminho para Confidential Containers (TEE). O README oficial do Kata Containers destaca os documentos de design da arquitetura clássica e da Arquitetura 4.0.

## Como funciona
Na evolução arquitetural do Kata Containers, em vez de lançar múltiplos processos auxiliares por container (como ocorria no Kata 1.x com `kata-shim`, `kata-proxy` e `kata-runtime` separados), a arquitetura moderna utiliza um único processo `containerd-shim-kata-v2` por Pod Kubernetes. Com o `runtime-rs` e o `kata-agent` escritos em Rust, o gerenciamento de ciclo de vida OCI, o compartilhamento de diretórios de imagens, a multiplexação sobre `vsock` e o acionamento de hipervisores (ou do VMM interno `dragonball`) ocorrem com tipagem forte e segurança de memória em todas as plataformas de 64 bits suportadas (`x86_64`, `aarch64`, `ppc64le` e `s390x`).

## Exemplo
```bash
# Inspecionar na árvore de processos do host que o Pod Kata é representado pelo processo containerd-shim-kata-v2
ps -ef | grep containerd-shim-kata-v2
```

## Limites e trade-offs
Como todos os containers pertencentes ao mesmo Pod Kubernetes compartilham a mesma máquina virtual leve (o mesmo sandbox Kata, kernel guest e instância do `kata-agent`), containers dentro do **mesmo** Pod compartilham o kernel convidado entre si; portanto, cargas de trabalho de tenants diferentes com níveis de confiança distintos devem sempre ser alocadas em Pods separados (cada um em sua própria VM Kata).

## Como verificar
Crie um Pod com dois containers usando `runtimeClassName: kata-qemu` e verifique no host que apenas uma única instância de máquina virtual foi iniciada para atender ambos os containers do Pod.

## Conexões
- [[kata-webhook-admissao-mutacao-pods-runtimeclass]] — Veja também: Kata Containers: mutating admission webhook (kata-webhook) para injeção transparente de RuntimeClass em Pods.
- [[kata-ci-testes-integracao-openshift-governanca-seguranca]] — Veja também: Kata Containers: suíte de testes de integração, pipelines OpenShift CI, governança comunitária e divulgação de segurança.
- [[kata-containers-isolamento-vms-leves-arquitetura]] — Referência cruzada direta com kata-containers-isolamento-vms-leves-arquitetura.
- [[kata-componentes-principais-shimv2-runtime-rs-agent-dragonball]] — Referência cruzada direta com kata-componentes-principais-shimv2-runtime-rs-agent-dragonball.
- [[youki-runtime-oci-rust-seguranca-memoria]] — Referência cruzada direta com youki-runtime-oci-rust-seguranca-memoria.

## Fontes
- [Kata Containers GitHub — README.md (Lightweight VMs, Hardware Requirements, Main & Additional Components)](https://raw.githubusercontent.com/kata-containers/kata-containers/main/README.md) — README oficial do Kata Containers (Apache-2.0) detalhando suporte a arquiteturas de 64 bits (x86_64, aarch64, ppc64le, s390x), kata-runtime check e componentes runtime, runtime-rs, agent, dragonball, osbuilder, kata-ctl e kata-deploy; consultado em 2026-10-03.
- [Kata Containers Design Documentation — Architecture & Configuration](https://github.com/kata-containers/kata-containers/blob/main/docs/design/architecture_4.0/architecture.md) — Documentação oficial de arquitetura do Kata Containers (incluindo evolução 4.0 em Rust, containerd shimv2 e configuração de hipervisores); consultado em 2026-10-03.
- [Kata Containers — Official GitHub Repository](https://github.com/kata-containers/kata-containers) — Repositório oficial Apache-2.0 do Kata Containers; consultado em 2026-10-03.
