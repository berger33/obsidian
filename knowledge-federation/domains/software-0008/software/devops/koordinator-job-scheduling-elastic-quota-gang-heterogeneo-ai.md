---
id: software.devops.tranche16.001570
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

# Koordinator: agendamento de jobs batch/IA com `Elastic Quota`, `Gang Scheduling` e dispositivos heterogêneos

## Em uma frase
Além da co-localização no nível de nó, o `koord-scheduler` incorpora capacidades nativas de agendamento de jobs distribuídos de Big Data e IA/ML: *Gang Scheduling* (`Coscheduling`), cotas elásticas hierárquicas (`Elastic Quota`) e agendamento topológico de GPUs/RDMA.

## Por que importa
Treinamentos distribuídos de modelos (PyTorch, Ray, Spark) exigem que todos os N workers subam juntos (*all-or-nothing*) com GPUs interconectadas por NVLink/RDMA, além de precisarem tomar emprestada a cota ociosa de outras equipes e devolvê-la quando o proprietário original submeter tarefas.

## Como funciona
O `koord-scheduler` suporta grupos de Pods (`PodGroup` compatível com `scheduling.sigs.k8s.io`), gerencia árvores de cotas com `min` garantido e `max` compartilhável para empréstimo entre departamentos e descobre a topologia física de GPUs, NICs RDMA e FPGAs por meio do `koordlet`, alocando dispositivos no mesmo switch PCIe/NVLink.

## Exemplo
```yaml
apiVersion: scheduling.sigs.k8s.io/v1alpha1
kind: PodGroup
metadata:
  name: pytorch-distributed-job
  namespace: ai-training
spec:
  minMember: 4
  scheduleTimeoutSeconds: 300
```

## Limites e trade-offs
Se os `4` Pods do `PodGroup` não puderem ser alocados dentro de `scheduleTimeoutSeconds`, o plugin de `Coscheduling` libera as reservas parciais daquele grupo para evitar *deadlock* de recursos entre múltiplos jobs concorrentes na fila.

## Como verificar
Inspecione `kubectl get podgroup -n ai-training` e verifique a transição de fase do grupo quando todos os `minMember` Pods são agendados conjuntamente pelo `koord-scheduler`.

## Conexões
- [[koordinator-koord-runtime-proxy-interceptacao-cri-cgroup-kernel]] — Veja também: Koordinator: interceptação de requisições CRI via `koord-runtime-proxy` para políticas avançadas de kernel.

## Fontes
- [Koordinator GitHub — README.md (QoS-Based Scheduling System for Hybrid Orchestration Workloads on Kubernetes)](https://koordinator.sh/docs/architecture/overview/) — README oficial do koordinator-sh/koordinator apresentando os objetivos de utilização de recursos, redução de interferência e políticas de agendamento; consultado em 2026-10-03.
- [Koordinator Official Documentation — Architecture Overview (Koord-Scheduler, Koord-Descheduler, Koord-Manager, Koordlet & Koord-RuntimeProxy)](https://raw.githubusercontent.com/koordinator-sh/koordinator/main/README.md) — Visão geral oficial da arquitetura do Koordinator detalhando os componentes do control plane e do nó (Koordlet e Koord-RuntimeProxy); consultado em 2026-10-03.
- [Koordinator — Official GitHub Repository](https://github.com/koordinator-sh/koordinator) — Repositório oficial Apache-2.0 do Koordinator; consultado em 2026-10-03.
