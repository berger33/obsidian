---
id: software.devops.tranche06.000515
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

# Composição modular com Uber Fx (controllers/fx.go) e pipeline comum de reconciliação no Chaos Mesh

## Em uma frase
O guia de arquitetura `controllers/README.md` explica como o `cmd/chaos-controller-manager` monta todos os reconciliadores `controller-runtime` através do framework de injeção de dependências **Uber Fx** em `controllers/fx.go` (`controllers.Module`). Para cada implementação de caos registrada em `chaosimpl.AllImpl` como um par `ChaosImplPair` (`Apply` e `Recover`), o bootstrap comum cria um controlador chamado **`<chaos-name>-pipeline`** que executa um pipeline ordenado compartilhado (`common/`): inicialização de finalizers (`finalizers`), cálculo da fase desejada (`desiredphase`), atualização de condições (`condition`), aplicação/recuperação com registros por alvo (`records`) e limpeza final de finalizers.

## Por que importa
Em vez de cada um dos mais de dez tipos de caos reimplementar sua própria lógica de agendamento de duração, retentativas, finalizers de exclusão e máquina de estados (`Injecting`, `Running`, `Paused`, `Finished`), o pipeline comum em `common/` garante comportamento uniforme e previsível para todos os CRDs do Chaos Mesh.

## Como funciona
Ao depurar ou desenvolver um novo tipo de falha no Chaos Mesh, concentre a implementação específica do tipo apenas nos métodos `Apply` e `Recover` sobre um único alvo dentro de `chaosimpl/`, deixando seleção de alvos, iteração, transições de fase e persistência para o pipeline comum.

## Exemplo
Quando um usuário pausa ou deleta qualquer recurso de caos (`PodChaos`, `StressChaos`, `DNSChaos`), o mesmo pipeline comum `common/` detecta a transição para a fase de recuperação, invoca `ChaosImpl.Recover` para cada alvo registrado e só remove o finalizer quando todos os alvos retornam ao estado normal.

## Limites e trade-offs
Utilize as variáveis de configuração `ENABLED_CONTROLLERS` e `ENABLED_WEBHOOKS` documentadas em `controllers/README.md` (`pkg/config/controller.go`) quando desejar habilitar apenas um subconjunto específico de controladores no seu cluster.

## Como verificar
Inspecione o campo `.status.experiment.desiredPhase`, `.status.conditions` e `.status.experiment.containerRecords` de um recurso de caos ativo para observar as etapas do pipeline comum em ação.

## Conexões
- [[chaosmesh-multi-cluster-remote-chaos-execution]] — Veja também: Execução multi-cluster de experimentos de caos a partir de um cluster de gerenciamento no Chaos Mesh.
- [[chaosmesh-pod-level-child-crds-podhttpchaos-podiochaos-podnetworkchaos]] — Veja também: Reconciliação de CRDs filhos de nível de Pod (PodHTTPChaos, PodIOChaos e PodNetworkChaos) no Chaos Mesh.

## Fontes
- [Chaos Mesh GitHub — README.md (Fault Coverage, Controller Manager, Chaos Daemon, Dashboard, Workflows & Multi-Cluster)](https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/README.md) — README oficial do Chaos Mesh (projeto CNCF Incubating sob Apache-2.0) detalhando cobertura ampla de falhas (Pod, rede, DNS, HTTP, I/O, tempo/clock skew, stress, kernel, block device, JVM, máquina física, AWS, Azure e GCP), recursos Schedule/Workflow/StatusCheck, execução multi-cluster e os três componentes de runtime Chaos Controller Manager, Chaos Daemon e Chaos Dashboard.; consultado em 2026-10-03.
- [Chaos Mesh GitHub — controllers/README.md (Uber Fx Architecture, One Writer Per Field, Level-Based Reconcilers & Requeue Semantics)](https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/controllers/README.md) — Guia oficial de arquitetura dos controladores do Chaos Mesh detalhando composição com Uber Fx (controllers/fx.go), pipeline comum (desiredphase, condition, records, finalizers), CRDs filhos PodHTTPChaos/PodIOChaos/PodNetworkChaos, regra One writer per field, reconciliação idempotente baseada em nível e semântica do controller-runtime v0.21.; consultado em 2026-10-03.
- [Chaos Mesh — Official GitHub Repository](https://github.com/chaos-mesh/chaos-mesh) — Repositório oficial Apache-2.0 do Chaos Mesh na CNCF.; consultado em 2026-10-03.
