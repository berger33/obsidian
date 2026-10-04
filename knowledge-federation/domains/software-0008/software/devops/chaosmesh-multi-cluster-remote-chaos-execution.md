---
id: software.devops.tranche06.000514
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

# Execução multi-cluster de experimentos de caos a partir de um cluster de gerenciamento no Chaos Mesh

## Em uma frase
O README oficial e o guia `controllers/README.md` documentam o suporte nativo a **execução multi-cluster (`multicluster/`)**: um cluster central de gerenciamento do Chaos Mesh pode registrar clusters Kubernetes remotos e **despachar experimentos de caos suportados para esses clusters remotos**. Conforme detalha `controllers/README.md`, objetos de caos de nível superior que possuem o campo de cluster remoto preenchido (`non-empty remote-cluster field`) são filtrados para fora do pipeline local comum e tratados pelos controladores `multicluster/`, que gerenciam o ciclo de vida do cluster remoto, a criação remota do objeto de caos e a sincronização bidirecional de `status` e `finalizers`.

## Por que importa
Em arquiteturas com dezenas de clusters de borda ou múltiplos clusters regionais, operar painéis e pipelines de caos separados em cada cluster fragmenta a governança; o modo multi-cluster centraliza a definição dos experimentos enquanto sincroniza o status e os finalizers com segurança.

## Como funciona
Utilize o recurso de gerenciamento multi-cluster do Chaos Mesh quando precisar coordenar testes de resiliência em múltiplos clusters a partir de um único plano de controle centralizado.

## Exemplo
A equipe de SRE cria um objeto `PodChaos` no cluster de gerenciamento especificando o nome do cluster remoto de homologação; o controlador `multicluster` replica o experimento no cluster remoto, sincroniza os registros de contêineres afetados de volta para o cluster central e remove os finalizers ao encerrar.

## Limites e trade-offs
Proteja rigorosamente os Secrets `kubeconfig` usados pelo controlador `multicluster` para comunicar-se com os clusters remotos, aplicando permissões RBAC mínimas e rotação periódica de credenciais.

## Como verificar
Verifique nos logs e no status do recurso criado com campo de cluster remoto que o status e as condições foram sincronizados a partir do cluster alvo.

## Conexões
- [[chaosmesh-schedule-workflow-and-statuscheck-orchestration]] — Veja também: Orquestração de experimentos recorrentes, fluxos seriados/paralelos e verificações de saúde com Schedule, Workflow e StatusCheck.
- [[chaosmesh-uber-fx-composition-and-common-reconciliation-pipeline]] — Veja também: Composição modular com Uber Fx (controllers/fx.go) e pipeline comum de reconciliação no Chaos Mesh.

## Fontes
- [Chaos Mesh GitHub — README.md (Fault Coverage, Controller Manager, Chaos Daemon, Dashboard, Workflows & Multi-Cluster)](https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/README.md) — README oficial do Chaos Mesh (projeto CNCF Incubating sob Apache-2.0) detalhando cobertura ampla de falhas (Pod, rede, DNS, HTTP, I/O, tempo/clock skew, stress, kernel, block device, JVM, máquina física, AWS, Azure e GCP), recursos Schedule/Workflow/StatusCheck, execução multi-cluster e os três componentes de runtime Chaos Controller Manager, Chaos Daemon e Chaos Dashboard.; consultado em 2026-10-03.
- [Chaos Mesh GitHub — controllers/README.md (Uber Fx Architecture, One Writer Per Field, Level-Based Reconcilers & Requeue Semantics)](https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/controllers/README.md) — Guia oficial de arquitetura dos controladores do Chaos Mesh detalhando composição com Uber Fx (controllers/fx.go), pipeline comum (desiredphase, condition, records, finalizers), CRDs filhos PodHTTPChaos/PodIOChaos/PodNetworkChaos, regra One writer per field, reconciliação idempotente baseada em nível e semântica do controller-runtime v0.21.; consultado em 2026-10-03.
- [Chaos Mesh — Official GitHub Repository](https://github.com/chaos-mesh/chaos-mesh) — Repositório oficial Apache-2.0 do Chaos Mesh na CNCF.; consultado em 2026-10-03.
