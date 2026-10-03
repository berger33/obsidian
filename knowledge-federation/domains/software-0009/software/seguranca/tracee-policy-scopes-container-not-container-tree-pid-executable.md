---
id: software.seguranca.tranche03.000223
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
fontes: ["https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/policies/index.md", "https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/overview.md", "https://github.com/aquasecurity/tracee"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Tracee Escopos de Política (`scope`): filtragem no kernel por `container`, `host`, árvore de processos (`tree`), `executable` e `uid`

## Em uma frase
Na seção **`scope`** de uma política do Tracee, você restringe exatamente a quais processos ou ambientes a política se aplica usando expressões como **`global`** (todo o nó), **`container`** (apenas processos dentro de containers, ou `container=new` para containers iniciados após o Tracee), **`not-container`** (apenas processos do host Linux fora de containers), **`tree=<pid>`** (toda a árvore de processos descendentes de um PID), **`executable=<path>`** ou **`mntns`/`pidns`**!

## Por que importa
Se você quer auditar comandos administrativos executados diretamente no sistema operacional do nó worker via SSH sem ser inundado pelos milhões de chamadas dos 150 containers que rodam naquele nó, filtrar em espaço de usuário após capturar tudo desperdiça CPU.

## Como funciona
Com `scope: [not-container]` (ou `scope: [container, executable=/usr/sbin/nginx]`), o Tracee aplica os filtros de escopo diretamente nos mapas eBPF dentro do kernel, descartando eventos fora de escopo com custo próximo de zero!

## Exemplo
```yaml
type: policy
name: audit-host-only-shell-activity
description: Monitora execuções de processos apenas no host Linux (ignorando containers)
scope:
  - not-container
rules:
  - event: sched_process_exec
    filters:
      - data.pathname=/bin/bash,/bin/sh,/usr/bin/sudo
```

## Limites e trade-offs
Você pode usar o operador de negação `!=` nos escopos (por exemplo, `executable!=/usr/bin/kubelet` dentro de `not-container`) para silenciar daemons legítimos do sistema operacional do nó.

## Como verificar
Teste o escopo `container` vs `not-container` executando comandos no host e dentro de um container Docker de teste.

## Conexões
- [[tracee-policies-yaml-kubernetes-crd-vs-plain-format-64-policies]] — Veja também: Tracee Políticas de Detecção (`Policies`): intercambiabilidade entre formato `Kubernetes CRD` (`tracee.aquasec.com/v1beta1`) e `Plain YAML`.
- [[tracee-event-filters-data-args-retval-context-operators-prefix-suffix]] — Veja também: Tracee Filtros de Eventos (`rules[].filters`): operadores sobre `data.*`, `retval`, `uid`, `comm` e wildcards `*` de prefixo/sufixo.

## Fontes
- [Aqua Security Tracee Official Documentation — Overview (Everything is an Event Architecture, 400+ Syscalls, Built-in Signatures, Forensic Capture & Security Model)](https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/policies/index.md) — Visão geral oficial da documentação do Tracee detalhando o pipeline unificado de eventos, assinaturas de detecção embutidas, coleta forense e modelo de ameaças; consultado em 2026-10-03.
- [Aqua Security Tracee Official Documentation — Policies Reference (Kubernetes CRD v1beta1 vs Plain Format, 64 Policies, Scopes & Event Filters)](https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/overview.md) — Referência oficial de políticas do Tracee explicando a intercambiabilidade entre o formato CRD Kubernetes e Plain YAML, escopos e filtros; consultado em 2026-10-03.
- [Aqua Security Tracee — Official GitHub Repository](https://github.com/aquasecurity/tracee) — Repositório oficial Apache-2.0 do Aqua Security Tracee; consultado em 2026-10-03.
