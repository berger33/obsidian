---
id: software.seguranca.tranche03.000225
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

# Tracee Assinaturas de Segurança Embutidas: detecção de execução *Fileless* (`mem_prot_alert`), *Rootkits* (` hooked_syscall`), `anti_debugging` e Escape

## Em uma frase
Conforme destacado em `docs/docs/overview.md` (*Security events with pre-built threat detection signatures*), o Tracee inclui dezenas de eventos de detecção de ameaças prontos para uso que correlacionam hooks LSM/kprobes internos do kernel para detectar técnicas avançadas de pós-exploração e evasão.

## Por que importa
Malwares modernos em Linux evitam gravar binários no disco (*fileless malware*): eles alocam uma região de memória anônima via `memfd_create` ou `mmap` com `PROT_WRITE`, copiam o shellcode para a RAM e mudam a permissão para `PROT_EXEC` (`mprotect`), ou sequestram a tabela de chamadas de sistema do kernel (*syscall hooking*) e `LD_PRELOAD`.

## Como funciona
Ativando eventos de segurança embutidos do Tracee como **`mem_prot_alert`**, **`fileless_execution`**, **`dropped_executable`**, **`dynamic_code_loading`**, **`ld_preload`**, **`hooked_syscall`**, **`hidden_kernel_module`**, **`docker_abuse`** e **`k8s_service_account_token`**, você detecta essas técnicas imediatamente sem precisar escrever a lógica de baixo nível!

## Exemplo
```yaml
type: policy
name: runtime-advanced-threat-detection
description: Habilita assinaturas embutidas de detecção de malware fileless, rootkits e container escape
scope:
  - global
rules:
  - event: fileless_execution
  - event: mem_prot_alert
  - event: dropped_executable
  - event: ld_preload
  - event: hooked_syscall
  - event: hidden_kernel_module
```

## Limites e trade-offs
Como no Tracee *tudo é um evento*, você pode aplicar a mesma sintaxe de `scope` e `filters` tanto em uma chamada de sistema bruta (`execve`) quanto em uma assinatura de alto nível (`fileless_execution`).

## Como verificar
Execute `tracee list` para explorar todas as assinaturas de segurança embutidas e suas descrições.

## Conexões
- [[tracee-event-filters-data-args-retval-context-operators-prefix-suffix]] — Veja também: Tracee Filtros de Eventos (`rules[].filters`): operadores sobre `data.*`, `retval`, `uid`, `comm` e wildcards `*` de prefixo/sufixo.
- [[tracee-forensic-capture-artifacts-executables-memory-pcap-files]] — Veja também: Tracee Captura Forense Automática (`--capture` / `output.artifacts`): coleta de binários executados, dumps de memória, arquivos e `PCAP`.

## Fontes
- [Aqua Security Tracee Official Documentation — Overview (Everything is an Event Architecture, 400+ Syscalls, Built-in Signatures, Forensic Capture & Security Model)](https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/overview.md) — Visão geral oficial da documentação do Tracee detalhando o pipeline unificado de eventos, assinaturas de detecção embutidas, coleta forense e modelo de ameaças; consultado em 2026-10-03.
- [Aqua Security Tracee Official Documentation — Policies Reference (Kubernetes CRD v1beta1 vs Plain Format, 64 Policies, Scopes & Event Filters)](https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/policies/index.md) — Referência oficial de políticas do Tracee explicando a intercambiabilidade entre o formato CRD Kubernetes e Plain YAML, escopos e filtros; consultado em 2026-10-03.
- [Aqua Security Tracee — Official GitHub Repository](https://github.com/aquasecurity/tracee) — Repositório oficial Apache-2.0 do Aqua Security Tracee; consultado em 2026-10-03.
