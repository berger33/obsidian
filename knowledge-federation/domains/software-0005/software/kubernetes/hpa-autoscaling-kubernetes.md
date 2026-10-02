---
id: software.kubernetes.hpa-autoscaling.000001
tipo: conceito
dominio: software
subdominio: kubernetes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/", "https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/"]
tags: [dominio/software, subdominio/kubernetes, qualidade/candidata]
aliases: [HPA, HorizontalPodAutoscaler, Horizontal Pod Autoscaling]
lote: software-kubernetes-operacao-0005
---

# Autoscaling horizontal de Pods com HPA

## Em uma frase
O HorizontalPodAutoscaler ajusta periodicamente o número desejado de réplicas de um workload escalável a partir de métricas configuradas.

## Por que importa
Uma quantidade fixa de Pods pode ser insuficiente em picos e cara em períodos de baixa demanda. HPA automatiza o ajuste de réplicas, mas não cria capacidade de nó nem corrige automaticamente gargalos que não se resolvem com mais réplicas. Métricas, requests e limites mínimo/máximo precisam refletir o comportamento do serviço.

## Como funciona
O recurso `HorizontalPodAutoscaler` aponta para um alvo escalável, como Deployment ou StatefulSet, e um controller compara métricas atuais com os objetivos. Para CPU ou memória configuradas como utilização percentual, a utilização é calculada em relação ao request do recurso correspondente. Se um container do Pod não tiver request de CPU, a utilização do Pod para essa métrica pode ficar indefinida e o autoscaler não toma ação com base nela. Métricas podem vir da API de recursos ou de APIs customizadas/externas; a API de métricas e o Metrics Server precisam estar disponíveis para o caso de uso escolhido.

## Exemplo
Um serviço pode manter entre três e doze réplicas e ajustar o alvo de utilização média de CPU. Um worker cuja carga é melhor descrita pelo tamanho da fila pode usar uma métrica customizada ou externa, em vez de assumir que CPU é sempre um bom indicador de demanda. HPA altera réplicas do workload; não aumenta request ou limit do container.

## Limites e trade-offs
O controlador é um loop periódico, não uma reação contínua a cada requisição. Métricas atrasadas ou ausentes, requests incorretos, limites máximos baixos e demora para iniciar Pods afetam a resposta. Escalar réplicas também pode aumentar concorrência contra uma dependência compartilhada. Avalie estabilização, janela de métricas, custos e capacidade do cluster antes de ativar escala agressiva.

## Como verificar
Confirme que a API de métricas entrega dados e que os requests usados no cálculo estão configurados em todos os containers relevantes. Em teste de carga, aumente e reduza a demanda; observe tempo até reagir, réplicas desejadas/reais, saturação dos nós e carga nas dependências. Teste também métricas ausentes e alcance dos limites `minReplicas`/`maxReplicas`.

## Conexões
- [[requests-limits-cpu-memoria-kubernetes]] — requests são denominador de métricas percentuais de CPU e memória.
- [[probes-kubernetes-liveness-readiness-startup]] — readiness e inicialização influenciam a capacidade efetivamente disponível.
- [[pdb-disponibilidade-kubernetes]] — autoscaling e interrupções voluntárias são mecanismos diferentes.

## Fontes
- [Kubernetes — Horizontal Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) — métricas, algoritmo e requisitos; acesso em 2026-10-01.
- [Kubernetes — HPA Walkthrough](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/) — exemplos de configuração e tipos de métrica; acesso em 2026-10-01.
