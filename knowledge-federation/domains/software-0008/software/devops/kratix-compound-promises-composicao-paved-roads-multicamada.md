---
id: software.devops.tranche12.001109
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

# Kratix: Compound Promises e Composição de Paved Roads Multicamada

## Em uma frase
Compound Promises no Kratix são Promises de nível superior cujo pipeline `resource.configure` emite Resource Requests para outras Promises de nível inferior (como banco de dados, cache, ingress e pipeline CI), compondo "paved roads" completas em uma única requisição.

## Por que importa
Equipes de produto frequentemente precisam provisionar um ambiente completo de microsserviço (aplicação + PostgreSQL + Redis + rota DNS) de forma atômica, enquanto especialistas de domínio continuam mantendo cada Promise individual separadamente.

## Como funciona
Na Compound Promise, `spec.workflows.promise.configure` garante que as sub-Promises requeridas estejam instaladas na plataforma, e o pipeline `spec.workflows.resource.configure` gera manifestos das CRDs filhas destinados ao próprio cluster de plataforma (usando um `Destination` que aponta para o plano de controle da plataforma), acionando em cascata os workflows de cada serviço especializado.

## Exemplo
```yaml
# Trecho de manifesto emitido por uma Compound Promise em /kratix/output/db-request.yaml:
apiVersion: marketplace.kratix.io/v1alpha2
kind: postgresql
metadata:
  name: checkout-service-db
  namespace: default
spec:
  teamId: "checkout-squad"
  backupEnabled: true
```

## Limites e trade-offs
Criar dependências circulares entre Compound Promises ou aninhar muitas camadas sem propagar corretamente o status das sub-requisições torna o diagnóstico de falhas de provisionamento opaco para o usuário final.

## Como verificar
Verifique se a Resource Request da Compound Promise cria as Resource Requests filhas com ` labels` de rastreabilidade e se o status consolidado reflete a prontidão de todos os sub-recursos.

## Conexões
- [[kratix-gestao-frota-day2-upgrades-reconciliacao-instancias]] — Veja também: Kratix: Gestão de Frota no Dia 2 e Atualização em Massa de Instâncias via Promise.
- [[kratix-delete-workflows-garbage-collection-descomissionamento]] — Veja também: Kratix: Workflows de Deleção (resource.delete) e Descomissionamento Seguro.

## Fontes
- [Kratix GitHub — README.md & Official Quick Start Guide (Promises, Destinations, State Stores & Fleet Management)](https://docs.kratix.io/main/quick-start) — README oficial do syntasso/kratix (Apache-2.0) e guia Quick Start detalhando Promises, Resource Requests, Workflows em containers, State Stores (SeaweedFS/Git), Flux e atualização de frota no Dia 2; consultado em 2026-10-03.
- [Kratix Official Documentation — Quick Start & Platform Concepts](https://raw.githubusercontent.com/syntasso/kratix/main/README.md) — Documentação oficial do Kratix sobre publicação de Promises, status.connectionDetails, Compound Promises e agendamento multi-cluster; consultado em 2026-10-03.
- [Syntasso Kratix — Official GitHub Repository](https://github.com/syntasso/kratix) — Repositório oficial Apache-2.0 do Kratix; consultado em 2026-10-03.
