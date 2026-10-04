---
id: software.devops.tranche07.000622
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/cilium/tetragon/main/README.md", "https://tetragon.io/docs/overview/", "https://github.com/cilium/tetragon"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Cilium Tetragon: observabilidade completa do ciclo de vida de processos com process_exec e process_exit

## Em uma frase
O Cilium Tetragon gera por padrão eventos `process_exec` e `process_exit` no kernel, mantendo o rastreamento completo da árvore de ancestralidade, argumentos, binários, UID/GID e capabilities de cada processo.

## Por que importa
Em investigações forenses e detecção de intrusão em containers, saber apenas que um binário suspeito como `curl` ou `nc` abriu um socket de rede é insuficiente sem saber qual processo pai o invocou (por exemplo, um worker Java ou Node.js explorado via execução remota de código), com quais privilégios ele iniciou e qual foi seu código de saída. De acordo com o README oficial do Tetragon, os sensores de ciclo de vida de processo vêm ativados por padrão para fornecer visibilidade contínua do nascimento ao término de cada processo.

## Como funciona
Ao enganchar nos pontos internos do kernel Linux responsáveis pela criação (`execve`) e finalização (`exit`) de tarefas, o Tetragon constrói e mantém em mapas eBPF uma tabela de processos correlacionada com metadados do container e do pod Kubernetes. Cada evento `process_exec` registra um `exec_id` único, o `parent_exec_id` (permitindo reconstruir toda a árvore genealógica do processo desde o init do container), o caminho do binário, argumentos de linha de comando, diretório de trabalho (`cwd`), namespaces Linux, capabilities (`permitted`, `effective`, `inheritable`) e credenciais de usuário, enquanto `process_exit` captura o sinal ou código de retorno exato no encerramento.

## Exemplo
```bash
# Filtrar eventos process_exec e process_exit de um namespace ou pod específico usando a CLI tetra
tetra getevents --server-address unix:///var/run/tetragon/tetragon.sock \
  -o compact --namespace default --pods backend-api
```

## Limites e trade-offs
Capturar todos os eventos `process_exec` e `process_exit` em nós que executam pipelines de CI/CD ou scripts shell intensivos (que criam milhares de subprocessos de curta duração por segundo) pode gerar alto volume de logs JSON na saída do agente; nesses ambientes, recomenda-se configurar filtros de exportação (allowlist/denylist) para suprimir processos efêmeros conhecidos e benignos.

## Como verificar
Execute um comando interativo dentro de um pod monitorado (por exemplo, `kubectl exec pod-teste -- ls /tmp`) e confirme na saída do `tetra getevents` a emissão imediata do par `process_exec` e `process_exit` com a árvore de processo pai correspondente.

## Conexões
- [[tetragon-ebpf-observabilidade-seguranca-runtime-enforcement]] — Veja também: Cilium Tetragon: observabilidade de segurança e runtime enforcement em tempo real com eBPF.
- [[tetragon-tracingpolicy-kprobes-tracepoints-uprobes-kernel]] — Veja também: Cilium Tetragon: CRD TracingPolicy e rastreamento genérico com kprobes, tracepoints e uprobes.
- [[tetragon-tetra-cli-inspecao-eventos-filtros-kubernetes]] — Referência cruzada direta com tetragon-tetra-cli-inspecao-eventos-filtros-kubernetes.

## Fontes
- [Cilium Tetragon GitHub — README.md (Process Lifecycle, TracingPolicy & Tetra CLI)](https://raw.githubusercontent.com/cilium/tetragon/main/README.md) — README oficial do Cilium Tetragon cobrindo eventos process_exec/process_exit, rastreamento genérico com kprobes/tracepoints/uprobes via TracingPolicy e casos de uso em Kubernetes e Linux; consultado em 2026-10-03.
- [Cilium Tetragon Official Documentation — Overview & eBPF Real-Time Enforcement](https://tetragon.io/docs/overview/) — Visão geral técnica do Cilium Tetragon detalhando filtragem e bloqueio síncrono em eBPF dentro do kernel Linux e enriquecimento com identidades do Kubernetes; consultado em 2026-10-03.
- [Cilium Tetragon — Official GitHub Repository](https://github.com/cilium/tetragon) — Repositório oficial do Cilium Tetragon na CNCF; consultado em 2026-10-03.
