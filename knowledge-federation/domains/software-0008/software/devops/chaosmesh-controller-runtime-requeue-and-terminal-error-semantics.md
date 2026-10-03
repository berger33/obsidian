---
id: software.devops.tranche06.000518
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

# Semântica de erros, RequeueAfter e TerminalError com controller-runtime v0.21 no Chaos Mesh

## Em uma frase
A seção *Error and requeue semantics* de `controllers/README.md` documenta o contrato exato de retorno dos reconciliadores do Chaos Mesh sobre o **`controller-runtime` v0.21**: (1) `return ctrl.Result{}, err` ignora o `Result` e agenda retentativa com backoff exponencial para erros não terminais (registrando o erro nos logs e nas métricas de erro de reconciliação); (2) `return ctrl.Result{RequeueAfter: delay}, nil` agenda nova reconciliação após um atraso conhecido (ideal para prazos de `duration` ou polling explícito); (3) `return ctrl.Result{}, nil` encerra a reconciliação até que um novo evento observado enfileire o objeto; e (4) `return ctrl.Result{}, reconcile.TerminalError(err)` registra o erro sem retentar quando novas tentativas jamais poderão progredir. O guia também destaca que `ctrl.Result.Requeue` está depreciado na versão atual do `controller-runtime` e que erros `NotFound` durante exclusão devem ser tratados como conclusão bem-sucedida.

## Por que importa
Retornar um `err` comum apenas para aguardar alguns segundos que um pod suba polui os logs de erro do `chaos-controller-manager` e infla falsamente os alertas de métricas de falha de reconciliação; por outro lado, retornar simultaneamente um `Result` não zero e um `err` não nulo é inútil porque o `controller-runtime` descarta o `Result` sempre que `err != nil`.

## Como funciona
Use eventos observados (watches) ou `ctrl.Result{RequeueAfter: delay}, nil` para esperas esperadas (como o término do `duration` de um experimento de caos) e retorne `err` apenas quando ocorrer uma falha real que deva ser retentada com backoff e contabilizada nas métricas.

## Exemplo
Quando um experimento `PodChaos` é configurado com `duration: 60s`, após injetar a falha o pipeline retorna `ctrl.Result{RequeueAfter: remainingDuration}, nil` sem erro, acordando exatamente no instante de expirar para iniciar a fase de recuperação (`Recover`).

## Limites e trade-offs
Não engula falhas reais de comunicação com o `Chaos Daemon` ou API Server apenas registrando um log e retornando `ctrl.Result{}, nil`, a menos que um evento futuro observado garanta a retentativa daquele trabalho.

## Como verificar
Execute `go test ./controllers/schedule/... ./controllers/statuscheck/... ./controllers/multicluster/...` para verificar o comportamento de enfileiramento e tratamento de erros dos controladores.

## Conexões
- [[chaosmesh-one-writer-per-field-and-idempotent-level-based-reconciliation]] — Veja também: Regras de engenharia de controladores no Chaos Mesh: One writer per field e reconciliação idempotente baseada em nível.
- [[chaosmesh-adding-new-top-level-chaos-kinds-and-make-generate]] — Veja também: Fluxo de criação de novos tipos de caos (api/v1alpha1, chaosimpl, Fx e make generate) no Chaos Mesh.

## Fontes
- [Chaos Mesh GitHub — README.md (Fault Coverage, Controller Manager, Chaos Daemon, Dashboard, Workflows & Multi-Cluster)](https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/README.md) — README oficial do Chaos Mesh (projeto CNCF Incubating sob Apache-2.0) detalhando cobertura ampla de falhas (Pod, rede, DNS, HTTP, I/O, tempo/clock skew, stress, kernel, block device, JVM, máquina física, AWS, Azure e GCP), recursos Schedule/Workflow/StatusCheck, execução multi-cluster e os três componentes de runtime Chaos Controller Manager, Chaos Daemon e Chaos Dashboard.; consultado em 2026-10-03.
- [Chaos Mesh GitHub — controllers/README.md (Uber Fx Architecture, One Writer Per Field, Level-Based Reconcilers & Requeue Semantics)](https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/controllers/README.md) — Guia oficial de arquitetura dos controladores do Chaos Mesh detalhando composição com Uber Fx (controllers/fx.go), pipeline comum (desiredphase, condition, records, finalizers), CRDs filhos PodHTTPChaos/PodIOChaos/PodNetworkChaos, regra One writer per field, reconciliação idempotente baseada em nível e semântica do controller-runtime v0.21.; consultado em 2026-10-03.
- [Chaos Mesh — Official GitHub Repository](https://github.com/chaos-mesh/chaos-mesh) — Repositório oficial Apache-2.0 do Chaos Mesh na CNCF.; consultado em 2026-10-03.
