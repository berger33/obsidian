---
id: software.devops.tranche17.001602
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
fontes: ["https://karmada.io/docs/core-concepts/architecture/", "https://raw.githubusercontent.com/karmada-io/karmada/master/README.md", "https://github.com/karmada-io/karmada"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Karmada: fluxo de propagação em quatro estágios (`PropagationPolicy` -> `ResourceBinding` -> `Work` -> Member Cluster)

## Em uma frase
A distribuição de um recurso no Karmada segue um pipeline desacoplado de quatro controladores: `Cluster Controller`, `Policy Controller`, `Binding Controller` e `Execution Controller`.

## Por que importa
Se um único controlador monolítico lesse um `Deployment`, decidisse o agendamento e gravasse diretamente na API de 50 clusters remotos, qualquer falha parcial ou customização regional bloquearia toda a reconciliação.

## Como funciona
Quando um manifesto (Resource Template) e uma `PropagationPolicy` são criados no `karmada-apiserver`: 1) o **Policy Controller** casa o recurso via `resourceSelector` e gera um `ResourceBinding`; 2) o **Karmada Scheduler** lê o `ResourceBinding` e preenche os clusters alvo e a contagem de réplicas por cluster; 3) o **Binding Controller** aplica eventuais `OverridePolicies` e cria um objeto `Work` por cluster membro (no namespace `karmada-es-<cluster>`); 4) o **Execution Controller** (ou `karmada-agent`) aplica o conteúdo do `Work` no cluster membro.

## Exemplo
```bash
kubectl --context karmada-apiserver get propagationpolicy,resourcebinding -n default
kubectl --context karmada-apiserver get work -n karmada-es-member1
```

## Limites e trade-offs
O usuário nunca deve editar manualmente os objetos intermediários `ResourceBinding` ou `Work`, pois eles são reconciliados continuamente pelo `Policy Controller` e pelo `Binding Controller` a partir do template original e das políticas.

## Como verificar
Inspecione `kubectl get resourcebinding <nome>-deployment -o yaml` no `karmada-apiserver` para auditar os clusters selecionados em `spec.clusters` e o status agregado em `status.aggregatedStatus`.

## Conexões
- [[karmada-arquitetura-control-plane-multi-cluster-cncf-graduated]] — Veja também: Karmada: arquitetura de plano de controle multi-cluster CNCF Graduated (`apiserver`, `controller-manager` e `scheduler`).
- [[karmada-modos-registro-clusters-push-vs-pull-karmada-agent]] — Veja também: Karmada: modos de registro de clusters membros (`Push` direto vs `Pull` via `karmada-agent`).

## Fontes
- [Karmada GitHub — README.md (Kubernetes Armada CNCF Incubating Multi-Cloud & Multi-Cluster Kubernetes Orchestration)](https://karmada.io/docs/core-concepts/architecture/) — README oficial do karmada-io/karmada (CNCF Incubating) apresentando capacidades multi-cluster, API compatível com Kubernetes nativo e políticas de propagação; consultado em 2026-10-03.
- [Karmada Official Documentation — Core Concepts: Architecture (Control Plane, PropagationPolicy, OverridePolicy, ResourceBinding, Work & Agent)](https://raw.githubusercontent.com/karmada-io/karmada/master/README.md) — Documentação oficial de arquitetura do Karmada detalhando API Server, Controller Manager, Karmada Scheduler, Execution Space e sincronização para member clusters; consultado em 2026-10-03.
- [Karmada — Official GitHub Repository](https://github.com/karmada-io/karmada) — Repositório oficial Apache-2.0 do projeto Karmada na CNCF; consultado em 2026-10-03.
