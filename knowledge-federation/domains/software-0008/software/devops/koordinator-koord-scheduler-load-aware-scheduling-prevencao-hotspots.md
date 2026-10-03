---
id: software.devops.tranche16.001564
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

# Koordinator: agendamento sensível à carga real (`Load-Aware Scheduling`) no `koord-scheduler`

## Em uma frase
O plugin de *Load-Aware Scheduling* do `koord-scheduler` agenda Pods avaliando a utilização real histórica e instantânea de CPU e memória dos nós (reportada pelo `koordlet` via CRD `NodeMetric`), e não apenas a soma estática de `requests` alocadas na API.

## Por que importa
O `kube-scheduler` padrão decide o posicionamento olhando apenas para `requests`: um nó pode ter 80% de `requests` reservados por Pods ociosos (usando 5% de CPU física), enquanto outro nó com 50% de `requests` está com 95% de CPU física saturada. O scheduler padrão colocaria novos Pods no nó já saturado, causando *throttling* severo.

## Como funciona
O `koordlet` coleta métricas de utilização do nó e de cada Pod em janelas deslizantes e atualiza o recurso `NodeMetric` (`slo.koordinator.sh/v1alpha1`). Durante as fases `Filter` e `Score`, o `koord-scheduler` filtra nós que ultrapassaram os limiares de segurança de uso real (por exemplo 75% de CPU física) e atribui maior pontuação aos nós com menor carga efetiva.

## Exemplo
```yaml
apiVersion: slo.koordinator.sh/v1alpha1
kind: NodeMetric
metadata:
  name: worker-node-01
spec:
  collectPolicy:
    aggregateDurationSeconds: 300
    reportIntervalSeconds: 60
```

## Limites e trade-offs
Para workloads recém-criados que ainda não acumularam histórico no `NodeMetric`, o plugin de Load-Aware Scheduling estima a carga inicial a partir de um fator configurável dos `requests` do Pod para evitar sobrecarregar um nó recém-esvaziado com dezenas de agendamentos simultâneos.

## Como verificar
Execute `kubectl get nodemetric -o wide` para inspecionar as taxas de utilização real de CPU e memória reportadas pelo `koordlet` em cada nó do cluster.

## Conexões
- [[koordinator-colocation-profile-injecao-automatica-sem-modificar-workloads]] — Veja também: Koordinator: adoção transparente de co-localização via `ClusterColocationProfile` sem alterar manifestos.
- [[koordinator-orquestracao-fina-cpu-numa-topology-llc-isolamento]] — Veja também: Koordinator: orquestração fina de CPU, topologia NUMA e isolamento de cache L3 (`LLC`) e banda de memória.

## Fontes
- [Koordinator GitHub — README.md (QoS-Based Scheduling System for Hybrid Orchestration Workloads on Kubernetes)](https://koordinator.sh/docs/architecture/overview/) — README oficial do koordinator-sh/koordinator apresentando os objetivos de utilização de recursos, redução de interferência e políticas de agendamento; consultado em 2026-10-03.
- [Koordinator Official Documentation — Architecture Overview (Koord-Scheduler, Koord-Descheduler, Koord-Manager, Koordlet & Koord-RuntimeProxy)](https://raw.githubusercontent.com/koordinator-sh/koordinator/main/README.md) — Visão geral oficial da arquitetura do Koordinator detalhando os componentes do control plane e do nó (Koordlet e Koord-RuntimeProxy); consultado em 2026-10-03.
- [Koordinator — Official GitHub Repository](https://github.com/koordinator-sh/koordinator) — Repositório oficial Apache-2.0 do Koordinator; consultado em 2026-10-03.
