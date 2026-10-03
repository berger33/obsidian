---
id: software.devops.tranche07.000626
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

# Cilium Tetragon: observabilidade de rede correlacionando sockets TCP/UDP diretamente a processos e pods

## Em uma frase
O Cilium Tetragon associa estruturas de sockets do kernel (`struct sock`) aos processos, binários e pods Kubernetes que abriram ou transmitiram dados na conexão, eliminando pontos cegos na observabilidade de rede.

## Por que importa
Fluxos tradicionais de rede (NetFlow, logs de CNI ou capturas de pacotes) informam que o IP de um pod conversou com um endereço externo suspeito na porta 443, mas não conseguem responder qual processo específico e qual linha de comando dentro daquele pod iniciaram a conexão — se foi o binário oficial da aplicação Go ou um script Python baixado por um invasor. De acordo com a documentação oficial do Tetragon, o estado em eBPF une sockets a processos no momento exato da chamada no kernel.

## Como funciona
Ao instrumentar funções da pilha de rede do kernel Linux (como `tcp_connect`, `tcp_close`, `tcp_sendmsg` ou `udp_sendmsg`) por meio de uma `TracingPolicy` com argumentos do tipo `sock` ou `skb`, o Tetragon extrai os endereços IP de origem e destino, portas TCP/UDP, família de protocolo e estatísticas de bytes enviados/recebidos, e cruza automaticamente esses dados no kernel com o `exec_id` do processo em execução. O evento resultante entregue ao espaço de usuário mostra em um único registro JSON tanto os metadados de camada 3/4 da conexão quanto o binário completo, argumentos, UID, árvore de processos pai e identidade do pod Kubernetes.

## Exemplo
```bash
# Inspecionar eventos de rede e processos asociados ao pod frontend-web com a CLI tetra
kubectl exec -n kube-system daemonset/tetragon -- \
  tetra getevents -o compact --pods frontend-web
```

## Limites e trade-offs
Rastrear apenas o estabelecimento e o fechamento de conexões (`tcp_connect` e `tcp_close`) possui overhead quase nulo no kernel; porém, enganchar em funções por pacote ou por mensagem (como `tcp_sendmsg` ou `tcp_recvmsg`) sem agregação em mapa eBPF ou filtro por IP/porta em serviços de alto throughput pode gerar volume excessivo de eventos no ring buffer do eBPF.

## Como verificar
Com uma política de observabilidade de conexões TCP ativa, execute `curl https://example.com` dentro de um pod e confirme no `tetra getevents` que o evento reporta o IP/porta de destino associado exatamente ao binário `/usr/bin/curl` e ao pod correspondente.

## Conexões
- [[tetragon-monitoramento-arquivos-credenciais-execucao-privilegiada]] — Veja também: Cilium Tetragon: monitoramento de acesso a arquivos sensíveis, credenciais Linux e execução privilegiada.
- [[tetragon-consciencia-kubernetes-identidades-pods-namespaces]] — Veja também: Cilium Tetragon: consciência nativa de Kubernetes com enriquecimento por Pod, Namespace e Workload.
- [[tetragon-ebpf-observabilidade-seguranca-runtime-enforcement]] — Referência cruzada direta com tetragon-ebpf-observabilidade-seguranca-runtime-enforcement.
- [[tetragon-ciclo-vida-processos-process-exec-exit-arvore]] — Referência cruzada direta com tetragon-ciclo-vida-processos-process-exec-exit-arvore.
- [[tetragon-tracingpolicy-kprobes-tracepoints-uprobes-kernel]] — Referência cruzada direta com tetragon-tracingpolicy-kprobes-tracepoints-uprobes-kernel.

## Fontes
- [Cilium Tetragon GitHub — README.md (Process Lifecycle, TracingPolicy & Tetra CLI)](https://raw.githubusercontent.com/cilium/tetragon/main/README.md) — README oficial do Cilium Tetragon cobrindo eventos process_exec/process_exit, rastreamento genérico com kprobes/tracepoints/uprobes via TracingPolicy e casos de uso em Kubernetes e Linux; consultado em 2026-10-03.
- [Cilium Tetragon Official Documentation — Overview & eBPF Real-Time Enforcement](https://tetragon.io/docs/overview/) — Visão geral técnica do Cilium Tetragon detalhando filtragem e bloqueio síncrono em eBPF dentro do kernel Linux e enriquecimento com identidades do Kubernetes; consultado em 2026-10-03.
- [Cilium Tetragon — Official GitHub Repository](https://github.com/cilium/tetragon) — Repositório oficial do Cilium Tetragon na CNCF; consultado em 2026-10-03.
