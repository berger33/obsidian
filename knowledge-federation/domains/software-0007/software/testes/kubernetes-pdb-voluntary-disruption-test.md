---
id: software.testes.tranche09.000305
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md"
fontes: ["https://kubernetes.io/docs/concepts/workloads/pods/disruptions/", "https://kubernetes.io/docs/concepts/workloads/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kubernetes PDB: limitar disrupção voluntária em teste controlado

## Em uma frase
PodDisruptionBudget influencia operações de disrupção voluntária, como eviction, conforme disponibilidade e selector dos Pods.

## Por que importa
Controladores Kubernetes reconciliam estado de forma assíncrona, então uma assertion instantânea sobre Pod isolado não representa necessariamente o resultado desejado. Um teste que mede somente replicas desejadas pode deixar selector ou minAvailable incorretos sem detectar efeito durante drain.

## Como funciona
Teste objetos e condições observáveis em cluster isolado, aguarde convergência com timeout e valide identidades e plugins que participam do comportamento. Em cluster descartável, provoque eviction controlada e observe se orçamento e workload respondem conforme esperado.

## Exemplo
O teste tenta drenar um nó com réplica única protegida e confirma que eviction é bloqueada até existir disponibilidade suficiente.

## Limites e trade-offs
Comportamento depende da versão, controller, scheduler e plugins instalados; dry-run do API server não prova execução de rede ou workload. PDB não impede falha involuntária de nó nem transforma toda atualização em operação sem downtime.

## Como verificar
Valide selector, status do budget e resultado de eviction separadamente, sem provocar disrupção em ambiente de produção.

## Conexões
- [[kubernetes-rbac-auth-can-i-identity]] — Veja também: Kubernetes RBAC: verificar permissão com identidade e escopo.
- [[kubernetes-hpa-eventual-convergence]] — Veja também: Kubernetes HPA: testar convergência eventual de réplicas.

## Fontes
- [Kubernetes — Pod disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) — disrupções voluntárias e PodDisruptionBudgets; consultado em 2026-10-02.
- [Kubernetes — Workloads](https://kubernetes.io/docs/concepts/workloads/) — controladores e reconciliação de workloads; consultado em 2026-10-02.
