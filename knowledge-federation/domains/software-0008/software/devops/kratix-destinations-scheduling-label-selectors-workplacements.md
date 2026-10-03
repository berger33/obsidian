---
id: software.devops.tranche12.001106
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

# Kratix: Destinations, Agendamento por Label Selectors e WorkPlacements

## Em uma frase
Recursos `Destination` no Kratix representam ambientes alvo (clusters Kubernetes, contas cloud ou ambientes Terraform) rotulados com metadados que permitem ao scheduler do Kratix direcionar `Work` para os destinos corretos por meio de `WorkPlacements`.

## Por que importa
Uma plataforma corporativa precisa rotear cargas de desenvolvimento para clusters de baixo custo, bancos PCI-DSS para clusters isolados e operadores de base para toda a frota sem codificar nomes de clusters estáticos nos pipelines.

## Como funciona
Cada `Destination` aponta para um `stateStoreRef` e declara labels (como `environment: prod`, `region: sa-east-1`, `pci: "true"`). A Promise ou o arquivo `/kratix/metadata/destination-selectors.yaml` emitido pelo pipeline define seletores de labels; o Kratix avalia a correspondência e cria objetos `WorkPlacement` que materializam os manifestos nas pastas daquele `Destination` dentro do State Store.

## Exemplo
```yaml
apiVersion: platform.kratix.io/v1alpha1
kind: Destination
metadata:
  name: prod-sa-east-1
  labels:
    environment: prod
    region: sa-east-1
spec:
  stateStoreRef:
    kind: GitStateStore
    name: fleet-git-store
  filepath:
    mode: nestedByMetadata
```

## Limites e trade-offs
Alterar os labels de um `Destination` em produção sem avaliar quais `WorkPlacements` ativos dependem daquele seletor faz o Kratix remover os manifestos do State Store daquele cluster, descomissionando recursos ativos.

## Como verificar
Execute `kubectl get workplacements.platform.kratix.io -A` e verifique se cada `Work` foi associado ao `Destination` esperado sem condições de `ScheduleSucceeded=False`.

## Conexões
- [[kratix-statestores-gitstatestore-bucketstatestore-gitops]] — Veja também: Kratix: State Stores (GitStateStore e BucketStateStore) e Desacoplamento GitOps.
- [[kratix-dependencies-promise-workflows-fleet-bootstrapping]] — Veja também: Kratix: Dependências de Promise e Workflows de Bootstrapping de Frota.

## Fontes
- [Kratix GitHub — README.md & Official Quick Start Guide (Promises, Destinations, State Stores & Fleet Management)](https://docs.kratix.io/main/quick-start) — README oficial do syntasso/kratix (Apache-2.0) e guia Quick Start detalhando Promises, Resource Requests, Workflows em containers, State Stores (SeaweedFS/Git), Flux e atualização de frota no Dia 2; consultado em 2026-10-03.
- [Kratix Official Documentation — Quick Start & Platform Concepts](https://raw.githubusercontent.com/syntasso/kratix/main/README.md) — Documentação oficial do Kratix sobre publicação de Promises, status.connectionDetails, Compound Promises e agendamento multi-cluster; consultado em 2026-10-03.
- [Syntasso Kratix — Official GitHub Repository](https://github.com/syntasso/kratix) — Repositório oficial Apache-2.0 do Kratix; consultado em 2026-10-03.
