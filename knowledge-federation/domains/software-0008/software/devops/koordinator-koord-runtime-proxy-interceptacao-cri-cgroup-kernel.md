---
id: software.devops.tranche16.001569
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-16.md"
fontes: ["https://koordinator.sh/docs/architecture/overview/", "https://raw.githubusercontent.com/koordinator-sh/koordinator/main/README.md", "https://github.com/koordinator-sh/koordinator"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Koordinator: interceptação de requisições CRI via `koord-runtime-proxy` para políticas avançadas de kernel

## Em uma frase
O `koord-runtime-proxy` é um serviço systemd opcional de nó que atua como proxy gRPC entre o `kubelet` e o container runtime (`containerd` ou `CRI-O`), interceptando chamadas CRI (`RunPodSandbox`, `CreateContainer`, `UpdateContainerResources`) para aplicar políticas de isolamento antes mesmo do container iniciar.

## Por que importa
Quando o `kubelet` cria um container diretamente no `containerd`, existe uma janela entre a partida do container e a reconciliação assíncrona de um DaemonSet externo em que o container pode rodar com parâmetros de cgroup padrão inadequados para cargas híbridas.

## Como funciona
Instalado no caminho do socket CRI do nó, o `koord-runtime-proxy` encaminha os eventos de ciclo de vida do container para hooks registrados pelo `koordlet`. Isso permite ajustar sincronamente parâmetros de cgroup (como `cpu.idle` para agendamento `SCHED_IDLE` do kernel Linux moderno, pesos de I/O de bloco e limites de memória) no instante exato da criação do container.

## Exemplo
```bash
koord-runtime-proxy \
  --koord-runtimeproxy-endpoint=/var/run/koord-runtimeproxy/runtimeproxy.sock \
  --remote-runtime-service-endpoint=/var/run/containerd/containerd.sock \
  --remote-image-service-endpoint=/var/run/containerd/containerd.sock
```

## Limites e trade-offs
Em versões recentes do Kubernetes que suportam NRI (*Node Resource Interface*) no `containerd` v1.7+, muitas dessas interceptações podem ser realizadas via plugin NRI nativo do `koordlet` sem precisar alterar a flag `--container-runtime-endpoint` do `kubelet`.

## Como verificar
Verifique o status do socket CRI/NRI nos logs do `koordlet` (`kubectl logs -n koordinator-system -l app=koordlet`) para confirmar o registro dos hooks de isolamento de containers.

## Conexões
- [[koordinator-koord-descheduler-rebalanceamento-carga-seguro]] — Veja também: Koordinator: `koord-descheduler` com migração segura apoiada em `Reservation` e balanceamento de carga.
- [[koordinator-job-scheduling-elastic-quota-gang-heterogeneo-ai]] — Veja também: Koordinator: agendamento de jobs batch/IA com `Elastic Quota`, `Gang Scheduling` e dispositivos heterogêneos.

## Fontes
- [Koordinator GitHub — README.md (QoS-Based Scheduling System for Hybrid Orchestration Workloads on Kubernetes)](https://koordinator.sh/docs/architecture/overview/) — README oficial do koordinator-sh/koordinator apresentando os objetivos de utilização de recursos, redução de interferência e políticas de agendamento; consultado em 2026-10-03.
- [Koordinator Official Documentation — Architecture Overview (Koord-Scheduler, Koord-Descheduler, Koord-Manager, Koordlet & Koord-RuntimeProxy)](https://raw.githubusercontent.com/koordinator-sh/koordinator/main/README.md) — Visão geral oficial da arquitetura do Koordinator detalhando os componentes do control plane e do nó (Koordlet e Koord-RuntimeProxy); consultado em 2026-10-03.
- [Koordinator — Official GitHub Repository](https://github.com/koordinator-sh/koordinator) — Repositório oficial Apache-2.0 do Koordinator; consultado em 2026-10-03.
