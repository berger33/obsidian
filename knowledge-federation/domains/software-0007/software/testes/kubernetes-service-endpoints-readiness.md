---
id: software.testes.tranche09.000309
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
fontes: ["https://kubernetes.io/docs/concepts/workloads/controllers/deployment/", "https://kubernetes.io/docs/concepts/workloads/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kubernetes Service: testar endpoints prontos sem fixar IP de Pod

## Em uma frase
Service direciona tráfego conforme selectors e endpoints publicados, enquanto Pods e IPs podem mudar durante reconciliação.

## Por que importa
Controladores Kubernetes reconciliam estado de forma assíncrona, então uma assertion instantânea sobre Pod isolado não representa necessariamente o resultado desejado. Teste acoplado ao IP atual do Pod pode passar sem validar o caminho estável usado pelos clientes.

## Como funciona
Teste objetos e condições observáveis em cluster isolado, aguarde convergência com timeout e valide identidades e plugins que participam do comportamento. Acesse DNS/Service da aplicação e confira distribuição para endpoints prontos sob atualização do conjunto de Pods.

## Exemplo
Após substituir réplica, o teste repete request ao Service e confirma resposta sem depender do endereço individual do container.

## Limites e trade-offs
Comportamento depende da versão, controller, scheduler e plugins instalados; dry-run do API server não prova execução de rede ou workload. DNS cache, readiness e implementação de rede afetam o timing; resposta única não prova distribuição equilibrada.

## Como verificar
Inspecione EndpointSlices e faça requests repetidos durante rollout controlado para validar descoberta e continuidade.

## Conexões
- [[kubernetes-namespace-cleanup-isolation]] — Veja também: Kubernetes: isolar testes de cluster por namespace descartável.

## Fontes
- [Kubernetes — Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) — rollout, ReplicaSets e estado observado do Deployment; consultado em 2026-10-02.
- [Kubernetes — Workloads](https://kubernetes.io/docs/concepts/workloads/) — controladores e reconciliação de workloads; consultado em 2026-10-02.
