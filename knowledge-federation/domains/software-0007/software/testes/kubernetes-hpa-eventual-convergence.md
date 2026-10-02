---
id: software.testes.tranche09.000306
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
fontes: ["https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/", "https://kubernetes.io/docs/concepts/workloads/controllers/deployment/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kubernetes HPA: testar convergência eventual de réplicas

## Em uma frase
HPA ajusta réplicas de um workload conforme métricas observadas e seu ciclo de controle, não como resposta instantânea.

## Por que importa
Controladores Kubernetes reconciliam estado de forma assíncrona, então uma assertion instantânea sobre Pod isolado não representa necessariamente o resultado desejado. Assertion imediata de replicas após gerar carga cria flakiness e confunde atraso de coleta com regra incorreta.

## Como funciona
Teste objetos e condições observáveis em cluster isolado, aguarde convergência com timeout e valide identidades e plugins que participam do comportamento. Prepare métricas disponíveis, carga estável e janela de observação; valide faixa e direção esperada em vez de instante exato.

## Exemplo
O teste eleva carga CPU em deployment de laboratório e aguarda aumento dentro do min/max configurado.

## Limites e trade-offs
Comportamento depende da versão, controller, scheduler e plugins instalados; dry-run do API server não prova execução de rede ou workload. Resultado depende de metrics pipeline, requests e períodos do controller; carga artificial isolada pode não representar produção.

## Como verificar
Registre valor de métrica, current/desired replicas e eventos ao longo da janela e encerre a carga no teardown.

## Conexões
- [[kubernetes-pdb-voluntary-disruption-test]] — Veja também: Kubernetes PDB: limitar disrupção voluntária em teste controlado.
- [[kubernetes-configmap-env-vs-volume]] — Veja também: Kubernetes ConfigMap: testar atualização por env e por volume.

## Fontes
- [Kubernetes — Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) — ciclo de controle assíncrono e métricas para escala; consultado em 2026-10-02.
- [Kubernetes — Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) — rollout, ReplicaSets e estado observado do Deployment; consultado em 2026-10-02.
