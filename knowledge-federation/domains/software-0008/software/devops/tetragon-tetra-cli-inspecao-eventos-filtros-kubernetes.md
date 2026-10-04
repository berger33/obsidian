---
id: software.devops.tranche07.000628
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

# Cilium Tetragon: uso da CLI Tetra para inspeção de eventos, filtros e administração de sensores

## Em uma frase
A CLI `tetra` conecta-se ao servidor gRPC do agente Cilium Tetragon para transmitir eventos em tempo real, filtrar por pods, namespaces ou processos e gerenciar políticas `TracingPolicy`.

## Por que importa
Durante a resposta a um incidente de segurança ou durante o desenvolvimento de uma nova `TracingPolicy`, engenheiros de plataforma precisam visualizar imediatamente os eventos capturados pelo kernel em formato legível no terminal, sem aguardar a indexação em um SIEM externo. De acordo com a documentação oficial do Tetragon, a ferramenta `tetra` (disponível tanto dentro do container do Tetragon quanto como binário standalone) é a interface primária de linha de comando para interagir com o daemon.

## Como funciona
O binário `tetra` comunica-se via gRPC (por padrão através do socket UNIX `/var/run/tetragon/tetragon.sock` ou porta TCP local) com o daemon do Tetragon. O subcomando `tetra getevents` consome o stream de eventos de observabilidade e segurança, oferecendo dois modos principais de saída: `-o json` (eventos completos estruturados com todos os argumentos do kernel, credenciais e metadados Kubernetes) e `-o compact` (visão resumida em uma linha por evento com ícones indicativos de processo, rede, arquivo ou sinal). Além disso, `tetragetevents` aceita flags de filtragem no servidor (`--namespace`, `--pods`, `--processes`, `--event-types`), e subcomandos como `tetra status` e `tetra tracingpolicy` permitem inspecionar a saúde do agente e testar políticas localmente.

## Exemplo
```bash
# Executar a CLI tetra para visualizar apenas eventos em formato compacto de um namespace específico
kubectl exec -ti -n kube-system ds/tetragon -c tetragon -- \
  tetra getevents -o compact --namespace kube-system

# Verificar o status do daemon Tetragon via socket gRPC
kubectl exec -ti -n kube-system ds/tetragon -c tetragon -- \
  tetra status
```

## Limites e trade-offs
Executar `tetra getevents` sem filtros em um nó de produção movimentado transmite todos os eventos capturados pelo daemon naquele nó através da sessão `kubectl exec`, consumindo largura de banda do apiserver; usar as flags `--namespace`, `--pods` ou `--event-types` delega o filtro ao servidor gRPC do Tetragon antes da serialização para o terminal.

## Como verificar
Execute `tetra status` dentro do pod do Tetragon para confirmar `Health status: running` e teste `tetra getevents -o compact` para observar a decodificação em tempo real dos eventos do nó.

## Conexões
- [[tetragon-consciencia-kubernetes-identidades-pods-namespaces]] — Veja também: Cilium Tetragon: consciência nativa de Kubernetes com enriquecimento por Pod, Namespace e Workload.
- [[tetragon-implantacao-kubernetes-linux-docker-standalone]] — Veja também: Cilium Tetragon: implantação em Kubernetes (DaemonSet) e em hosts Linux via Docker ou pacotes nativos.
- [[tetragon-ebpf-observabilidade-seguranca-runtime-enforcement]] — Referência cruzada direta com tetragon-ebpf-observabilidade-seguranca-runtime-enforcement.
- [[tetragon-ciclo-vida-processos-process-exec-exit-arvore]] — Referência cruzada direta com tetragon-ciclo-vida-processos-process-exec-exit-arvore.
- [[tetragon-exportacao-logs-json-metricas-prometheus-siem]] — Referência cruzada direta com tetragon-exportacao-logs-json-metricas-prometheus-siem.

## Fontes
- [Cilium Tetragon GitHub — README.md (Process Lifecycle, TracingPolicy & Tetra CLI)](https://raw.githubusercontent.com/cilium/tetragon/main/README.md) — README oficial do Cilium Tetragon cobrindo eventos process_exec/process_exit, rastreamento genérico com kprobes/tracepoints/uprobes via TracingPolicy e casos de uso em Kubernetes e Linux; consultado em 2026-10-03.
- [Cilium Tetragon Official Documentation — Overview & eBPF Real-Time Enforcement](https://tetragon.io/docs/overview/) — Visão geral técnica do Cilium Tetragon detalhando filtragem e bloqueio síncrono em eBPF dentro do kernel Linux e enriquecimento com identidades do Kubernetes; consultado em 2026-10-03.
- [Cilium Tetragon — Official GitHub Repository](https://github.com/cilium/tetragon) — Repositório oficial do Cilium Tetragon na CNCF; consultado em 2026-10-03.
