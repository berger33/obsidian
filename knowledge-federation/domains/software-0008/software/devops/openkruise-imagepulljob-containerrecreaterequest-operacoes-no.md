---
id: software.devops.tranche16.001559
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
fontes: ["https://raw.githubusercontent.com/openkruise/kruise/master/README.md", "https://openkruise.io/docs/user-manuals/cloneset/", "https://github.com/openkruise/kruise"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenKruise: pré-aquecimento de imagens (`ImagePullJob`) e reinício cirúrgico (`ContainerRecreateRequest`)

## Em uma frase
O OpenKruise fornece CRDs operacionais de dia 2 que atuam diretamente sobre os nós via `kruise-daemon`: o `ImagePullJob` para pré-baixar imagens de container em lote nos nós antes de um rollout e o `ContainerRecreateRequest` (`CRR`) para reiniciar containers individuais dentro de um Pod ativo.

## Por que importa
Quando um `CloneSet` ou `Deployment` de 500 réplicas é atualizado para uma nova imagem de 2 GB, o download simultâneo no momento do rollout causa lentidão e timeouts. Além disso, quando apenas um container em um Pod multi-container trava, deletar o Pod inteiro derruba os demais containers saudáveis.

## Como funciona
O `ImagePullJob` distribui tarefas de pull para o `kruise-daemon` em todos os nós selecionados (com controle de paralelismo `parallelism` e `completionPolicy`), garantindo que as camadas já estejam no cache do CRI antes do deploy. Já o `ContainerRecreateRequest` instrui o `kruise-daemon` do nó onde o Pod reside a parar e recriar apenas os containers listados sem remover o Pod da API.

## Exemplo
```yaml
apiVersion: apps.kruise.io/v1alpha1
kind: ImagePullJob
metadata:
  name: prewarm-release-v2
spec:
  image: ghcr.io/org/order-service:v2.0.0
  parallelism: 10
  completionPolicy:
    type: Always
    activeDeadlineSeconds: 1200
    ttlSecondsAfterFinished: 300
```

## Limites e trade-offs
Para imagens hospedadas em registries privados, o `ImagePullJob` precisa que os nomes dos `Secrets` de credenciais sejam listados explicitamente em `spec.pullSecrets` para que o `kruise-daemon` possa autenticar o pull no CRI.

## Como verificar
Acompanhe `kubectl get imagepulljob prewarm-release-v2` e confirme que `SUCCEEDED` iguala o número de nós desejados (`DESIRED`) antes de disparar o rollout do `CloneSet`.

## Conexões
- [[openkruise-workloadspread-uniteddeployment-distribuicao-multi-dominio]] — Veja também: OpenKruise: distribuição multi-domínio elástica com `WorkloadSpread` e `UnitedDeployment`.
- [[openkruise-deletion-protection-pod-unavailable-budget-sla]] — Veja também: OpenKruise: proteção contra deleção em cascata (`Deletion Protection`) e `PodUnavailableBudget` (`PUB`).

## Fontes
- [OpenKruise GitHub — README.md (Advanced Workloads, In-Place Update, Sidecar Management, Multi-Domain & Application Protection)](https://raw.githubusercontent.com/openkruise/kruise/master/README.md) — README oficial do openkruise/kruise (CNCF Incubating) listando os controladores avançados de workload, operações aprimoradas e proteções de disponibilidade; consultado em 2026-10-03.
- [OpenKruise Official Documentation — CloneSet User Manual (Scale Features, PVC Templates, disablePVCReuse & Selective Pod Deletion)](https://openkruise.io/docs/user-manuals/cloneset/) — Manual oficial do CloneSet no OpenKruise detalhando suporte a PVCs, atualização in-place, podsToDelete e sequência de prioridades de deleção; consultado em 2026-10-03.
- [OpenKruise — Official GitHub Repository](https://github.com/openkruise/kruise) — Repositório oficial Apache-2.0 do OpenKruise na CNCF; consultado em 2026-10-03.
