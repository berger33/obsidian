---
id: software.devops.tranche12.001104
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
fontes: ["https://docs.kratix.io/main/quick-start", "https://raw.githubusercontent.com/syntasso/kratix/main/README.md", "https://github.com/syntasso/kratix"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kratix: Workflows Imperativos-Declarativos com Containers (/kratix/input, /kratix/output e /kratix/metadata)

## Em uma frase
Os Workflows do Kratix executam sequências de containers em Pods de Job Kubernetes que leem a requisição em `/kratix/input/object.yaml`, executam lógica arbitrária de validação ou composição e escrevem os artefatos declarativos finais em `/kratix/output/`.

## Por que importa
Nem toda regra de negócio corporativa cabe em templates YAML puros: integrar CMDB, reservar sub-redes em IPAM, registrar custos em FinOps ou compor múltiplos recursos exige linguagens de programação reais antes da entrega GitOps.

## Como funciona
Cada etapa de `spec.workflows.resource.configure` ou `spec.workflows.promise.configure` roda como container em um Pod gerenciado pelo Kratix com volumes compartilhados montados em `/kratix/input` (somente leitura com o objeto solicitado), `/kratix/output` (onde os manifestos destinados aos clusters alvo são gravados) e `/kratix/metadata` (para `status.yaml` e `destination-selectors.yaml`).

## Exemplo
```yaml
apiVersion: platform.kratix.io/v1alpha1
kind: Promise
metadata:
  name: redis-cache
spec:
  workflows:
    resource:
      configure:
        - apiVersion: platform.kratix.io/v1alpha1
          kind: Pipeline
          metadata:
            name: instance-configure
          spec:
            containers:
              - name: generate-manifests
                image: ghcr.io/org/platform-redis-pipeline:v1.2.0
```

## Limites e trade-offs
Fazer chamadas externas mutáveis em containers de pipeline sem garantir idempotência causa efeitos colaterais duplicados sempre que o Kratix reconcilia novamente a Promise ou a Resource Request.

## Como verificar
Liste os Pods de workflow (`kubectl get pods -l kratix.io/promise-name`) e inspecione os logs de cada container da pipeline para confirmar leitura de `/kratix/input` e escrita limpa em `/kratix/output`.

## Conexões
- [[kratix-resource-requests-ciclo-vida-status-connectiondetails]] — Veja também: Kratix: Ciclo de Vida de Resource Requests e Retorno de Status ao Consumidor.
- [[kratix-statestores-gitstatestore-bucketstatestore-gitops]] — Veja também: Kratix: State Stores (GitStateStore e BucketStateStore) e Desacoplamento GitOps.

## Fontes
- [Kratix GitHub — README.md & Official Quick Start Guide (Promises, Destinations, State Stores & Fleet Management)](https://docs.kratix.io/main/quick-start) — README oficial do syntasso/kratix (Apache-2.0) e guia Quick Start detalhando Promises, Resource Requests, Workflows em containers, State Stores (SeaweedFS/Git), Flux e atualização de frota no Dia 2; consultado em 2026-10-03.
- [Kratix Official Documentation — Quick Start & Platform Concepts](https://raw.githubusercontent.com/syntasso/kratix/main/README.md) — Documentação oficial do Kratix sobre publicação de Promises, status.connectionDetails, Compound Promises e agendamento multi-cluster; consultado em 2026-10-03.
- [Syntasso Kratix — Official GitHub Repository](https://github.com/syntasso/kratix) — Repositório oficial Apache-2.0 do Kratix; consultado em 2026-10-03.
