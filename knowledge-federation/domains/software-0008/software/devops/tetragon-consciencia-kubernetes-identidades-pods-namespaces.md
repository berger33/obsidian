---
id: software.devops.tranche07.000627
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

# Cilium Tetragon: consciência nativa de Kubernetes com enriquecimento por Pod, Namespace e Workload

## Em uma frase
O Cilium Tetragon integra o estado do kernel Linux com metadados do Kubernetes para filtrar políticas e enriquecer eventos por `namespace`, `pod`, `container`, rótulos (`podSelector`) e controladores (Deployment/DaemonSet).

## Por que importa
Em um nó Kubernetes que hospeda dezenas de pods de diferentes equipes, eventos brutos do kernel contendo apenas números de PID, cgroup ID ou inode de mount namespace são difíceis de interpretar para analistas de SOC e impossíveis de usar para criar regras de segurança específicas por microsserviço. Segundo o README oficial do Tetragon, o componente é nativamente Kubernetes-aware, permitindo configurar detecção e bloqueio em relação a workloads individuais.

## Como funciona
O agente do Tetragon em cada nó monitora a API do Kubernetes (ou o estado local do kubelet/container runtime) e mapeia os identificadores de cgroups e namespaces do container para o objeto Pod correspondente. Esse mapeamento opera em duas direções: (1) no enriquecimento de eventos de saída, anexando automaticamente nome do pod, namespace, imagem do container, labels e workload pai a cada evento `process_exec`, `process_kprobe` ou `process_exit`; e (2) na filtragem em-kernel de políticas `TracingPolicy` e `TracingPolicyNamespaced`, onde o uso de `podSelector` ou escopo de namespace restringe a avaliação do sensor eBPF apenas aos containers pertencentes aos pods selecionados.

## Exemplo
```yaml
# TracingPolicy aplicando monitoramento apenas a pods com o rótulo app=pagamentos-api
apiVersion: cilium.io/v1alpha1
kind: TracingPolicyNamespaced
metadata:
  name: politica-pagamentos
  namespace: financeiro
spec:
  podSelector:
    matchLabels:
      app: pagamentos-api
  kprobes:
    - call: "security_bprm_check"
      syscall: false
```

## Limites e trade-offs
O uso de `TracingPolicyNamespaced` e `podSelector` é essencial em clusters multi-tenant porque impede que uma política criada para proteger um serviço específico afete todos os outros pods do nó; contudo, o operador `tetragon-operator` e o RBAC de leitura de pods precisam estar saudáveis para que os novos pods criados recebam o mapeamento de cgroup imediato na inicialização.

## Como verificar
Inspecione um evento bruto em JSON (`tetra getevents -o json | jq .process_exec.process.pod`) e confirme a presença dos campos `namespace`, `name`, `container.image.id`, `pod_labels` e `workload`.

## Conexões
- [[tetragon-observabilidade-rede-sockets-processos-ebpf]] — Veja também: Cilium Tetragon: observabilidade de rede correlacionando sockets TCP/UDP diretamente a processos e pods.
- [[tetragon-tetra-cli-inspecao-eventos-filtros-kubernetes]] — Veja também: Cilium Tetragon: uso da CLI Tetra para inspeção de eventos, filtros e administração de sensores.
- [[tetragon-ebpf-observabilidade-seguranca-runtime-enforcement]] — Referência cruzada direta com tetragon-ebpf-observabilidade-seguranca-runtime-enforcement.
- [[tetragon-tracingpolicy-kprobes-tracepoints-uprobes-kernel]] — Referência cruzada direta com tetragon-tracingpolicy-kprobes-tracepoints-uprobes-kernel.
- [[inspektor-enriquecimento-kernel-kubernetes-filtragem-ebpf]] — Referência cruzada direta com inspektor-enriquecimento-kernel-kubernetes-filtragem-ebpf.

## Fontes
- [Cilium Tetragon GitHub — README.md (Process Lifecycle, TracingPolicy & Tetra CLI)](https://raw.githubusercontent.com/cilium/tetragon/main/README.md) — README oficial do Cilium Tetragon cobrindo eventos process_exec/process_exit, rastreamento genérico com kprobes/tracepoints/uprobes via TracingPolicy e casos de uso em Kubernetes e Linux; consultado em 2026-10-03.
- [Cilium Tetragon Official Documentation — Overview & eBPF Real-Time Enforcement](https://tetragon.io/docs/overview/) — Visão geral técnica do Cilium Tetragon detalhando filtragem e bloqueio síncrono em eBPF dentro do kernel Linux e enriquecimento com identidades do Kubernetes; consultado em 2026-10-03.
- [Cilium Tetragon — Official GitHub Repository](https://github.com/cilium/tetragon) — Repositório oficial do Cilium Tetragon na CNCF; consultado em 2026-10-03.
