---
id: software.devops.tranche06.000513
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

# Orquestração de experimentos recorrentes, fluxos seriados/paralelos e verificações de saúde com Schedule, Workflow e StatusCheck

## Em uma frase
Além dos recursos individuais de falha, o README oficial destaca três recursos nativos de orquestração do Chaos Mesh: **`Schedule`** (para disparar experimentos recorrentes baseados em expressões cron, com rastreamento de objetos ativos, coleta de lixo e propagação de pausa), **`Workflow`** (para encadear experimentos em série ou em paralelo, podendo ser integrado também ao Argo conforme citado nos blogs oficiais) e **`StatusCheck`** (para executar verificações periódicas de saúde da aplicação durante o experimento e abortar automaticamente a falha caso o serviço saia dos limites aceitáveis).

## Por que importa
Executar um `Workflow` de caos com um `StatusCheck` acoplado garante segurança operacional (circuit breaker do próprio experimento): se a verificação HTTP de saúde da aplicação começar a falhar além do limiar configurado, o Chaos Mesh interrompe o workflow e reverte imediatamente as falhas injetadas.

## Como funciona
Combine sempre recursos `Workflow` ou `Schedule` com um `StatusCheck` apontado para o endpoint de saúde ou métrica de SLO da aplicação sob teste, configurando políticas de concorrência (`Forbid` ou `Replace`) nos agendamentos `Schedule`.

## Exemplo
Um `Workflow` no Chaos Mesh inicia uma verificação contínua `StatusCheck` sobre a API de pagamentos enquanto executa em série um `NetworkChaos` (latência de 100ms) seguido de um `PodChaos` (`pod-failure`); quando todas as etapas passam, o workflow conclui e limpa todas as falhas.

## Limites e trade-offs
Sempre defina o campo `duration` explícito nos experimentos de caos e nos nós de `Workflow` para garantir que nenhuma falha fique injetada indefinidamente caso o operador esqueça de deletar o recurso manualmente.

## Como verificar
Inspecione o status de `kubectl get workflow,schedule,statuscheck -n <namespace>` confirmando a execução das etapas e o resultado das checagens de saúde.

## Conexões
- [[chaosmesh-broad-fault-coverage-pod-network-io-time-jvm-and-cloud]] — Veja também: Cobertura abrangente de falhas no Chaos Mesh: Pod, Rede, DNS, HTTP, I/O, Clock Skew, Kernel, JVM, Bare-Metal e Nuvens.
- [[chaosmesh-multi-cluster-remote-chaos-execution]] — Veja também: Execução multi-cluster de experimentos de caos a partir de um cluster de gerenciamento no Chaos Mesh.

## Fontes
- [Chaos Mesh GitHub — README.md (Fault Coverage, Controller Manager, Chaos Daemon, Dashboard, Workflows & Multi-Cluster)](https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/README.md) — README oficial do Chaos Mesh (projeto CNCF Incubating sob Apache-2.0) detalhando cobertura ampla de falhas (Pod, rede, DNS, HTTP, I/O, tempo/clock skew, stress, kernel, block device, JVM, máquina física, AWS, Azure e GCP), recursos Schedule/Workflow/StatusCheck, execução multi-cluster e os três componentes de runtime Chaos Controller Manager, Chaos Daemon e Chaos Dashboard.; consultado em 2026-10-03.
- [Chaos Mesh GitHub — controllers/README.md (Uber Fx Architecture, One Writer Per Field, Level-Based Reconcilers & Requeue Semantics)](https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/controllers/README.md) — Guia oficial de arquitetura dos controladores do Chaos Mesh detalhando composição com Uber Fx (controllers/fx.go), pipeline comum (desiredphase, condition, records, finalizers), CRDs filhos PodHTTPChaos/PodIOChaos/PodNetworkChaos, regra One writer per field, reconciliação idempotente baseada em nível e semântica do controller-runtime v0.21.; consultado em 2026-10-03.
- [Chaos Mesh — Official GitHub Repository](https://github.com/chaos-mesh/chaos-mesh) — Repositório oficial Apache-2.0 do Chaos Mesh na CNCF.; consultado em 2026-10-03.
