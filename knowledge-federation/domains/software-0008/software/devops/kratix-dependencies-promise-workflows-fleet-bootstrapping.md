---
id: software.devops.tranche12.001107
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

# Kratix: Dependências de Promise e Workflows de Bootstrapping de Frota

## Em uma frase
As dependências de uma Promise (`spec.dependencies` ou geradas por `spec.workflows.promise.configure`) definem os operadores, CRDs e políticas de base que devem estar instalados nos `Destinations` antes que instâncias daquela Promise possam funcionar.

## Por que importa
Se um desenvolvedor pede um banco PostgreSQL via Promise, o cluster de destino já precisa ter o operador Postgres (como Zalando Postgres Operator ou CloudNativePG) instalado; gerenciar esse pré-requisito manualmente por cluster quebra a automação da plataforma.

## Como funciona
Ao publicar uma Promise, o Kratix executa os workflows de nível de Promise (`workflows.promise.configure`) ou lê `spec.dependencies` e agenda esses manifestos nos `Destinations` compatíveis. Assim, qualquer novo cluster registrado com os labels correspondentes recebe automaticamente o operador base via GitOps antes mesmo da primeira Resource Request.

## Exemplo
```bash
kubectl get works.platform.kratix.io -A -l kratix.io/promise-name=postgresql
kubectl get workplacements.platform.kratix.io -A -l kratix.io/work-type=static-dependency
kubectl get kustomizations.kustomize.toolkit.fluxcd.io -n flux-system
```

## Limites e trade-offs
Empacotar operadores pesados com CRDs conflitantes em `spec.dependencies` de múltiplas Promises que compartilham os mesmos `Destinations` causa disputas de reconciliação no Flux ou Argo CD.

## Como verificar
Inspecione os objetos `Work` do tipo `static-dependency` ou gerados pelo workflow da Promise e confirme no Flux/Argo CD do cluster de destino que os operadores base subiram saudáveis.

## Conexões
- [[kratix-destinations-scheduling-label-selectors-workplacements]] — Veja também: Kratix: Destinations, Agendamento por Label Selectors e WorkPlacements.
- [[kratix-gestao-frota-day2-upgrades-reconciliacao-instancias]] — Veja também: Kratix: Gestão de Frota no Dia 2 e Atualização em Massa de Instâncias via Promise.

## Fontes
- [Kratix GitHub — README.md & Official Quick Start Guide (Promises, Destinations, State Stores & Fleet Management)](https://docs.kratix.io/main/quick-start) — README oficial do syntasso/kratix (Apache-2.0) e guia Quick Start detalhando Promises, Resource Requests, Workflows em containers, State Stores (SeaweedFS/Git), Flux e atualização de frota no Dia 2; consultado em 2026-10-03.
- [Kratix Official Documentation — Quick Start & Platform Concepts](https://raw.githubusercontent.com/syntasso/kratix/main/README.md) — Documentação oficial do Kratix sobre publicação de Promises, status.connectionDetails, Compound Promises e agendamento multi-cluster; consultado em 2026-10-03.
- [Syntasso Kratix — Official GitHub Repository](https://github.com/syntasso/kratix) — Repositório oficial Apache-2.0 do Kratix; consultado em 2026-10-03.
