---
id: software.devops.tranche06.000519
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

# Fluxo de criação de novos tipos de caos (api/v1alpha1, chaosimpl, Fx e make generate) no Chaos Mesh

## Em uma frase
A seção *Adding or changing controllers* de `controllers/README.md` documenta o roteiro de 4 passos para adicionar um novo tipo de recurso de caos de nível superior ao Chaos Mesh: (1) definir e anotar o tipo da API sob **`api/v1alpha1/`**; (2) implementar o comportamento de alvo único `Apply` e `Recover` sob **`chaosimpl/`**; (3) fornecer um `ChaosImplPair` a partir do módulo Uber Fx da implementação e incluí-lo em **`chaosimpl.AllImpl`** (protegendo novos controladores de topo com um nome estável em `ShouldSpawnController`); e (4) executar **`make generate`** e inspecionar o código de API gerado, clientes, manifestos de CRDs, registros em `Workflow`/`Schedule` e mapeamentos de frontend.

## Por que importa
No Chaos Mesh, um novo tipo de falha só fica plenamente funcional quando além do reconciliador individual ele também é registrado automaticamente nas estruturas de `Workflow` e `Schedule` e nos schemas de CRDs gerados por `make generate`.

## Como funciona
Ao estender o Chaos Mesh com um novo recurso ou campo em `api/v1alpha1/`, execute sempre `make generate` e inclua os artefatos gerados (CRDs, deepcopy, clientes e integrações de workflow/schedule) no mesmo commit, acompanhados de testes unitários de reconciliação normal, exclusão, conflitos e idempotência.

## Exemplo
Um contribuidor adiciona um novo parâmetro ao tipo `HTTPChaos` em `api/v1alpha1/`, atualiza o `Apply` em `chaosimpl/httpchaos/`, executa `make generate` para atualizar os manifestos de CRD e valida com `go test`.

## Limites e trade-offs
Mantenha sempre estável o nome do controlador passado para `ShouldSpawnController`, pois, conforme alerta `controllers/README.md`, esse identificador faz parte da configuração pública exposta aos usuários em `ENABLED_CONTROLLERS`.

## Como verificar
Execute `make generate` e `git status` para confirmar que todos os CRDs e códigos gerados estão sincronizados com as definições de `api/v1alpha1/`.

## Conexões
- [[chaosmesh-controller-runtime-requeue-and-terminal-error-semantics]] — Veja também: Semântica de erros, RequeueAfter e TerminalError com controller-runtime v0.21 no Chaos Mesh.
- [[chaosmesh-helm-production-installation-and-security-reporting]] — Veja também: Instalação em produção via Helm, matriz de releases suportadas e reporte de segurança (SECURITY.md) no Chaos Mesh.

## Fontes
- [Chaos Mesh GitHub — README.md (Fault Coverage, Controller Manager, Chaos Daemon, Dashboard, Workflows & Multi-Cluster)](https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/README.md) — README oficial do Chaos Mesh (projeto CNCF Incubating sob Apache-2.0) detalhando cobertura ampla de falhas (Pod, rede, DNS, HTTP, I/O, tempo/clock skew, stress, kernel, block device, JVM, máquina física, AWS, Azure e GCP), recursos Schedule/Workflow/StatusCheck, execução multi-cluster e os três componentes de runtime Chaos Controller Manager, Chaos Daemon e Chaos Dashboard.; consultado em 2026-10-03.
- [Chaos Mesh GitHub — controllers/README.md (Uber Fx Architecture, One Writer Per Field, Level-Based Reconcilers & Requeue Semantics)](https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/controllers/README.md) — Guia oficial de arquitetura dos controladores do Chaos Mesh detalhando composição com Uber Fx (controllers/fx.go), pipeline comum (desiredphase, condition, records, finalizers), CRDs filhos PodHTTPChaos/PodIOChaos/PodNetworkChaos, regra One writer per field, reconciliação idempotente baseada em nível e semântica do controller-runtime v0.21.; consultado em 2026-10-03.
- [Chaos Mesh — Official GitHub Repository](https://github.com/chaos-mesh/chaos-mesh) — Repositório oficial Apache-2.0 do Chaos Mesh na CNCF.; consultado em 2026-10-03.
