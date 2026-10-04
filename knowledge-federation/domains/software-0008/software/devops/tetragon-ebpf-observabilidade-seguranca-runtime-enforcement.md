---
id: software.devops.tranche07.000621
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

# Cilium Tetragon: observabilidade de segurança e runtime enforcement em tempo real com eBPF

## Em uma frase
O Cilium Tetragon é um componente baseado em eBPF que realiza observabilidade de segurança em tempo real e aplicação de políticas (runtime enforcement) diretamente no kernel Linux com consciência nativa de Kubernetes.

## Por que importa
Ferramentas de segurança em espaço de usuário que interceptam chamadas de sistema (`syscalls`) via `ptrace` ou auditoria assíncrona sofrem alto overhead de troca de contexto, são vulneráveis a condições de corrida (TOCTOU) na fronteira usuário/kernel e detectam ataques apenas depois que a operação maliciosa já foi concluída. Segundo a documentação oficial do Cilium Tetragon, aplicar filtragem e bloqueio diretamente em eBPF dentro do kernel reduz drasticamente o custo de observação e permite interromper processos violadores antes mesmo que a chamada de sistema retorne.

## Como funciona
O Tetragon carrega sensores eBPF em pontos estratégicos do kernel Linux (funções internas via `kprobes`, `tracepoints` e `uprobes`), coletando eventos críticos de segurança — como execução e término de processos, atividade de chamadas de sistema, acesso a arquivos, mudanças de credenciais/capabilities e conexões de rede — e correlacionando o estado do kernel com identidades do Kubernetes (`namespace`, `pod`, `container`, rótulos e workloads). Como toda a filtragem por caminhos de arquivos, sockets, nomes de binários, namespaces e capabilities ocorre no próprio kernel via eBPF, apenas os eventos relevantes são enviados ao agente em user space (formato JSON/gRPC), enquanto ações de bloqueio ou terminação (`SIGKILL`) são executadas sincronicamente pelo kernel em tempo real.

## Exemplo
```bash
# Instalação do Cilium Tetragon no Kubernetes via Helm e observação de eventos em tempo real com a CLI tetra
helm repo add cilium https://helm.cilium.io
helm repo update
helm install tetragon cilium/tetragon -n kube-system

kubectl exec -ti -n kube-system ds/tetragon -c tetragon -- tetra getevents -o compact
```

## Limites e trade-offs
Como o Tetragon opera carregando programas eBPF diretamente no kernel do nó hospedeiro, ele exige privilégios administrativos no DaemonSet e versões de kernel Linux modernas com suporte a BTF (BPF Type Format); além disso, políticas de enforcement mal calibradas que aplicam `Sigkill` em funções críticas do kernel podem encerrar processos legítimos da aplicação se não forem testadas previamente em modo de apenas observação.

## Como verificar
Verifique se o DaemonSet `tetragon` está em estado `Running` no namespace `kube-system` e execute `tetra status` e `tetra getevents -o compact` para confirmar o fluxo de eventos em tempo real enriquecidos com metadados de pods.

## Conexões
- [[tetragon-ciclo-vida-processos-process-exec-exit-arvore]] — Veja também: Cilium Tetragon: observabilidade completa do ciclo de vida de processos com process_exec e process_exit.
- [[tetragon-tracingpolicy-kprobes-tracepoints-uprobes-kernel]] — Referência cruzada direta com tetragon-tracingpolicy-kprobes-tracepoints-uprobes-kernel.
- [[tetragon-enforcement-kernel-sigkill-override-bloqueio-tempo-real]] — Referência cruzada direta com tetragon-enforcement-kernel-sigkill-override-bloqueio-tempo-real.

## Fontes
- [Cilium Tetragon GitHub — README.md (Process Lifecycle, TracingPolicy & Tetra CLI)](https://raw.githubusercontent.com/cilium/tetragon/main/README.md) — README oficial do Cilium Tetragon cobrindo eventos process_exec/process_exit, rastreamento genérico com kprobes/tracepoints/uprobes via TracingPolicy e casos de uso em Kubernetes e Linux; consultado em 2026-10-03.
- [Cilium Tetragon Official Documentation — Overview & eBPF Real-Time Enforcement](https://tetragon.io/docs/overview/) — Visão geral técnica do Cilium Tetragon detalhando filtragem e bloqueio síncrono em eBPF dentro do kernel Linux e enriquecimento com identidades do Kubernetes; consultado em 2026-10-03.
- [Cilium Tetragon — Official GitHub Repository](https://github.com/cilium/tetragon) — Repositório oficial do Cilium Tetragon na CNCF; consultado em 2026-10-03.
