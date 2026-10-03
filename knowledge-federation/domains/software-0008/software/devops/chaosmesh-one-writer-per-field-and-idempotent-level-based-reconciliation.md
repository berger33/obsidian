---
id: software.devops.tranche06.000517
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/README.md", "https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/controllers/README.md", "https://github.com/chaos-mesh/chaos-mesh"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Regras de engenharia de controladores no Chaos Mesh: One writer per field e reconciliação idempotente baseada em nível

## Em uma frase
A seção *Design rules* de `controllers/README.md` estabelece quatro regras arquiteturais estritas para todos os reconciliadores do Chaos Mesh: (1) **One writer per field** — cada campo de status tem um único dono lógico (`desiredphase` é dono de `.status.experiment.desiredPhase`, `condition` é dono de `.status.conditions`, `records` é dono de `.status.experiment.containerRecords`, e `finalizers` é dono dos finalizers comuns), evitando conflitos de escrita e transições contraditórias; (2) **Reconciliação idempotente e baseada em nível (level-based)** — ler o estado atual, compará-lo ao estado desejado e tolerar reexecuções repetidas; (3) **Ordenação explícita** sem depender da ordem de entrega de informers; e (4) **Atualizar apenas o estado próprio em retentativas de conflito** sem reexecutar efeitos colaterais externos não idempotentes dentro do loop de retry de conflito da API.

## Por que importa
Em operadores Kubernetes complexos, se dois reconciliadores diferentes modificam `.status.conditions` ao mesmo tempo ou se uma retentativa de conflito `409 Conflict` no Kubernetes API Server dispara novamente uma chamada gRPC não idempotente ao `Chaos Daemon`, o cluster entra em loops de erro e estados corrompidos.

## Como funciona
Siga a regra *One writer per field* e verifique sempre se a falha já foi injetada ou recuperada no alvo antes de aplicar efeitos colaterais externos, propagando sempre o `context.Context` da reconciliação (evitando `context.TODO()`).

## Exemplo
Durante uma atualização concorrente do objeto `NetworkChaos`, ocorre um conflito de versão (`Conflict`) ao salvar o status; o reconciliador `records` busca novamente a versão mais recente do objeto no API Server e reaplica exclusivamente `.status.experiment.containerRecords` sem reinjetar a falha no `Chaos Daemon`.

## Limites e trade-offs
Conforme instrui `controllers/README.md`, nunca atualize `.status.experiment.desiredPhase` ou `.status.conditions` diretamente de dentro de `ChaosImpl.Apply` ou `ChaosImpl.Recover`; esses métodos devem apenas operar sobre o alvo selecionado e retornar a fase resultante.

## Como verificar
Execute a suíte de testes focada do pipeline comum com `go test ./controllers/common/...` para validar a conformidade das transições de estado e resolução de conflitos.

## Conexões
- [[chaosmesh-pod-level-child-crds-podhttpchaos-podiochaos-podnetworkchaos]] — Veja também: Reconciliação de CRDs filhos de nível de Pod (PodHTTPChaos, PodIOChaos e PodNetworkChaos) no Chaos Mesh.
- [[chaosmesh-controller-runtime-requeue-and-terminal-error-semantics]] — Veja também: Semântica de erros, RequeueAfter e TerminalError com controller-runtime v0.21 no Chaos Mesh.

## Fontes
- [Chaos Mesh GitHub — README.md (Fault Coverage, Controller Manager, Chaos Daemon, Dashboard, Workflows & Multi-Cluster)](https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/README.md) — README oficial do Chaos Mesh (projeto CNCF Incubating sob Apache-2.0) detalhando cobertura ampla de falhas (Pod, rede, DNS, HTTP, I/O, tempo/clock skew, stress, kernel, block device, JVM, máquina física, AWS, Azure e GCP), recursos Schedule/Workflow/StatusCheck, execução multi-cluster e os três componentes de runtime Chaos Controller Manager, Chaos Daemon e Chaos Dashboard.; consultado em 2026-10-03.
- [Chaos Mesh GitHub — controllers/README.md (Uber Fx Architecture, One Writer Per Field, Level-Based Reconcilers & Requeue Semantics)](https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/controllers/README.md) — Guia oficial de arquitetura dos controladores do Chaos Mesh detalhando composição com Uber Fx (controllers/fx.go), pipeline comum (desiredphase, condition, records, finalizers), CRDs filhos PodHTTPChaos/PodIOChaos/PodNetworkChaos, regra One writer per field, reconciliação idempotente baseada em nível e semântica do controller-runtime v0.21.; consultado em 2026-10-03.
- [Chaos Mesh — Official GitHub Repository](https://github.com/chaos-mesh/chaos-mesh) — Repositório oficial Apache-2.0 do Chaos Mesh na CNCF.; consultado em 2026-10-03.
