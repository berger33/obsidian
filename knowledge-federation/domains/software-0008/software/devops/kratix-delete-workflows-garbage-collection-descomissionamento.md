---
id: software.devops.tranche12.001110
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

# Kratix: Workflows de Deleção (resource.delete) e Descomissionamento Seguro

## Em uma frase
Além dos fluxos `configure`, o Kratix suporta workflows `delete` (`spec.workflows.resource.delete` e `spec.workflows.promise.delete`) e finalizers que executam limpezas externas e removem os manifestos do State Store quando uma Resource Request ou Promise é excluída.

## Por que importa
Se um workflow `configure` provisionou recursos fora do Kubernetes (como registros em API externa, DNS corporativo ou buckets cloud via chamadas de API) ou requer snapshot final antes da remoção, simplesmente apagar o YAML do GitOps deixaria recursos órfãos ou causaria perda de dados.

## Como funciona
Quando o usuário executa `kubectl delete` na Resource Request, o finalizer do Kratix retém o objeto, dispara o Job de pipeline configurado em `workflows.resource.delete` passando o manifesto em `/kratix/input/object.yaml` e, somente após o container de deleção terminar com código zero, remove o `Work` e o `WorkPlacement` do State Store e libera o finalizer.

## Exemplo
```bash
kubectl delete postgresql.marketplace.kratix.io order-db -n default
kubectl get pods -l kratix.io/promise-name=postgresql,kratix.io/workflow-action=delete
kubectl get workplacements.platform.kratix.io -A
```

## Limites e trade-offs
Escrever um pipeline `resource.delete` que falha permanentemente quando o recurso externo já foi removido manualmente trava o finalizer da Resource Request no Kubernetes em estado `Terminating`.

## Como verificar
Garanta que toda lógica em `workflows.resource.delete` seja idempotente (tratando `404 Not Found` como sucesso) e valide que o `WorkPlacement` e os artefatos no State Store desaparecem após a deleção.

## Conexões
- [[kratix-compound-promises-composicao-paved-roads-multicamada]] — Veja também: Kratix: Compound Promises e Composição de Paved Roads Multicamada.

## Fontes
- [Kratix GitHub — README.md & Official Quick Start Guide (Promises, Destinations, State Stores & Fleet Management)](https://docs.kratix.io/main/quick-start) — README oficial do syntasso/kratix (Apache-2.0) e guia Quick Start detalhando Promises, Resource Requests, Workflows em containers, State Stores (SeaweedFS/Git), Flux e atualização de frota no Dia 2; consultado em 2026-10-03.
- [Kratix Official Documentation — Quick Start & Platform Concepts](https://raw.githubusercontent.com/syntasso/kratix/main/README.md) — Documentação oficial do Kratix sobre publicação de Promises, status.connectionDetails, Compound Promises e agendamento multi-cluster; consultado em 2026-10-03.
- [Syntasso Kratix — Official GitHub Repository](https://github.com/syntasso/kratix) — Repositório oficial Apache-2.0 do Kratix; consultado em 2026-10-03.
