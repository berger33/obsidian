---
id: software.seguranca.tranche03.000230
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/overview.md", "https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/policies/index.md", "https://github.com/aquasecurity/tracee"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Tracee Modelo de Ameaças e Segurança (*Security Model*): resistência contra adversários em *userspace* e detecção de ameaças em *kernel*

## Em uma frase
Conforme destacado na seção *Clear Security Model* de `docs/docs/overview.md`, o Tracee documenta com transparência suas garantias e fronteiras de segurança frente a dois níveis de adversários: **forte proteção contra adversários em espaço de usuário (*userspace*)** e **detecção *best-effort* de ameaças no nível do kernel (*rootkits*)**.

## Por que importa
Agentes que dependem de injeção de biblioteca em espaço de usuário (`LD_PRELOAD` ou `ptrace`) são facilmente contornados por binários compilados estaticamente em Go/Rust/C que invocam a instrução assembly `syscall` diretamente.

## Como funciona
Como os coletores do Tracee rodam **dentro do kernel Linux via eBPF**, um invasor em espaço de usuário dentro de um container (mesmo sendo `root` dentro do container sem privilégios de kernel) **não consegue desativar nem fazer bypass** dos probes eBPF anexados às syscalls e LSM hooks! Já caso o invasor obtenha execução de código no próprio ring 0 do kernel (via módulo de kernel malicioso ou exploit de kernel), o Tracee oferece assinaturas dedicadas de detecção de rootkits (`hooked_syscall`, `hidden_kernel_module`, `fops_hooking`, `proc_fops_hooking`).

## Exemplo
```yaml
type: policy
name: kernel-integrity-and-rootkit-monitoring
description: Monitora carregamento de módulos de kernel, programas eBPF suspeitos e hooking de tabelas do kernel
scope:
  - global
rules:
  - event: init_module
  - event: hooked_syscall
  - event: hidden_kernel_module
  - event: fops_hooking
  - event: bpf_attach
```

## Limites e trade-offs
Para impedir que um container comprometido interfira no próprio processo `tracee` no host, execute o Tracee em um namespace dedicado (`tracee-system`) com `PodSecurityStandard: privileged` restrito apenas a esse namespace e bloqueie o carregamento de módulos de kernel não assinados (`kernel.modules_disabled=1`) nos nós.

## Como verificar
Audite eventos `bpf_attach` e `init_module` em produção para monitorar qualquer novo programa eBPF ou módulo carregado nos nós.

## Conexões
- [[tracee-implantacao-kubernetes-helm-daemonset-postee-webhook-siem]] — Veja também: Tracee em Kubernetes: implantação via Helm DaemonSet, CRDs `Policy` (`tracee.aquasec.com/v1beta1`) e roteamento de saída (`json`, `webhook`, `forward`).

## Fontes
- [Aqua Security Tracee Official Documentation — Overview (Everything is an Event Architecture, 400+ Syscalls, Built-in Signatures, Forensic Capture & Security Model)](https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/overview.md) — Visão geral oficial da documentação do Tracee detalhando o pipeline unificado de eventos, assinaturas de detecção embutidas, coleta forense e modelo de ameaças; consultado em 2026-10-03.
- [Aqua Security Tracee Official Documentation — Policies Reference (Kubernetes CRD v1beta1 vs Plain Format, 64 Policies, Scopes & Event Filters)](https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/policies/index.md) — Referência oficial de políticas do Tracee explicando a intercambiabilidade entre o formato CRD Kubernetes e Plain YAML, escopos e filtros; consultado em 2026-10-03.
- [Aqua Security Tracee — Official GitHub Repository](https://github.com/aquasecurity/tracee) — Repositório oficial Apache-2.0 do Aqua Security Tracee; consultado em 2026-10-03.
